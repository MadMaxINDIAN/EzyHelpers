from django.forms import ModelForm
from .models import BlogPost

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'