from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('person-profile', views.person_profile, name='person_profile'),
    path('person-profile/<int:person_id>', views.person_profile_update, name='person_profile_update'),
]
