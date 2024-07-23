from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    question = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2}),
        label="Question",
    )
    
    answer = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2}),
        label="Answer",
    )

    class Meta:
        model = Question
        fields = "__all__"
