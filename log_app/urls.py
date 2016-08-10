from django.conf.urls import url

from log_app.views import *

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^login/$',  csrf_exempt(LoginFormView.as_view()), name='login'),
    # url(r'^logout/$', LogoutView.as_view()),
    url(r'^$', view=index, name='index'),
    url(r'^login/$', view=login_user, name='login'),
    url(r'^logout/$', view=logout_user),
    # url(r'^register/$', view=register_user),
    url(r'^register/$', RegisterFormView.as_view()),
]
