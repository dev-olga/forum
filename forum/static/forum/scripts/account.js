$(function() {

    $("#login").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#login-form-container"), "#submit-login");
    });

    $("#registration").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#registration-form-container"), "#submit-registration");
    });

});