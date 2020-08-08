#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gannon Barnett'
SITENAME = 'Gannon Barnett'
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + "/images/propic_2.jpg"
PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Articles', SITEURL),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/gannon-barnett/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# Theme
THEME = "Flex"

# Plugins 
PLUGIN_PATHS = ['pelican-plugins'] 
PLUGINS = []
