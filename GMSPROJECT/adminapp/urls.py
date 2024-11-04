from django.urls import path

from . import views
urlpatterns = [
    path("adminhome", views.adminhome, name='adminhome'),

    path("viewareas", views.viewareas, name='viewareas'),

    path("action0/<int:aid>", views.action0, name='action0'),

    path("aaddarea0",views.aaddarea0, name='aaddarea0' ),
    path("aaddarea1",views.aaddarea1, name='aaddarea1' ),
    path("aeditarea0/<int:aid>", views.editarea0, name='aeditarea0'),
    path("updatearea/<int:aid>", views.updatearea, name='updatearea'),
    path("delarea0/<int:aid>", views.delarea0, name='delarea0'),

    path("viewusers0/<int:aid>", views.viewusers0, name='viewusers0'),
    path("adduser0/<int:aid>", views.adduser0, name='adduser0'),
    path("edituser0/<int:uid>", views.edituser0, name='edituser0'),
    path("deleteuser0/<int:uid>", views.deleteuser0, name='deleteuser0'),

    path("viewgrelist",views.viewgrelist, name='viewgrelist'),
    path("readgre/<int:gid>", views.readgre, name='readgre'),
    path("update_issue_status/<int:gid>", views.update_issue_status, name='update_issue_status'),

    path("aeditreq0", views.editreq0, name='editreq0'),
    path("aeditreq1/<int:eid>/<int:flag>", views.editreq1, name='aeditreq1'),

    path("aaddsubadmin0/<int:id>", views.aaddsubadmin0, name='aaddsubadmin0'),
    path("aaddsubadmin1/<int:id>/<int:uid>", views.aaddsubadmin1, name='aaddsubadmin1'),
    path("viewsubadmin", views.viewsubadmin, name='viewsubadmin'),
    path("adenysubadmin/<int:uid>", views.adenysubadmin, name='adenysubadmin'),

    path("workanalysis/<int:uid>", views.workanalysis, name='workanalysis'),

    path("viewsendnotify", views.viewsendnotify,name='viewsendnotify'),
    path("viewrecnotify", views.viewrecnotify, name='viewrecnotify'),
    path("readnotify/<int:id>", views.readnotify, name='readnotify'),
    path("sendnotify/<int:uid>", views.sendnotify, name='sendnotify'),
    path("deletenotify/<int:id>", views.deletenotify, name='deletenotify'),
]