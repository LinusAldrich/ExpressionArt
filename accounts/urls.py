from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),  
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('link_invalid/', views.linkValid, name="link_invalid"),
    path('landing_page/', views.landingPage, name="landing_page"),

    path('', views.home, name="home"),
    path('diary/<str:pk_test>/', views.diary, name="diarys"),
    path('clients/<str:pk_test>/', views.client, name="clients"),

    path('create_diary/<str:pk>/', views.createDiary, name="create_diarys"),
    path('update_diary/<str:pk_test>/', views.updateDiary, name="update_diarys"),
    path('delete_diary/<str:pk>/', views.deleteDiary, name="delete_diarys"),

    path('canvas/<str:pk_test>/', views.canvas, name="canvass"),
    path('canvas_creator/<str:pk_test>/', views.canvasCreator, name="canvas_creator"),
    path('upload_canvas/<str:pk>', views.uploadCanvas, name="upload_canvas"),
    path('delete_canvas/<str:pk>/', views.deleteCanvas, name="delete_canvas"),
    path('edit_canvas/<str:pk>/', views.editCanvas, name="edit_canvas"),
    path('redirect_canvas/', views.savingCanvas, name="saving_canvas"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),


    path('collage/<str:pk_test>/', views.collage, name="collages"),
    path('collage_creator/<str:pk_test>/', views.createCollage, name="collage_creator"),
    path('upload_collage/<str:pk_test>/', views.uploadCollage, name="upload_collage"),
    path('delete_collage/<str:pk>/', views.deleteCollage, name="delete_collage"),
]

urlpatterns += staticfiles_urlpatterns()