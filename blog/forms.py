from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class post_create_form(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.Field()

    class Meta:
        model = Post
        fields = ["title", "content"]


class post_update_form(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()

    class Meta:
        model = Post
        fields = ["title", "content"]


class post_comment_form(forms.Form):
    comment = forms.CharField()

    class Meta:
        model = Comment
        feilds = ["comment"]
