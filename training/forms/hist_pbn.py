from django import forms
from training.models import Histpbn, Peserta

class fHistpbn(forms.ModelForm):
    class Meta:
        model = Histpbn
        fields = '__all__'
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fHistpbn, self).__init__(*args, **kwargs)
        self.fields['peserta'].widget.attrs['class'] = 'form-control select2'
        self.fields['peserta'].widget.attrs['style'] = 'width: 100%;'
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

        dict_ph = {'tgl_training':'tanggal training'}

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
        self.fields['materi'].choices  = [("", "-- materi --"),] + list(self.fields["materi"].choices)[1:]
        self.fields['trainer'].choices  = [("", "-- trainer --"),] + list(self.fields["trainer"].choices)[1:]
