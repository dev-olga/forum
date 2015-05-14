$(function() {

    $("#login").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        initModalDialog(this, $("#login-form-container"), "#submit-login");
    });

    $("#registration").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        initModalDialog(this, $("#registration-form-container"), "#submit-registration");
    });

    var initModalDialog = function(sender, container, submitSelector){
        container.find(".modal-body").load($(sender).attr("href"), function(data){
            container.find(submitSelector).on('click', function(e){
                e.preventDefault();
                e.stopPropagation();
                submit(container.find("form"));
            });

            container.modal();
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
                if(!data.is_valid){
                    self.replaceWith(data.response);
                }
                else{
                    window.location.replace(window.location.href);
                }
            }
        });
    };
});