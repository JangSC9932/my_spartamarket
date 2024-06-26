from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = {
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'profile_pic',
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = {
            'first_name',
            'last_name',
            'profile_pic',
        }
