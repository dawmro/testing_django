from django.shortcuts import render

# Create your views here.
def meal_queue_toggle_view(request, recipe_id=None):
    context = {
        'recipe_id': recipe_id
    }
    return render(request, 'meals/partials/queue-toggle.html', context)
