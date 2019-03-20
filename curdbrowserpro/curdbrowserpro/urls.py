from django.conf.urls import include, url
from django.contrib import admin
from curdapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'curdbrowserpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.homeview),
    url(r'^create/',views.insertview),
    url(r'^retrive/',views.retriveview),
    url(r'^update/',views.updateview),
    url(r'^delete/',views.deleteview),
]
