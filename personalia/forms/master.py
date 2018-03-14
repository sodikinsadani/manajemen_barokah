from django import forms
from personalia.models import Individu,Member

class fIndividu(forms.ModelForm):
    class Meta:
        model = Individu
        fields = '__all__'
        widgets = {
            'alamat':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fIndividu, self).__init__(*args, **kwargs)
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

        dict_ph = {'tgl_lahir':'tanggal lahir','alamat_desa':'desa','alamat_kec':'kecamatan','alamat_kabkot':'kota/kabupaten',
            'alamat_prov':'provinsi','hp':'nomor handphone','tmpt_lahir':'tempat lahir'
        }

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

        self.fields['jk'].choices  = [("", "-- jenis kelamin --"),] + list(self.fields["jk"].choices)[1:]
        self.fields['lulusan'].choices  = [("", "-- lulusan --"),] + list(self.fields["lulusan"].choices)[1:]

class fMember(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['individu','tgl_input',]
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fMember, self).__init__(*args, **kwargs)
        self.fields['warga_media'].widget.attrs['class'] = 'flat-red'
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

        dict_ph = {'tgl_daftar':'Tanggal Daftar',}

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

        self.fields['jenjang'].choices  = [("", "-- jenjang --"),] + list(self.fields["jenjang"].choices)[1:]
        self.fields['status_aktif'].choices  = [("", "-- status aktif --"),] + list(self.fields["status_aktif"].choices)[1:]
        self.fields['segmentasi'].choices  = [("", "-- segmentasi --"),] + list(self.fields["segmentasi"].choices)[1:]
        self.fields['pangkal'].empty_label = "-- pangkal --"
        self.fields['pangkal'].widget.choices = self.fields['pangkal'].choices
