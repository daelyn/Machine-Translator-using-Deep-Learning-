$('#translate').click(function() {

    var text = $('#english-text').val()

    $.ajax({
        url: "/",
        type: "POST",
        data: JSON.stringify({data: text}),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        cache: false,
        success: function(data){
            $("#hindi-text").val(data.translation);
        }
      });


});