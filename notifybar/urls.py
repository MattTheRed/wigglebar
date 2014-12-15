from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from bar.views import BuilderView, dashboard, CreateBar, ViewBar, HomePage, UpdateBar
from register_user.views import RegistrationView, account_profile
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notifybar.views.home', name='home'),
    # url(r'^notifybar/', include('notifybar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePage.as_view()),
    url(r'^home/', HomePage.as_view()),
    url(r'^view/(?P<pk>[\d]+)/initialize.js', ViewBar.as_view()),
    #url(r'^l/(?P<slug>(.*))/$', shortlink.redirect, name="shortlink"),
    url(r'^users/(?P<username>(.*))/$', dashboard, name="dashboard"),
    url(r'^bar/create/', CreateBar.as_view(), name="create_bar"),
    url(r'^bar/edit/(?P<pk>\d+)/$', login_required(UpdateBar.as_view()), name="edit_bar"),
    url(r'^subscribe/', TemplateView.as_view(template_name="registration/subscribe.html"), name="subscribe"),

    url(r'^notifybar/directives/palette-picker.html', TemplateView.as_view(template_name="palette-picker.html")),
    url(r'^notifybar/directives/icon-picker.html', TemplateView.as_view(template_name="icon-picker.html")),
    url(r"^payments/", include("payments.urls")),
    url(r'^accounts/profile/$', account_profile, name="account_profile")


)

urlpatterns += patterns('',
    url(r'^accounts/register/$',
       RegistrationView.as_view(),
       name='registration_register'),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$',
       auth_views.login,
       {'template_name': 'registration/login.html'},
       name='auth_login'),
    url(r'^accounts/logout/$',
       auth_views.logout,
       {'template_name': 'registration/logout.html'},
       name='auth_logout'),
    url(r'^password/change/$',
       auth_views.password_change,
       name='auth_password_change'),
    url(r'^accounts/password/change/done/$',
       auth_views.password_change_done,
       name='auth_password_change_done'),
    url(r'^accounts/password/reset/$',
       auth_views.password_reset,
       name='auth_password_reset'),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
       auth_views.password_reset_confirm,
       name='auth_password_reset_confirm'),
    url(r'^accounts/password/reset/complete/$',
       auth_views.password_reset_complete,
       name='auth_password_reset_complete'),
    url(r'^accounts/password/reset/done/$',
       auth_views.password_reset_done,
       name='auth_password_reset_done'),
)


    #(r'^accounts/', include('registration.backends.simple.urls')),


#http://stackoverflow.com/questions/5517950/django-media-url-and-media-root
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

