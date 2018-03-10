from django.conf.urls import url, include
from . import views
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),

    url(r'^emplist', views.EmpList.as_view(), name='employee-list'),
    url(r'^empdetails/(?P<pk>[0-9]+)$', views.EmpDetails.as_view(), name='employee-detail'),
    url(r'^employeedetails/(?P<pk>[0-9]+)$', views.EmployeeDetails.as_view(), name='employee-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^empview', views.EmpListView.as_view(), name='empListview'),
    url(r'^userlistview', views.UserListView.as_view(), name='userlistview'),
    url(r'^$', views.api_root, name='api-root'),
    url(r'^empinfo/(?P<pk>[0-9]+)/highlight/$', views.EmployeeHighlight.as_view(), name='employee-highlight'),
]
