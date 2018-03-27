from django import forms
from ekonomi.models import Kue

class fKue(forms.ModelForm):
    class Meta:
        model = Kue
        fields = '__all__'
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fKue, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            #get current classes from Meta
            classes = self.fields[field].widget.attrs.get("class")
            if classes is not None:
                classes = classes
            else:
                classes = "form-control"
            self.fields[field].widget.attrs.update({
                'class': classes
            })

        dict_ph = {'nama_kue':'nama kue','jenis_kue':'jenis kue'}

        for field in iter(self.fields):
            #get current classes from Meta
            placeholder = self.fields[field].widget.attrs.get("placeholder")
            if placeholder is not None:
                placeholder = placeholder
            elif field in dict_ph:
                placeholder = dict_ph[field]
            else:
                placeholder = field
            self.fields[field].widget.attrs.update({
                'placeholder': placeholder
            })

        self.fields['jenis_kue'].choices  = [("", "-- jenis kue --"),] + list(self.fields["jenis_kue"].choices)[1:]
