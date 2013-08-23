from DateTime import DateTime
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.zorionagurra import zorionagurraMessageFactory as _

from zope.i18nmessageid import MessageFactory
__ = MessageFactory("plone")


class IZorionagurraPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IZorionagurraPortlet)

    def __init__(self):
        pass

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return __(u"Zorionagurra Portlet")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('zorionagurraportlet.pt')

    def get_latest(self, num=5):
        context = aq_inner(self.context)

        today = DateTime().earliestTime()
        todayend = DateTime().latestTime()
        pcal = getToolByName(context, 'portal_catalog')
        todaybrains = pcal(portal_type='Zorionagurra',
                           review_state='published',
                           getDate={'query': (today, todayend),
                                    'range': 'min:max'},
                           sort_on='getDate',
                           sort_limit=num)

        todaybrainnumber = len(todaybrains)
        if todaybrainnumber >= num:
            return todaybrains

        else:
            tomorrowbrainnumber = num - todaybrainnumber
            tomorrowbrains = pcal(portal_type='Zorionagurra',
                                  review_state='published',
                                  getDate={'query': (todayend,),
                                           'range': 'min'},
                                  sort_on='getDate',
                                  sort_limit=tomorrowbrainnumber)

            return todaybrains + tomorrowbrains


# NOTE: If this portlet does not have any configurable parameters, you can
# inherit from NullAddForm and remove the form_fields variable.
class AddForm(base.NullAddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    def create(self, data):
        return Assignment(**data)


