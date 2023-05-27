from django.shortcuts import render
from .forms import StoryForm
from .tasks import generate_and_send_story


def home(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal']
            habit = form.cleaned_data['habit']
            email = form.cleaned_data['email']

            # Call the actor
            generate_and_send_story.send(goal, habit, email)
    else:
        form = StoryForm()
    return render(request, 'motivation/home.html', {'form': form})
