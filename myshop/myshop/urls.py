from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import logins, logout_view, register_user_view, view_profile, edit_profile

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
   ## url(r'^accounts/', include('accounts.urls', namespace='accounts')),

    ##user auth urls
    url(r'^accounts/login/$', logins, name='logins'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^accounts/register/$', register_user_view, name='register'),
    url(r'^accounts/profile/$', view_profile, name='profile'),
    url(r'^accounts/profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^', include('shop.urls', namespace='shop')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
