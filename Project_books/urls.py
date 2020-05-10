"""Project_books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import home_view, create_view, edit_view, view_view, delete_view, edit_global_view, view_global_view, delete_global_view, edit_list_view, view_list_view, delete_list_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create/', create_view),
    path('edit/', edit_view),
    path('view/', view_view),
    path('delete/', delete_view),

    path('edit/<int:id>/', edit_global_view),
    path('view/<int:id>', view_global_view),
    path('delete/<int:id>', delete_global_view),
    
    path('edit_list/', edit_list_view),
    path('view_list/', view_list_view),
    path('delete_list/', delete_list_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
