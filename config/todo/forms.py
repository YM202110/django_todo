from django import forms
from .models import Todo, TodoCategory, TodoStatus

class TodoForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        label="業務種別",
        queryset=TodoCategory.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,)
    
    status = forms.ModelChoiceField(
        label="処理状況",
        queryset=TodoStatus.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,)
    
    class Meta:
        model = Todo
        fields = '__all__'
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
    

