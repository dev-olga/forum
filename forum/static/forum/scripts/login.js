//$(function() {
//    var loginDialog;
//    $("#login").click(function(e){
//        e.preventDefault();
//        e.stopPropagation();
//        if (!loginDialog){
//            $("#login-form").load($(this).attr("href"), function(data){
//            data = $(data);
//            var form = data.find("form").andSelf();
//            loginDialog = data
//                .dialog({
//                    autoOpen: true,
//                    height: "auto",
//                    width: "auto",
//                    modal: true,
////                    buttons: {
////                        Login: function() {
////                             $.ajax({
////                               type: form.attr("method"),
////                               url: form.attr("action"),
////                               data: $(form).serialize(),
////                               success: function(data)
////                               {
////                                   alert(data);
////                               },
////                               error: function(data)
////                               {
////                                   alert(data);
////                               }
////                             });
////                        },
////                        Cancel: function() {
////                          loginDialog.dialog( "close" );
////                        }
////                    },
//                    title: "Login"
//            });
//            });
//
//        }
//        else{
//            loginDialog.dialog("open");
//        }
//        return false;
//    });
//});

$(function() {
    var loginDialog;
    $("#login").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        $("#login-form .modal-body").load($(this).attr("href"), function(data){
            $("#login #submit-login").click(function(e){
                 $.ajax({
                   type: form.attr("method"),
                   url: form.attr("action"),
                   data: $(form).serialize(),
                   success: function(data)
                   {
                       alert(data);
                   },
                   error: function(data)
                   {
                       alert(data);
                   }
                 });
            });

            $("#login-form").modal();
        });
        return false;
    });
});