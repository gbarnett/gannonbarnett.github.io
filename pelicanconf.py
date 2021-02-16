#/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gannon Barnett'
SITENAME = 'Gannon Barnett'
SITEURL = ''
RELATIVE_URLS = False
GOOGLE_ANALYTICS = "UA-118783637-2"
SITELOGO = SITEURL + "/images/pro_pic_aug2020.png"
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('resume', SITEURL + '/pdfs/GannonBarnett-8_17_2020.pdf'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/gannon-barnett/'),)

DEFAULT_PAGINATION = False

THEME = "flex-theme"

DEFAULT_METADATA = {
    'status': 'draft',
}

#DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default

DELETE_OUTPUT_DIRECTORY = True
