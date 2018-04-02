from django import forms
from ekonomi.models import Penjualan

class fPenjualanKue(forms.ModelForm):
    class Meta:
        model = Penjualan
        fields = '__all__'
        widgets = {
            'keterangan':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fPenjualanKue, self).__init__(*args, **kwargs)
        self.fields['kue'].widget.attrs['class'] = 'form-control select2'
        self.fields['kue'].widget.attrs['style'] = 'width: 100%;'
        self.fields['sales'].widget.attrs['class'] = 'form-control select2'
        self.fields['sales'].widget.attrs['style'] = 'width: 100%;'
        self.fields['is_terkirim'].widget.attrs['class'] = 'flat-red'
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

        dict_ph = {'nama_konsumen':'nama konsumen','tgl_kirim':'tgl kirim','tgl_penjualan':'tgl transaksi'}

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

        self.fields['jenis_transaksi'].choices  = [("", "-- jenis transaksi --"),] + list(self.fields["jenis_transaksi"].choices)[1:]
