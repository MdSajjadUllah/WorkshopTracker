from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # public routes
    path("", views.landing, name="landing"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # admin approval routes
    path("approve-users/", views.approve_users, name="approve_users"),
    path("approve-user/<int:user_id>/", views.approve_user, name="approve_user"),
    path("delete-user/<int:user_id>/", views.delete_user, name="delete_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
