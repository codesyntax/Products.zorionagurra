# -*- coding: utf-8 -*-

try:
    from Products.LinguaPlone.public import *
except ImportError:
    from Products.Archetypes.atapi import *

from zope.interface import implements
from Products.zorionagurra.config import PROJECTNAME
from ..interfaces import IZorionagurra
import DateTime

schema = Schema((

    StringField(
        name='name',
        required=1,
        searchable=0,
        widget=StringWidget(
            label='Name',
            label_msgid='zorionagurra_label_name',
            description_msgid='zorionagurra_help_name',
            i18n_domain='zorionagurra',
        )
    ),

    StringField(
        name='surname',
        required=1,
        searchable=0,
        widget=StringWidget(
            label='Surname',
            label_msgid='zorionagurra_label_surname',
            description_msgid='zorionagurra_help_surname',
            i18n_domain='zorionagurra',
        )
    ),

    DateTimeField(
        name='date',
        languageIndependent=True,
        default=DateTime.DateTime(),
        widget=CalendarWidget(
            show_hm=False,
            label="Date",
            description='Select the day of this element',
            label_msgid='zorionagurra_label_date',
            description_msgid="zorionagurra_help_date",
            i18n_domain="zorionagurra",
            ),
    ),

    ComputedField(
        name='title',
        expression='context.computeFullname()',
        searchable=1,
        accessor='Title',
        widget=StringWidget(
            label='Title',
            label_msgid='zorionagurra_label_title',
            description_msgid='zorionagurra_help_title',
            i18n_domain='zorionagurra',
            visible={'view': 'visible',
                     'edit': 'invisible',
                     'roster_list': 'visible',
                     },
        )
    ),

    TextField(
        name='text',
        required=1,
        searchable=1,
        allowable_content_types=('text/plain',),
        widget=TextAreaWidget(
            rows=5,
            cols=40,
            label='Text',
            label_msgid='zorionagurra_label_text',
            description_msgid='zorionagurra_help_text',
            i18n_domain='zorionagurra',
        ),
        default_output_type='text/plain',
        default_content_type='text/plain',
    ),

    ImageField(
        name='photo',
        required=1,
        sizes={
              'thumb': (50, 50),
              'mini': (150, 150),
              'preview': (400, 400),
              },
        widget=ImageWidget(
            label='Photo',
            label_msgid='zorionagurra_label_photo',
            description_msgid='zorionagurra_help_photo',
            i18n_domain='zorionagurra',
        ),
        storage=AttributeStorage()
    ),

),
)

Zorionagurra_schema = BaseSchema.copy() + \
    schema.copy()

Zorionagurra_schema['description'].required = 0
Zorionagurra_schema['description'].widget.visible = {'edit': 'hidden',
                                                     'view': 'hidden',
                                                     }

class Zorionagurra(BaseContent):
    """ Birthday greeting """
    implements(IZorionagurra)

    portal_type = 'Zorionagurra'

    schema = Zorionagurra_schema

    # Methods
    def at_post_create_script(self):
        """ Post creation hook """
        self._renameAfterCreation()
        self.setExpirationDate(DateTime.DateTime(self.getDate()).earliestTime() + 1)

    def at_post_edit_script(self):
        """ Post edit hook """
        self.setExpirationDate(DateTime.DateTime(self.getDate()).earliestTime() + 1)

    def computeFullname(self):
        name = self.getField('name').getAccessor(self)()
        surname = self.getField('surname').getAccessor(self)()
        if name and surname:
            space = ' '
        else:
            space = ''
        return "%s%s%s" % (name, space, surname)

    def Description(self):
        """ Return the description """

        return self.getText()

    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.Title()
        return self.getField('photo').tag(self, **kwargs)


registerType(Zorionagurra, PROJECTNAME)
