__version__ = '$Id$'

from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from DateTime import DateTime

class LastZorionagurrak(BrowserView):

    def getLastZorionagurrak(self, num=5):
        context = aq_inner(self.context)

        today = DateTime().earliestTime()
        todayend = DateTime().latestTime()
        tomorrow = today + 1

        pcal = getToolByName(context, 'portal_catalog')
        todaybrains = pcal(portal_type='Zorionagurra',
                           review_state='published',
                           getDate={'query':(today, todayend),
                                    'range':'min:max'},
                           sort_on='getDate',
                           sort_limit=num)
        
        todaybrainnumber = len(todaybrains)
        if todaybrainnumber >= num:
            return todaybrains

        else:
            tomorrowbrainnumber = num - todaybrainnumber
            tomorrowbrains = pcal(portal_type='Zorionagurra',
                                  review_state='published',
                                  getDate={'query':(todayend,),
                                           'range':'min'},
                                  sort_on='getDate',
                                  sort_limit=tomorrowbrainnumber)

            return todaybrains + tomorrowbrains
