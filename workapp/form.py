from django import forms
from django.core.exceptions import ValidationError

def name_validator(name):
    if len(name) > 8:
        raise ValidationError("请输入8个字符以内的用户名")

def phone_validator(phone):
    if phone < 10000000000:
        raise ValidationError("请输入11位手机号")

def yhm_validator(name):
    if len(name) > 14:
        raise ValidationError("请输入14个字符以内的用户名")

def mima_validator(mima):
    if len(mima) < 7 :
        raise ValidationError("请输入6个字符以上的密码")

class AppointForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': '姓名'}
        ),
        validators=[name_validator]

    )
    phone = forms.IntegerField(
        max_value=19999999999,
        widget=forms.TextInput(
            attrs={'placeholder': '手机'}
        ),
        validators=[phone_validator]
    )

class RegForm(forms.Form):
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={'placeholder': '邮箱'}
        )
    )
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': '姓名'}
        ),
        validators=[yhm_validator]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': '密码'}
        ),
        validators=[mima_validator]
    )

class LogForm(forms.Form):
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={'placeholder': '邮箱'}
        )
    )
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={'placeholder': '密码'}
        ),
        validators=[mima_validator]
    )

class ModifyForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label='修改用户名',
        required=False,
        validators=[yhm_validator]
    )
    password = forms.CharField(
        label='修改密码',
        required=False,
        widget=forms.PasswordInput(),
        validators=[mima_validator]
    )