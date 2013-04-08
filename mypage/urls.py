from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    url(r'^$', 'web_api_calls.views.tumblr_api', name='home'),
    url(r'^github', 'web_api_calls.views.github_api', name='home'),
    # url(r'^mypage/', include('mypage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
