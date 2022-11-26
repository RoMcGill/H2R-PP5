from django import forms
from .models import Subscribers, SendNews


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class SendNewsForm(forms.ModelForm):
    class Meta:
        model = SendNews
        fields = '__all__'
