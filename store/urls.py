from django.urls import path
from .views import FurnitureListView, HomePageView, ForUsView, ServicesView, DetailFurnitureView, \
    ItemProjectListView, DetailProjectItemView, contact_view, health_check

urlpatterns = [
    path('', HomePageView.as_view(), name='store'),
    path('for-us/', ForUsView.as_view(), name='forus'),
    path('services/', ServicesView.as_view(), name='services'),

    path('category/<slug:slug>/<int:category_id>/', FurnitureListView.as_view(), name='product_list_by_category'),
    path('furniture/details/<slug:slug>/<int:pk>/', DetailFurnitureView.as_view(), name='furniture-details'),

    path('project/<slug:slug>/<int:project_id>/', ItemProjectListView.as_view(), name='product_list_by_project'),
    path('project/item/<slug:slug>/<int:pk>/', DetailProjectItemView.as_view(), name='project-item-detail'),

    path('contacts/', contact_view, name='contacts'),

    path('health/', health_check, name='health-check'),

]
