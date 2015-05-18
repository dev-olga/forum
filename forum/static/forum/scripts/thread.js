(function(newPostsListener) {

    var listener = undefined;

    var checkNewPosts = function(url){
        $.ajax({
            url: url,
            dataType: "json",
            traditional: true,
            success: function(data)
            {
                if(data.new_posts){
                    clearInterval(listener);
                    $("#new-posts-notification").show();
                }
            }
        });
    }

    newPostsListener.start = function(url){
        if (!listener){
            listener = setInterval(function() {checkNewPosts(url);}, 10000)
        }
    }
})(window.newPostsListener = window.newPostsListener || {});

