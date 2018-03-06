

//function searchSuccess(data, textStatus, jqXHR) {
	//$('#stopResults').html(data)
//};
//function searchSuccess(data, textStatus, jqXHR) {
	//$('#stopResults').html(data)
//};

$(function(){
	$('#id_stop_choice').keyup(function() {
	
	$('#id_stop_choice').autocomplete({
		
		source: function(request, response){
			
			$.ajax({
				
			url: '/SearchStop/',
			type: "POST",
			dataType: "json",
			data:{
				SearchTrain : $('#id_train_choice').val(),
				SearchStop : $('#id_stop_choice').val(),
				csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken]").val(),
			},
			success: function(data){
				response(data)
			
			}});
	}});
	});
});
	
			
		

			

			
	