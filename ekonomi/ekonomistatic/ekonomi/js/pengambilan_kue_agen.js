function setForm(data){
  $("#id_kue").val(data[2]).trigger("change");
  $("#id_kurir").val(data[4]);
  $("#id_jumlah").val(data[5])
  $("#id_jenis_transaksi option").filter(function() {
    return $(this).text().toUpperCase() == data[6].toUpperCase()
  }).prop('selected', true);
  $("#id_tgl_ambil").val(data[7]);
  $("#id_keterangan").val(data[8])
}

function showForm (actionselect, data) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('New Transaksi Pengambilan')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/ekonomi/pengambilankueagen/');
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Transaksi Pengambilan')
    $("form .box-body :input").prop("disabled", false)
    setForm(data)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/ekonomi/pengambilankueagen/'+data[1]+'/edit/');
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Transaksi Pengambilan')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    $("form").attr('action', '/ekonomi/pengambilankueagen/'+data[1]+'/delete/');
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Transaksi')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').hide()
    $('#btnreset').hide()
  }

  $('#modal-default').modal('toggle');
}

$(function(){
  var table = $('#example1').DataTable({
    "columnDefs":[
      {"targets":[1,2],
    "visible":false}
  ],
  select: true,
  "scrollX": true,
  });

  //Initialize Select2 Elements
  $('#id_kue').select2({
    placeholder: 'pilih kue'
  })

  $('#id_sales').select2({
    placeholder: 'pilih sales'
  })

  //Date picker
  $('#id_tgl_ambil').datepicker({
    autoclose: true
  })

  /*$('#id_tgl_penjualan').datepicker({
    autoclose: true
  })*/

  //Flat red color scheme for iCheck
  /*$('input[type="checkbox"].flat-red, input[type="radio"].flat-red').iCheck({
    checkboxClass: 'icheckbox_flat-green',
    radioClass   : 'iradio_flat-green'
  })*/

  $('#example1 tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
  });
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
