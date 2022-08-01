# api/urls.py

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'upcomings', views.UpcomingViewSet, basename='upcomings')
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('upcomings/<int:user_id>/', views.UpcomingViewSet.as_view({'get':'upcomings'})),
    path('upcomings/<int:pk>/orders/', views.UpcomingViewSet.as_view({'get':'orders', 'post':'orders'})),
    path('upcomings/<int:pk>/orders/<int:order>/', views.UpcomingViewSet.as_view({'delete':'remove_order'})),
    path('upcomings/<int:pk>/ratings/', views.UpcomingViewSet.as_view({'get':'ratings', 'post':'ratings'})),
    path('upcomings/<int:pk>/ratings/<int:rating>/', views.UpcomingViewSet.as_view({'delete':'remove_rating'})),
    path('upcomings/<int:pk>/comments/', views.UpcomingViewSet.as_view({'get':'comments', 'post':'comments'})),
    path('upcomings/<int:pk>/comments/<int:comment>/', views.UpcomingViewSet.as_view({'delete':'remove_comment'})),
]