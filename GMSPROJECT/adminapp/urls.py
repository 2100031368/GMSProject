from django.urls import path

from . import views
urlpatterns = [
    path("viewareas", views.viewareas, name='viewareas'),

    path("viewusers0/<int:aid>", views.viewusers0, name='viewusers0'),

    path("action0/<int:aid>", views.action0, name='action0'),

    path("aaddarea0",views.aaddarea0, name='aaddarea0' ),
    path("aaddarea1",views.aaddarea1, name='aaddarea1' ),

    path("aeditarea0/<int:aid>", views.editarea0, name='aeditarea0'),
    path("updatearea/<int:aid>", views.updatearea, name='updatearea'),

    path("delarea0/<int:aid>", views.delarea0, name='delarea0'),

    path("adduser0/<int:aid>", views.adduser0, name='adduser0'),
]