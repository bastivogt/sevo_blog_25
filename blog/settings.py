from django.conf import settings


# defaults
POST_FEATURED = False
POST_ALLOW_COMMENTS = True
POST_SHOW_COMMENTS = True
POST_PUBLISHED = True


if hasattr(settings, "POST_FEATURED"):
    POST_FEATURED = settings.POST_FEATURED


if hasattr(settings, "POST_ALLOW_COMMENTS"):
    POST_ALLOW_COMMENTS = settings.POST_ALLOW_COMMENTS


if hasattr(settings, "POST_SHOW_COMMENTS"):
    POST_SHOW_COMMENTS = settings.POST_SHOW_COMMENTS


if hasattr(settings, "POST_PUBLISHED"):
    POST_PUBLISHED = settings.POST_PUBLISHED