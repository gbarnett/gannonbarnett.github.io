#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gannon Barnett'
SITENAME = 'Gannon Barnett'
SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-118783637-2"
SITELOGO = SITEURL + "/images/pro_pic_aug2020.png"
PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Articles', SITEURL), ('resume', SITEURL + '/pdfs/GannonBarnett-8_17_2020.pdf'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/gannon-barnett/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Theme
THEME = "flex-theme"

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = []
