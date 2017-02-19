# -*- coding: utf-8 -*-

# Basic blog details
BLOG_AUTHOR = "BLOG_AUTHOR"
BLOG_TITLE = "Libretto"
BLOG_DESCRIPTION = "You can write a brief (or long!) description of your " \
                   "blog here."
SITE_URL = "https://note2self.abraham-v.com/libretto-theme-for-nikola/"
BLOG_EMAIL = "no@email.here"
TIMEZONE = "America/Toronto"

# Blog configuration
THEME = "libretto"
DEFAULT_LANG = "en"
INDEX_DISPLAY_POST_COUNT = 4
INDEX_TEASERS = True
INDEX_PATH = "posts"
IMAGE_FOLDERS = {
    'images': 'images'
}
POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst", "", "story.tmpl"),
)
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/", "Home"),
        ("/posts/index.html", "Blog"),
        ("/archive.html", "Archives"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}
# Configs to remove warnings
WRITE_TAG_CLOUD = True
USE_BUNDLES = False

# Third party integrations
COMMENT_SYSTEM = ""

##########################
# Optional Blog settings

# Small notice near bottom of every page
# <a> tag is optional
CONTENT_FOOTER = "Contents © 2017 <a href='mailto:please@no.spam'>Abraham Varricatt</a>"

# Social media links, will generate icons near bottom of every page
# WARNING: This usage is NOT the same as on other Nikola themes!!
# On this theme, we make a dictionary of links.
# The theme tries to figure out the icon based on links in the dictionary.
# Supported sites are - dribbble.com, facebook.com, flickr.com, google.com,
# instagram.com, linkedin.com, pinterest.com, getpocket.com, reddit.com,
# stumbleupon.com, tumblr.com, twitter.com, vimeo.com, youtube.com
# Sites not in this list will get a star icon.
# NOTE: The order of these buttons is ALWAYS randomized each time you build a
# new version of your site.
SOCIAL_BUTTONS_CODE = {
    'https://twitter.com/GetNikola',
    'https://www.linkedin.com/in/abrahamvarricatt/',
    'https://github.com/abrahamvarricatt/',
    'http://www.facebook.com/',
    'https://www.reddit.com/r/civ/',
}

