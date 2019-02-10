from collections import namedtuple

from webpreview import OpenGraph, TwitterCard


def get_webpreview(url):
    """Gets the web preview for URL."""
    WebPrev = namedtuple('WebPrev', ['title', 'description', 'image'])

    og = OpenGraph(url, {'og:title', 'og:description', 'og:image'})
    tc = TwitterCard(url, {'twitter:title', 'twitter:description',
                           'twitter:image'})

    title = og.title or tc.title
    description = og.description or tc.description
    image = og.image or tc.image
    return WebPrev(title=title, description=description, image=image)
