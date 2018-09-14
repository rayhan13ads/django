$(function(){
    $('#upload-sucess').hide();
    $('#btnDrop').click(function () { 
        $('#upload-sucess').show();
        $('#name,#filepath,#btnDrop,#small').hide();
        
    });
});