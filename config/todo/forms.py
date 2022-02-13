from xml.dom import ValidationErr
from django import forms
from .models import Todo, TodoCategory, TodoStatus
from django.core.exceptions import ValidationError
# import bootstrap_datepicker_plus as datetimepicker



class DateInput(forms.DateInput):
    input_type = 'date'



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
        widgets = {
            'deadline' : forms.NumberInput(attrs={
                "type":"date"})
        }
    
    """
    ※DateInputクラスを使う場合はこちら
        widgets = {
            'deadline': DateInput()
        }
    """
    """
    ※リスト形式で選ぶ場合はこちら
        widgets = {
            'deadline': forms.SelectDateWidget
        }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        
        
    
class AnalysisPeriodForm(forms.Form):
    start_day = forms.DateField(label="開始日", widget=DateInput())
    end_day = forms.DateField(label="終了日", widget=DateInput())

    def clean(self):
        period = super().clean()
        start_day = period["start_day"]
        end_day = period["end_day"]
        if start_day > end_day:
            raise ValidationError("開始日と終了日が前後しています。")
        return period
