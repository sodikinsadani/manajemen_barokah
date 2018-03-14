from django import forms
from training.models import Peserta

class fPeserta(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = '__all__'
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super(fPeserta, self).__init__(*args, **kwargs)
        self.fields['id_peserta'].widget.attrs['class'] = 'form-control select2'
        self.fields['id_peserta'].widget.attrs['style'] = 'width: 100%;'
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

        dict_ph = {'jenjang':'jenjang'}

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
