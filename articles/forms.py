from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # declare fields for model
    class Meta:
        model = Article
        fields = ["title", "content"]

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        # do query set lookup for duplicate titles
        qs = Article.objects.all().filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" already exists! Pick different title.")
        return data

