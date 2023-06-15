from django import forms

from users.models import User


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=50, required=True)

    def save(self, *args):
        user = User.objects.create(
            username=self.cleaned_data["login"],
            email=self.cleaned_data["email"],
            first_name=self.cleaned_data["name"],
            last_name=self.cleaned_data["lastname"],
        )
        user.set_password(self.cleaned_data["password"])
        user.save(update_fields=["password"])
        return user


class ResetPassword(forms.Form):
    email = forms.EmailField()
