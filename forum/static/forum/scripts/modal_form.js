modalForm = function(){

    this.init = function(sender, container){
        container.find(".modal-body").load($(sender).attr("href"), function(data){
            container.find('[type=submit]').on('click', function(e){
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
                else if (data.success_url){
                    window.location.replace(data.success_url);
                }
                else{
                    window.location.reload();
                }
            }
        });
    }
}

modalMultipartForm = function(){

    this.init = function(sender, container){
        container.find(".modal-body").load($(sender).attr("href"), function(data){
            container.find('[type=submit]').on('click', function(e){
                e.preventDefault();
                e.stopPropagation();
                submit(container.find("form"));
            });

            container.modal();
        });
    }

    var submit = function(form) {
        var self = form;
        var formData = new FormData(form[0]);
        $.ajax({
            type: self.attr("method"),
            url: self.attr("action"),
            // Form data
            data: formData,
            //Options to tell jQuery not to process data or worry about content-type.
            cache: false,
            contentType: false,
            processData: false,
            success: function(data)
            {
                if(!data.is_valid){
                    self.replaceWith(data.response);
                }
                else if (data.success_url){
                    window.location.replace(data.success_url);
                }
                else{
                    window.location.reload();
                }
            }
        });
    }
}
