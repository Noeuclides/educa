from django.urls import path
from . import views


urlpatterns = [
    path('propios/', views.ManageCourseListView.as_view(),
         name='manage_course_list'),

    path('crear/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/editar/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/eliminar/', views.CourseDeleteView.as_view(), name='course_delete'),

    path('<pk>/modulo/', views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),

    path('modulo/<int:module_id>/contenido/<model_name>/crear/',
         views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('modulo/<int:module_id>/contenido/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('contenido/<int:id>/eliminar/', views.ContentDeleteView.as_view(),
         name='module_content_delete'),

    path('modulo/<int:module_id>/', views.ModuleContentListView.as_view(),
         name='module_content_list'),

    path('modulo/orden/', views.ModuleOrderView.as_view(), name='module_order'),
    path('contenido/orden/', views.ContentOrderView.as_view(), name='content_order'),

    path('asignatura/<slug:subject>/', views.CourseListView.as_view(),
         name='course_list_subject'),
    path('<slug:slug>/', views.CourseDetailView.as_view(),
         name='course_detail'),
]
