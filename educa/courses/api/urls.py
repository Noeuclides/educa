from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'courses'
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('asignaturas/', views.SubjectListView.as_view(), name='subject_list'),
    path('asignaturas/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('cursos/<pk>/registrarse', views.CourseEnrollView.as_view(), name='course_enroll'),
    path('', include(router.urls)),
]
