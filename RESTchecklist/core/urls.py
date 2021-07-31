from os import name
from django.urls import path
from . import views
from .views import CheckListAPIView,CheckListsAPIView,CheckListItemCreateAPIView,CheckListItemAPIView
urlpatterns = [
    # path('',views.test_api,name="test_api"),
    # path('',TestAPIView.as_view()),
    path('author/',views.author),
    path('api/checklists/',CheckListAPIView.as_view()),
    path('api/checklists/<int:pk>',CheckListsAPIView.as_view()),
    path('api/checklistItem/create',CheckListItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>',CheckListItemAPIView.as_view()),
]
