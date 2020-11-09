from django.conf.urls import url
from temp_app import views


urlpatterns = [
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative')
]


# TEMPLATE TAGGING:
app_name = 'temp_app'
