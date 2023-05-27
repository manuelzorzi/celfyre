from django import forms

class StoryForm(forms.Form):
    goal = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
        label="goal"
    )
    habit = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
        label="habit"
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
        label="email"
    )

