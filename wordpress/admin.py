from django.contrib import admin
from wordpress.models import (
    WpCommentmeta,
    WpComments,
    WpLinks,
    WpOptions,
    WpPostmeta,
    WpPosts,
    WpTermRelationships,
    WpTermTaxonomy,
    WpTerms,
    WpUsermeta,
    WpUsers,
)

admin.site.register(WpCommentmeta)
admin.site.register(WpComments)
admin.site.register(WpLinks)
admin.site.register(WpOptions)
admin.site.register(WpPostmeta)
admin.site.register(WpPosts)
admin.site.register(WpTermRelationships)
admin.site.register(WpTermTaxonomy)
admin.site.register(WpTerms)
admin.site.register(WpUsermeta)
admin.site.register(WpUsers)
