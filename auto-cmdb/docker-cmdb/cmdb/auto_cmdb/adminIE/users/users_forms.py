import re 
from django import forms


from django import forms

from users.models import UsersProfile

class UserRegisterFormView(forms.ModelForm):
    class Meta:
        model = UsersProfile
        fields = ['username', 'password', 'mobile',"email"]

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        PRGEX_MOBILE = r'^1[358]\d{9}|^147\d{8}|^176\d{8}$'
        regex = re.compile(PRGEX_MOBILE)
        if regex.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(
                '无效的手机号！',
                code='mobile_invalid'
            )