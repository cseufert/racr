from racr import models
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def associate_user(*args, **kwargs):
    user = kwargs.get("user")
    try:
        models.User.objects.get(user=user)
    except models.User.DoesNotExist:
        return HttpResponseRedirect(reverse('not-registered'))
