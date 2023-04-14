from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='아이디')
    email = forms.CharField(label='이메일')
    last_name = forms.CharField(label='성')
    first_name = forms.CharField(label='이름')
    birthday = forms.DateField(label='생년월일', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    image = forms.ImageField(label='프로필 사진')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput, help_text='문자 포함 8자이상 입력해 주세요')
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput, help_text='비밀번호를 정확히 입력해 주세요')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'image', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(label='이메일')
    first_name = forms.CharField(label='이름')
    last_name = forms.CharField(label='성')
    birthday = forms.DateField(label='생년월일', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    image = forms.ImageField(label='프로필 사진')
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'birthday', 'image')
     
     
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='',
        widget=forms.TextInput(
            attrs={
                    'class': 'form-control',
                    'autofocus': True,
                    'placeholder':"username",
                }
            )
        )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                    'autocomplete': 'current-password',
                    'placeholder': "foo@example.com",
                }
            ),
    )
