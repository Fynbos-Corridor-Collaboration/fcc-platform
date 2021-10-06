from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gardens/", views.gardens, name="gardens"),
    path("gardens/<int:id>/", views.garden, name="garden"),
    path("gardens/<int:garden>/photos/", views.photos, name="garden_photos"),
    path("maps/", views.maps, name="maps"),
    path("maps/<int:id>/", views.map, name="map"),
    path("space/<int:id>/", views.space, name="space"),
    path("geojson/<int:id>/", views.geojson, name="geojson"),
    path("report/", views.report, name="report"),
    path("report/map/", views.report, {"show_map": True}, name="report_map"),
    path("report/<str:lat>/<str:lng>/", views.report, name="report"),
    path("species/", views.species_overview, name="species"),
    path("species/all/", views.species_full_list, name="species_full_list"),
    path("species/search/", views.species_full_list, name="species_search"),
    path("species/<int:id>/", views.species, name="species"),
    path("species/genus/<int:genus>/", views.species_list, name="genus"),
    path("species/family/<int:family>/", views.species_list, name="family"),
    path("vegetation-types/", views.vegetation_types, name="vegetation_types"),
    path("vegetation-types/<slug:slug>/", views.vegetation_type, name="vegetation_type"),
    path("vegetation-types/<slug:vegetation_type>/species/", views.species_overview, name="vegetation_type_species"),

    path("profile/<str:lat>,<str:lng>/", views.profile, name="profile"),
    path("profile/<str:lat>,<str:lng>/<slug:section>/", views.profile, name="profile"),
    path("profile/<str:lat>,<str:lng>/<slug:section>/<slug:subsection>/", views.profile, name="profile"),

    path("profile/<int:id>/", views.profile, name="profile"),
    path("profile/<int:id>/<slug:section>/", views.profile, name="profile"),

    path("photos/", views.photos, name="photos"),

    path("accounts/login/", views.user_login, name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
]
