"""
URL configuration for product_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.shortcuts import redirect

# Router
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

# Optional: redirect /api/docs/ to default version (v1)
def docs_redirect(request):
    return redirect('/api/v1/docs/')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Versioned API
    path('api/<str:version>/', include(router.urls)),

    # Versioned schema & Swagger
    path('api/<str:version>/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/<str:version>/docs/', SpectacularSwaggerView.as_view(url_name='schema')),

    # Redirect unversioned docs to v1
    path('api/docs/', docs_redirect),
]
