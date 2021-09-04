from django import forms
from .models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ('id', )

    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['date_start'].widget.attrs['readonly'] = True

    def clean_date_start(self):
        if self.instance:
            return self.instance.date_start
        else:
            return self.fields['date_start']

    def clean(self):
        if self.cleaned_data['date_start'] >= self.cleaned_data['date_end']:
            self.add_error('date_end', 'Poll end date must be after start date')
        return self.cleaned_data