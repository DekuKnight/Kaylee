var iconTable = {
    'info':'fa-info-circle',
    'warn':'fa-exclamation-triangle',
    'error':'fa-minus-circle',
    'plane':'fa-plane'
};

jQuery.fn.updateWithText = function(text, speed)
{
	var dummy = $('<div/>').html(text);

	if ($(this).html() != dummy.html())
	{
		$(this).fadeOut(speed/2, function() {
			$(this).html(text);
			$(this).fadeIn(speed/2, function() {
			});
		});
	}
}

jQuery.fn.flashMessage = function(text, speed, duration)
{
	$(this).fadeOut(speed/2, function() {
		$(this).html(text);
		$(this).fadeIn(speed/2, function() {
			$(this).delay(duration).fadeOut(speed/2, function(){
			});
		});
	});
}

jQuery.fn.outerHTML = function(s) {
    return s
        ? this.before(s).remove()
        : jQuery("<p>").append(this.eq(0).clone()).html();
};

addNotification = function(i, message, speed){  
    if($('#notifications').children().length == 0){
        $('.notification').fadeIn(speed/2,function(){
        });
    }
    var opacity =1;
    $('#notifications').children().each(function(index){
        opacity -= 0.155;
        $(this).fadeTo(speed/2, opacity);
        if(index>3){
            $(this).fadeOut(speed/2, function(){
                $(this).hide();
            });
        }
    });
    
    
    var icon = $('<span/>').addClass('fa').addClass(i);
    var notification = $('<div/>').html(icon.outerHTML() +' '+message).fadeTo(0,0);
    $('#notifications').prepend(notification.outerHTML());
    $($('#notifications').children()[0]).fadeTo(speed/2,1);
    
}

removeNotification = function(message, speed){
    var removed = false;
    var opacity;
    $('#notifications').children().each(function(index){
        if($(this).text().trim() == message.trim() && !removed){
            removed = true;
            opacity = $(this).css("opacity");
            $(this).fadeOut(speed/2, function(){
                $(this).remove();
            })
            
        }
        else if(removed){
            $(this).fadeTo(speed/2, opacity);
            opacity -= 0.155;
            if(index=3){
                $(this).fadeIn(speed/2, function(){
                    $(this).show();
                });
            }
        }
    });

    if($('#notifications').children().length == 1 && removed){
        $('.notification').fadeOut(speed/2, function(){
        });
    }
}

jQuery(document).ready(function($) {
	
	var eventList = [];
	var news = [];
	var newsIndex = 0;
	
	moment.lang(config.lang);
	
	weather.init();
	
	time.init();

});