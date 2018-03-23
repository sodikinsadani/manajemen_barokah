function setForm(data){
$("#id_nama").val(data[2])
$("#id_tmpt_lahir").val(data[3])
$("#id_tgl_lahir").val(data[4])
$("#id_jk option").filter(function() {
    return $(this).text().toUpperCase() == data[5].toUpperCase();
}).prop('selected', true);
$("#id_alamat").val(data[6])
$("#id_alamat_desa").val(data[7])
$("#id_alamat_kec").val(data[8])
$("#id_alamat_kabkot").val(data[9])
$("#id_alamat_prov").val(data[10])
$("#id_lulusan option").filter(function() {
    return $(this).text().toUpperCase() == data[11].toUpperCase();
}).prop('selected', true);
$("#id_lulusan option").filter(function() {
    return $(this).text().toUpperCase() == data[11].toUpperCase();
}).prop('selected', true);
$("#id_hp").val(data[12])

$("#id_status option").filter(function() {
    return $(this).text().toUpperCase() == data[13].toUpperCase();
}).prop('selected', true);
$("#id_tgl_finish").val(data[14])
$("#id_status_aktif option").filter(function() {
    return $(this).text().toUpperCase() == data[15].toUpperCase();
}).prop('selected', true);
$("#id_segmentasi option").filter(function() {
    return $(this).text().toUpperCase() == data[16].toUpperCase();
}).prop('selected', true);
$("#id_sales").val(data[17]).trigger("change");
if (data[18] == 'True') {
  $("#id_warga_media").prop("checked", true);
} else {
  $("#id_warga_media").prop("checked", false);
}
$('input[type="checkbox"].flat-red, input[type="radio"].flat-red').iCheck({
  checkboxClass: 'icheckbox_flat-green',
  radioClass   : 'iradio_flat-green'
})

$("#id_keterangan").val(data[19])
}

function showForm (actionselect, data) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Konsumen')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/marketing/konsumen/');
    $('#id_tgl_finish').hide()
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Konsumen')
    $("form .box-body :input").prop("disabled", false)
    setForm(data)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/marketing/konsumen/'+data[1]+'/edit/');
    $('#id_tgl_finish').show()
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Konsumen')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    $("form").attr('action', '/marketing/konsumen/'+data[1]+'/delete/');
    $('#id_tgl_finish').show()
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Konsumen')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').hide()
    $('#btnreset').hide()
    $('#id_tgl_finish').show()
  }

  $('#modal-default').modal('toggle');
}

$(function(){
  var table = $('#example1').DataTable({
    "columnDefs":[
      {"targets":[1,3,4,6,7,8,9,10,11,12,14,16,18,19],
    "visible":false}
  ],
  select: true,
  //"scrollX": true,
  });

  $('#example1 tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
  });

  //Date picker
  $('#id_tgl_lahir').datepicker({
    autoclose: true
  })

  $('#id_tgl_finish').datepicker({
    autoclose: true
  })

  //Initialize Select2 Elements
  $('#id_sales').select2({
    placeholder: 'pilih sales'
  })

  //Flat red color scheme for iCheck
  $('input[type="checkbox"].flat-red, input[type="radio"].flat-red').iCheck({
    checkboxClass: 'icheckbox_flat-green',
    radioClass   : 'iradio_flat-green'
  })

  var actionselect = 0;

    $("#actionmenu li a").each(function(){
        $(this).click(function(e){
            actionselect = $(this).parent().index();

            var jumlah = table.rows( { selected: true } ).count()
            var data = table.rows('.selected').data()[0];

            if (actionselect != 0 && jumlah != 1) {
                alert("you must select only one row")
            } else {
                showForm(actionselect, data)
            }
            e.preventDefault();
        });
    });

})
