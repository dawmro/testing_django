from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data # dict
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "the office":
            self.add_error("title", "This title is taken")
        if "office" in content or "office" in title.lower():
            self.add_error("content", "This content is taken")
            raise forms.ValidationError("Office is not allowed")
        return cleaned_data

    # validation method