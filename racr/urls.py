from django.conf.urls import patterns, include, url
from django.contrib import admin
from racr.views import TimetableViewSet
from rest_framework.routers import DefaultRouter

admin.autodiscover()

router = DefaultRouter()
router.register('timetable', TimetableViewSet, base_name='timetable')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'racr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1/', include(router.urls)),
    url(r'^not-registered/', 'racr.views.not_registered', name='not-registered'),
    url(r'', include('social_auth.urls')),
    url(r'', 'racr.views.main'),
)
