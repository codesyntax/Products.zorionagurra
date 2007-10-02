#!/bin/sh

# recreate the pot file from skin page templates
i18ndude rebuild-pot --pot zorionagurra.pot --create zorionagurra ../skins ../browser 
# append the pot file and the firstly generated one
cat manual.pot >> zorionagurra.pot
cat generated.pot >> zorionagurra.pot
# append new msgids to language specific PO files
i18ndude sync --pot zorionagurra.pot zorionagurra-??.po
i18ndude sync --pot zorionagurra-plone.pot zorionagurra-plone-??.po