from django.views.generic import View
from forum import models


class BaseForumView(View):

    def _get_context(self):
        return {'categories': models.Category.objects.all()}