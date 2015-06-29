$(function() {

    $("[data-action='post-update']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#update-post-form-container"));
    });

    $("[data-action='delete']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#delete-form-container"));
    });

    $("[data-action='thread-update']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalMultipartForm()).init(this, $("#update-thread-form-container"));
    });
});