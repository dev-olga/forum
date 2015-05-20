$(function() {

    $("[data-action='post-update']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#post-update-form-container"));
    });

    $("[data-action='thread-update']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#thread-update--form-container"));
    });

});