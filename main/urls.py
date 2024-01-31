from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'solvers', SolverViewSet, basename='solvers')
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'exinsolver', ExInSolverViewSet, basename='exinsolver')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
