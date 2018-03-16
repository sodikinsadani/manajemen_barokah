function setForm(data){
  $("#id_peserta").val(data[2]).trigger("change");
  $("#id_materi option").filter(function() {
      return $(this).text().toUpperCase() == data[7].toUpperCase();
  }).prop('selected', true);
  $("#id_tgl_training").val(data[3])
  $("#id_keterangan").val(data[8])
  $("#id_trainer option").filter(function() {
      return $(this).text().toUpperCase() == data[9].toUpperCase();
  }).prop('selected', true);
}

function showForm (actionselect, data) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Histori Training')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/training/hist_pbn/');
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Histori Training')
    $("form .box-body :input").prop("disabled", false)
    setForm(data)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/training/hist_pbn/'+data[1]+'/edit/');
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Histori Training')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    $("form").attr('action', '/training/hist_pbn/'+data[1]+'/delete/');
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Histori Training')
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
      {"targets":[1,2,8,9],
    "visible":false}
  ],
  select: true,
  //"scrollX": true,
  });

  //Initialize Select2 Elements
  $('#id_peserta').select2({
    placeholder: 'pilih peserta'
  })

  //Date picker
  $('#id_tgl_training').datepicker({
    autoclose: true
  })

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
