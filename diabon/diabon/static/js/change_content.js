$(document).ready(function(){
	$("nav#releves-tri a.change_load").click(function(){
		//on recup l'url de la page dans une variable 'page'
		page = $(this).attr("href");
		$.ajax({
			url: page,
			cache:false,
			success:function(html){
				afficher_releves(html);
			},
			error:function(XMLHttpRequest,textStatus,errorThrown){
				alert(textStatus);
			}
		})
		//on change sa classe pour qu'il soit actif
		$(".change_load").removeClass('actif');
		$(this).addClass('actif');
		
		return false;
	});
}); 

function afficher_releves(data){
	$("#table-releve-container").fadeOut(300,function(){
		$("#table-releve-container").empty();
		$("#table-releve-container").append(data);
		$("#table-releve-container").fadeIn(500);
	})
}