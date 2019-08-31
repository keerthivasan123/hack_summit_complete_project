from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('laptops', views.display_laptops, name="display_laptops"),
    path('desktops', views.display_desktops, name="display_desktops"),
    path('mobiles', views.display_mobiles, name="display_mobiles"),

    path('add_laptop', views.add_laptop, name="add_laptop"),
    path('add_desktop', views.add_desktop, name="add_desktop"),
    path('add_mobile', views.add_mobile, name="add_mobile"),

    path('laptops/edit_item/(?P<pk>\d+)', views.edit_laptop, name="edit_laptop"),
    path('desktops/edit_item/(?P<pk>\d+)', views.edit_desktop, name="edit_desktop"),
    path('mobiles/edit_item/(?P<pk>\d+)', views.edit_mobile, name="edit_mobile"),

    path('laptops/delete/(?P<pk>\d+)', views.delete_laptop, name="delete_laptop"),
    path('desktops/delete/(?P<pk>\d+)', views.delete_desktop, name="delete_desktop"),
    path('mobiles/delete/(?P<pk>\d+)', views.delete_mobile, name="delete_mobile")
    
]

 