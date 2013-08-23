from plone.folder.interfaces import IFolder
from interfaces import IZorionagurra
from five import grok

grok.templatedir('templates')


class ZorionagurraView(grok.View):
    grok.context(IZorionagurra)
    grok.require('zope2.view')
    grok.name('view')


class ZorionagurraMultipleView(grok.View):
    grok.context(IFolder)
    grok.require('zope2.view')
    grok.name('zorionagurra_multiple_view')
