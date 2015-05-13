$(function() {

    $("#login").on('click', function(e){
        var containerId = "login-form-container";
        e.preventDefault();
        e.stopPropagation();
        initModalDialog(this, $("#login-form-container"),  "#submit-login");
    });

    $("#registration").on('click', function(e){
        var containerId = "registration-form-container";
        e.preventDefault();
        e.stopPropagation();
        initModalDialog(this, $("#registration-form-container"),  "#submit-registration");
    });

    var initModalDialog = function(sender, containerSelector, submitSelector){
        containerSelector.find(".modal-body").load($(sender).attr("href"), function(data){
            containerSelector.find(submitSelector).on('click', function(e){
                e.preventDefault();
                e.stopPropagation();
                submit(containerSelector.find("form"));
            });

            containerSelector.modal();
        });
    }

    var submit = function(form) {
        var self = form;
        $.ajax({
            type: self.attr("method"),
            url: self.attr("action"),
            data: self.serialize(),
            dataType: "json",
            traditional: true,
            success: function(data)
            {
                if(data.invalid){
                    self.replaceWith(data.invalid);
                }
                else{
                    window.location.replace(window.location.href);
                }
            }
        });
    };
});