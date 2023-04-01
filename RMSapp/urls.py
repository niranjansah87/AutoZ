# from django.urls import path,include
from . import views
from django.urls import path,include, re_path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import CustomLoginView
urlpatterns = [
    # path('login/',views.Login,name="login"),
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.Logout,name="logout"),
    path('user/<int:pk>/profile/',views.Profile,name="profile"),
    path('forgotpassword/',views.forgotpassword, name='forgotpassword'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('account-deleted/', views.Account_Deleted, name='account_deleted'),
    # path('activate/<uidb64>/<token>',Verification.as_view(),name="activate"),
    
    
    
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]











