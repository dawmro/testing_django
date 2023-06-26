from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data # dict
        title = cleaned_data.get("title")
        if title.lower().strip() == "the office":
            raise forms.ValidationError("Ths title is taken")
        return title

    # validation method