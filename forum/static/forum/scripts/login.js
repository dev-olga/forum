$(function() {


    $("#login").on('click', function(e){
        var containerId = "login_form_container";
        e.preventDefault();
        e.stopPropagation();
        $("#" + containerId + " .modal-body").load($(this).attr("href"), function(data){

            var form = $("#login_form");//$("#login-form .modal-body").find("form").andSelf();
            $("#" + containerId + " #submit_login").on('click', function(e){
                e.preventDefault();
                e.stopPropagation();
                form.submit();
            });

            form.on("submit", function(e) {
                e.preventDefault();
                e.stopPropagation();
                $.ajax({
                    type: form.attr("method"),
                    url: form.attr("action"),
                    data: $(this).serialize(),
                    dataType: "json",
                    traditional: true,
                    success: function(data)
                    {
                        if(data.errors){
                            form.find(".validation-errors").html(data.errors);
                        }
                        else if(data.redirect_to){
                            window.location.replace(data.redirect_to);
                        }
                    }
                });
            });

            $("#" + containerId).modal();
        });

    });
});