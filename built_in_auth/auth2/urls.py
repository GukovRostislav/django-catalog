from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sign-up/', SignUpView.as_view(), name='sign_up_e'),
    path('logout/', logout_view, name='logout'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:id>', catalog_product, name='catalog_product'),
    path('contacts/', contacts, name='contacts'),
    path('projects/', projects, name='projects'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/like/<int:id>', like, name='like'),
    path('projects/<int:id>', project, name='project'),
    path('consultation/', consultation, name='consultation'),
    path('request_leave/', request_leave, name='request_leave'),
]
