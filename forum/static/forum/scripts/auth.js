$(function() {
    var auth

    $("#login").on('click', function(e){
        var containerId = "login_form_container";
        e.preventDefault();
        e.stopPropagation();
        $("#" + containerId + " .modal-body").load($(this).attr("href"), function(data){

            var form = $("#login_form");
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
                        window.location.replace(window.location.href);
                    },
                     error:function(data)
                    {
                        alert(data);
                    }
                });
            });

            $("#" + containerId).modal();
        });

    });
});