
from .import views
from django.urls import path
urlpatterns = [
    path("userhome", views.userhome, name='userhome'),

    path("viewmygre0", views.viewmygre0, name='viewmygre0'),
    path("editmygre0/<int:gid>", views.editmygre0, name='editmygre0'),
    path("delmygre0/<int:gid>", views.delmygre0, name='delmygre0'),
    path("postgre0", views.postgre0, name='postgre0'),

    path("editmydetails0", views.editmydetails0, name='editmydetails0'),
    path("editmobile", views.editmobile, name='editmobile'),
    path("editname", views.editname, name='editname'),
    path("editaddr", views.editaddr, name='editaddr'),
    path("editarea0", views.editarea0, name='editarea0'),
    path("editarea1", views.editarea1, name='editarea1'),

    path("myedits", views.myedits, name='myedits'),
    path("delmyreq/<int:eid>", views.delmyreq, name='delmyreq'),
]