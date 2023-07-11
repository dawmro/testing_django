from django import forms

from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    error_class_css = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(help_text="This is help text! <a href='contact/'>Contact us!</a>")
    #description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    class Meta:
        model = Recipe
        fields = ["name", "description", "directions"]

    def __init__(self, *args, **kwargs):
        # call initial init method
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f"Recipe {str(field)}",
                "class": "form-control",
                "hx-post": ".",
                "hx-trigger": "keyup changed delay:500ms",
                "hx-target": "#recipe-container",
                "hx-swap": "inerHTML"
            }
            self.fields[str(field)].widget.attrs.update(new_data)
        self.fields["description"].widget.attrs.update({"rows": "2"})
        self.fields["directions"].widget.attrs.update({"rows": "4"})


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["name", "quantity", "unit"]