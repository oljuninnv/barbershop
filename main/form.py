from django import forms
from .models import Visiting

class VisitingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        worker = kwargs.pop('worker', None)
        super(VisitingForm, self).__init__(*args, **kwargs)
        
        # Фильтрация дат и времени на основе имеющихся записей
        if worker:
            self.fields['date'].queryset = Visiting.objects.filter(worker=worker).values_list('date', flat=True).distinct()
            self.fields['time'].queryset = Visiting.objects.filter(worker=worker, customer_name=None, customer_phone=None).values_list('time', flat=True)

    class Meta:
        model = Visiting
        fields = ['worker', 'service', 'customer_name', 'customer_phone', 'date', 'time']

        widgets = {
            'service': forms.CheckboxSelectMultiple(),
            'date': forms.SelectDateWidget(),
            'time': forms.Select(),
        }