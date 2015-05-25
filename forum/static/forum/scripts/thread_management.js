$(function() {

    $("[data-action='post-update']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#update-form-container"));
    });

    $("[data-action='delete']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalForm()).init(this, $("#delete-form-container"));
    });

    $("[data-action='thread-update']").on('click', function(e){
        e.preventDefault();
        e.stopPropagation();
        (new modalMultipartForm()).init(this, $("#update-form-container"));
    });

//    $("[data-action='thread-update']").on('click', function(e){
//        e.preventDefault();
//        e.stopPropagation();
//        var container =$(this).closest(".thread-update-form-container");
//        container.find(".content").load($(this).attr("href"), function(data){   container.show();     });
//    });

});