
from django import forms
from .models import Post, Comment, Tag
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]
        
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")
    
    class Meta:
        model = Post
        fields = ['title', 'content']
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        tags_input = self.cleaned_data.get('tags')
        if tags_input:
            tag_names = [tag.strip() for tag in tags_input.split(',')]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                instance.tags.add(tag)

        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']