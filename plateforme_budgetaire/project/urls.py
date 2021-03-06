from django.conf.urls import patterns, url
from project.views import *

urlpatterns = patterns(
    '',
    url(
        r'^view/(?P<pk>\d+)$',
        ProjectDetail.as_view(),
        name='project_detail'
    ),
    url(
        r'^(?P<validated>0|1|2)$',
        ProjectList.as_view(),
        name='project_list'
    ),
    url(
        r'^create/$',
        ProjectCreate.as_view(),
        name='project_create'
    ),
    url(
        r'^list/$',
        ProjectList.as_view(),
        {"validated": "all"},
        name='project_list'
    ),
    url(
        r'^subCreate/(?P<projectID>\d+)$',
        SubProjectCreate.as_view(),
        name='subproject_create'
    ),
    url(
        r'^(?P<pk>\d+)/update/$',
        ProjectUpdate.as_view(),
        name='project_update'
    ),
    url(
        r'^(?P<pk>\d+)/subUpdate/$',
        SubProjectUpdate.as_view(),
        name='subproject_update'
    ),
    url(
        r'^subDelete/(?P<subProjectID>\d+)$',
        SubProjectDelete.as_view(),
        name='subproject_delete'
    ),
    url(
        r'^delete/(?P<pk>\d+)$',
        ProjectDelete.as_view(),
        name='project_delete'
    ),

    # Function
    url(
        r'^accept/(?P<pk>\d+)$',
        AcceptProject.as_view(),
        name="project_accept"
    ),
    url(
        r'^refuse/(?P<pk>\d+)$',
        RefuseProject.as_view(),
        name="project_refuse"
    ),
)
