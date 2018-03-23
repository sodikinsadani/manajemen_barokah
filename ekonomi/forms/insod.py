from django import forms
from ekonomi.models import Insod

class fInsod(forms.ModelForm):
    class Meta:
        model = Insod
        fields = '__all__'
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fInsod, self).__init__(*args, **kwargs)
        self.fields['member'].widget.attrs['class'] = 'form-control select2'
        self.fields['member'].widget.attrs['style'] = 'width: 100%;'
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

        dict_ph = {'tgl_setor':'tanggal setor','jenis_insod':'jenis insod'}

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

        self.fields['jenis_insod'].choices  = [("", "-- jenis insod --"),] + list(self.fields["jenis_insod"].choices)[1:]
