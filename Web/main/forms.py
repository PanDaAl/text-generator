from .models import Feedback
from django.forms import ModelForm, Textarea


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'text']

        widgets = {
            "name": Textarea(attrs={
                'id': 'text_name',
                'type': 'text',
                'placeholder': 'Введите ваше имя',
                'maxlenght': '20'
            }),
            "email": Textarea(attrs={
                'id': 'text_email',
                'type': 'text',
                'placeholder': 'Введите ваш Email-адрес',
                'maxlenght': '30'
            }),
            "text": Textarea(attrs={
                'id': 'text_main',
                'type': 'text',
                'placeholder': 'Введите ваше сообщение',
                'maxlenght': '250'
            })
        }
