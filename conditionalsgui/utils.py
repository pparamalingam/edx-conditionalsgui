# Utilities to help with processing #

import pkg_resources
import logging
import os
import sys
import fnmatch


from lxml import etree

# Globals ###########################################################

log = logging.getLogger(__name__)


def load_resource(path):
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, 'verticle.xml'):
            tree = etree.parse(file)
            root = tree.getroot()
            print(root.tag)

def process_resource(obj):
	return null
