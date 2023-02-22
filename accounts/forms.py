from django.contrib.auth import get_user_model

# this get_user_model gets the user model from the AUTH_USER_MODEL which i change it from the default for my custom model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = get_user_model()
        fields = ("email", "username")


# it is not needed to type "password" above because it is shown by default


class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = get_user_model()
        fields = ("email", "username")
