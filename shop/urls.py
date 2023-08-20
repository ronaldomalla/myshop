from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Login,Signup
urlpatterns = [
    path('',views.index,name='home' ),
    path('signup/',Signup.as_view(),name='signup'),
    path("login/", Login.as_view(), name="login"),
    path('logout/', views.logout,name="logout"),
    path('cart/', views.cart,name="cart"),


]+static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
