from django import forms


class MyForm(forms.Form):
    data = forms.CharField(max_length=255, label='Data')
    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = int(kwargs.pop('extra', 0))
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields
        for index in range(extra_fields):
            self.fields['data{index}'.format(index=index + 1)] = forms.CharField()

    def clean(self):
        self.cleaned_data.pop('extra_field_count')
        return self.cleaned_data
