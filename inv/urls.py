from django.urls import path
from .views import(
    ComprobacionGastosListView,
    ComprobacionGastosDetailView,
    ComprobacionGastosCreateView,
    ComprobacionGastosUpdateView,
    ComprobacionGastosDeleteView,
    UserComprobacionGastosListView
)
from . import views

urlpatterns = [
    path('', ComprobacionGastosListView.as_view(), name="inv-home"),
    path('user/posts/<str:username>', UserComprobacionGastosListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', ComprobacionGastosDetailView.as_view(), name="post-detail"),
    path('post/new/', ComprobacionGastosCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', ComprobacionGastosUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', ComprobacionGastosDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="inv-about"),
]

