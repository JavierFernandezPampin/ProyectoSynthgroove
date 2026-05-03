from django import forms
from .models import Usuario


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Usuario
        fields = ["usuario", "nombre", "apellido", "mail", "rol"]
        labels = {
            "usuario": "Username",
            "nombre": "Name",
            "apellido": "Surname",
            "mail": "Email",
            "rol": "Role",
        }

    def mail_unico(self):
        mail = self.cleaned_data.get("mail")
        if Usuario.objects.filter(mail=mail).exists():
            raise forms.ValidationError("This email is already registered.")
        return mail

    def comprobar_password(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class LoginForm(forms.Form):
    usuario = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
