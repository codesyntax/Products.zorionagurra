# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo

try:
    from Products.LinguaPlone.public import *
except ImportError:
    from Products.Archetypes.atapi import *

from Products.zorionagurra.config import *

schema = Schema((

    StringField(
        name='name',
        widget=StringWidget(
            label='Name',
            label_msgid='zorionagurra_label_name',
            description_msgid='zorionagurra_help_name',
            i18n_domain='zorionagurra',
        )
    ),

    StringField(
        name='surname',
        widget=StringWidget(
            label='Surname',
            label_msgid='zorionagurra_label_surname',
            description_msgid='zorionagurra_help_surname',
            i18n_domain='zorionagurra',
        )
    ),

    StringField(
        name='title',
        widget=StringWidget(
            label='Title',
            label_msgid='zorionagurra_label_title',
            description_msgid='zorionagurra_help_title',
            i18n_domain='zorionagurra',
        )
    ),

    TextField(
        name='text',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Text',
            label_msgid='zorionagurra_label_text',
            description_msgid='zorionagurra_help_text',
            i18n_domain='zorionagurra',
        ),
        default_output_type='text/html',
        searchable=1
    ),

    ImageField(
        name='photo',
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

class Zorionagurra(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Zorionagurra'

    meta_type = 'Zorionagurra'
    portal_type = 'Zorionagurra'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'Zorionagurra.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Zorionagurra"
    typeDescMsgId = 'description_edit_zorionagurra'

    _at_rename_after_creation = True

    schema = Zorionagurra_schema

    # Methods


registerType(Zorionagurra, PROJECTNAME)



