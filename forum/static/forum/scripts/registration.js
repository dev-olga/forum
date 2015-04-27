//$(function() {
//    var registrationDialog;
//    $("#registration").click(function(e){
//        e.preventDefault();
//        e.stopPropagation();
//        if (!registrationDialog){
//            $("#registration-form").load($(this).attr("href"), function(data){
//            data = $(data);
//            var form = data.find("form").andSelf();
//            loginDialog = data
//                .dialog({
//                    autoOpen: true,
//                    height: "auto",
//                    width: "auto",
//                    modal: true,
//                    title: "Login"
//            });
//            });
//
//        }
//        else{
//            registrationDialog.dialog("open");
//        }
//        return false;
//    });
//});