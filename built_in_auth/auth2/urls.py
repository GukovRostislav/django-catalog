from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('sign-up/', SignUpView.as_view(), name='sign_up_e'),
    path('logout/', logout_view, name='logout'),
    path('s', s, name='s'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:id>', catalog_product, name='catalog_product'),
    path('contacts/', contacts, name='contacts'),
    path('projects/', projects, name='projects'),
    path('projects/<int:id>', project, name='project'),
    path('consultation/', consultation, name='consultation'),
]
