from django import forms


class ChatForm(forms.Form):
    chat_message = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Ask me ...'}))
