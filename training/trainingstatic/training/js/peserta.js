function setForm(data, id_peserta){
  $("#id_id_peserta").val(data[1]).trigger("change");
  $("#id_jenjang option").filter(function() {
      return $(this).text().toUpperCase() == data[4].toUpperCase();
  }).prop('selected', true);
}

function showForm (actionselect, data, id_peserta) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Peserta')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/training/peserta/');
    $("#id_id_peserta").parent().show();
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Peserta ('+data[2]+')')
    $("form .box-body :input").prop("disabled", false)
    setForm(data, id_peserta)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/training/peserta/'+data[1]+'/edit/');
    $("#id_id_peserta").parent().hide();
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Peserta ('+data[2]+')')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    //$("form").attr('action', '/personalia/peserta/'+data[1]+'/delete/');
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Peserta ('+data[2]+')')
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
      {"targets":[1,],
    "visible":false}
  ],
  select: true,
  //"scrollX": true,
  });

  //Initialize Select2 Elements
  var id_peserta = $('#id_id_peserta').select2({
    placeholder: 'pilih peserta'
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
              showForm(actionselect, data, id_peserta)
          }
          e.preventDefault();
      });
  });

})
