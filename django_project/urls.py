from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # this is for admin panel url
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # u can manage ur auth from here
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),  # urls for pages app
    # urls for accounts (REGISTER)
]

# the availabe urls and pages are :
# accounts/login/ [name="login"]
# accounts/logout/ [name="logout"]
# accounts/password_change/ [name="password_change"]
# accounts/password_change/done/ [name="password_change_done"]
# accounts/password_reset/ [name="password_reset"]
# accounts/password_reset/done/ [name="password_reset_done"]
# accounts/reset/<uidb64>/<token>/ [name="password_reset_confirm"]
# accounts/reset/done/ [name="password_reset_complete"]
