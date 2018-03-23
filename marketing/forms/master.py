from django import forms
from marketing.models import Konsumen


class fKonsumen(forms.ModelForm):
    class Meta:
        model = Konsumen
        exclude = ['individu',]
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fKonsumen, self).__init__(*args, **kwargs)
        self.fields['warga_media'].widget.attrs['class'] = 'flat-red'
        self.fields['sales'].widget.attrs['class'] = 'form-control select2'
        self.fields['sales'].widget.attrs['style'] = 'width: 100%;'
        # add common css classes to all widgets
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

        dict_ph = {'tgl_finish':'Tanggal Finish',}

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

        self.fields['status'].choices  = [("", "-- status --"),] + list(self.fields["status"].choices)[1:]
        self.fields['status_aktif'].choices  = [("", "-- status aktif --"),] + list(self.fields["status_aktif"].choices)[1:]
        self.fields['segmentasi'].choices  = [("", "-- segmentasi --"),] + list(self.fields["segmentasi"].choices)[1:]
