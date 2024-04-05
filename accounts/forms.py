from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User=get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name','email',]

    def clean_password2(self):
        '''
        Verify both passwords match.
        '''
        #cleaned_data = super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['full_name','email', 'password','active','admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class GuestForm(forms.Form):
	email=forms.EmailField()


class LoginForm(forms.Form):
	email=forms.EmailField(label = 'Email')
	password=forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name','email',]

    def clean_password2(self):
        '''
        Verify both passwords match.
        '''
        #cleaned_data = super().clean()
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #user.active = False
        if commit:
            user.save()
        return user

'''class RegisterForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(
		attrs={
		"class":"form-control"
		}))
	email=	 forms.EmailField(widget=forms.TextInput(
		attrs={
		"class":"form-control"
		}))
	password=forms.CharField(widget=forms.PasswordInput(
		attrs={"class":"form-control"}))
	password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
	
	def clean_username(self):
		username=self.cleaned_data.get('username')
		qs=User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username already taken")
		return username

	def clean_email(self):
		email=self.cleaned_data.get('email')
		qs=User.objects.filter(username=email)
		if qs.exists():
			raise forms.ValidationError("email already taken")
		return email

	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		if password!=password2:
			raise forms.ValidationError("password must match")
		return data
'''
