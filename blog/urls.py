from django.contrib import admin
from django.urls import path
from django.conf import settings
from django_mongoengine import mongo_admin
from blogapp.views import BlogAPI,BlogDetailsBy_ID,PostDetail,PostList
from user.views import Register
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mongoadmin/', mongo_admin.site.urls),
    path('blogdata/',BlogAPI.as_view()),
    path('blogid/<str:id>/',BlogDetailsBy_ID.as_view()),
    path('register/',Register.as_view()),
    path('postt',PostList.as_view(), name='home'),
    path('podetail/',PostDetail.as_view(), name='post_detail'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view()),

]
