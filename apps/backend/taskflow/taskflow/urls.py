from django.contrib import admin
from django.urls import path, include
from signup import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("signup/", v.signup, name="signup"),
    path("", include("main.urls")),
]
