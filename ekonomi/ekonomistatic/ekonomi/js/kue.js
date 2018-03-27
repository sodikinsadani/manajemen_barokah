function setForm(data){
  $("#id_nama_kue").val(data[2]);
  $("#id_harga").val(data[3])
  $("#id_jenis_kue option").filter(function() {
    return $(this).text().toUpperCase() == data[4].toUpperCase()
  }).prop('selected', true);
  $("#id_target").val(data[5]);
  $("#id_stok").val(data[6])
  $("#id_terjual").val(data[7]);
  $("#id_sisa").val(data[8])
  $("#id_keterangan").val(data[9])
}

function showForm (actionselect, data) {
  //reset form
  $('form')[1].reset();
  if (actionselect == 0) {
    $('#modal-default').find('.modal-title').text('Tambah Setoran Kue')
    $("form .box-body :input").prop("disabled", false);
    $('#btnsave').text('Save')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/ekonomi/kue/');
  } else if (actionselect == 1) {
    $('#modal-default').find('.modal-title').text('Edit Setoran Kue')
    $("form .box-body :input").prop("disabled", false)
    setForm(data)
    $('#btnsave').text('Update')
    $('#btnsave').show()
    $('#btnreset').show()
    $("form").attr('action', '/ekonomi/kue/'+data[1]+'/edit/');
  } else if (actionselect == 2) {
    $('#modal-default').find('.modal-title').text('Hapus Setoran Kue')
    $("form .box-body :input").prop("disabled", true)
    setForm(data)
    $('#btnsave').text('Delete')
    $('#btnsave').show()
    $('#btnreset').hide()
    $("form").attr('action', '/ekonomi/kue/'+data[1]+'/delete/');
  } else if (actionselect == 4) {
    $('#modal-default').find('.modal-title').text('Data Setoran Kue')
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
  "scrollX": true,
  });

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
