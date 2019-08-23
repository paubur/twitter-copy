from django.forms import ModelForm
from twitter.models import Message


class MessageForm(ModelForm):
    class Meta:
        fields = ("message", "sender", "receiver")
        model = Message
