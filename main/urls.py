from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/v1/solvers/', SolverList.as_view()),
    path('api/v1/solvers/<int:pk>/', SolverDetail.as_view()),
    path('api/v1/categories/', CategoriesList.as_view()),
    path('api/v1/categories/<int:pk>', CategoriesDetail.as_view()),
    path('api/v1/ExInSolver/', ExInSolverList.as_view()),
    path('api/v1/ExInSolver/<int:pk>', ExInSolverDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
