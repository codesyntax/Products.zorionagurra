# -*- coding: utf-8 -*-

# There are three ways to inject custom code here:
#
#   - To set global configuration variables, create a file AppConfig.py.
#       This will be imported in config.py, which in turn is imported in
#       each generated class and in this file.
#   - To perform custom initialisation after types have been registered,
#       use the protected code section at the bottom of initialize().
#   - To register a customisation policy, create a file CustomizationPolicy.py
#       with a method register(context) to register the policy.

import logging
logger = logging.getLogger('zorionagurra')
logger.info('Installing Product')

try:
    import CustomizationPolicy
except ImportError:
    CustomizationPolicy = None

import os, os.path
from Globals import package_home
from Products.CMFCore import utils as cmfutils

try: # New CMF
    from Products.CMFCore import permissions as CMFCorePermissions 
except: # Old CMF
    from Products.CMFCore import CMFCorePermissions

from Products.CMFCore import DirectoryView
from Products.CMFPlone.utils import ToolInit
from Products.Archetypes.atapi import *
from Products.Archetypes import listTypes
from Products.Archetypes.utils import capitalize
from config import *

DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/zorionagurra',
                                    product_globals)

def initialize(context):
    # imports packages and types for registration
    import content


    # Initialize portal content
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    cmfutils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)


