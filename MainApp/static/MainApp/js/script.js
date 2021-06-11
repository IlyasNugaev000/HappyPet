$(document).ready(function(){
    $('.slider').slick({
        accessibility: false,
        dots: true,
        arrows: true,
        draggable: false,
        slidesToShow: 2,
        slidesToScroll: 2,
    });
	
	
	$(document).on('mouseup', 'input', function() {
		let cookie = document.cookie
		let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
		console.log($("." + $(this).attr('class')).first().val())
	  $.ajax({
	    type: "POST",
	    url: "addCount/",
		headers: {
			'X-CSRFToken': csrfToken
		},
	    data: {
		  'count': $(this).val(),
		  'id': $(this).attr('id')
	    },
		success: function(data){
			console.log("aaaa")
		}
	  });
    });
});