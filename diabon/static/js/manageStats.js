window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer",
	{
		theme: "theme1",
		exportEnabled: true,
		animationEnabled: true,
		title: {
			text: "Mes relevés du jour"               
		},
		legend: {
			fontFamily: "kenyan_coffeeregular",
			fontStyle: "normal",
		},
			axisX: {
			valueFormatString: "HH:mm",
			interval:1,
			labelFontFamily: "tall_filmsregular",
			labelFontWeight: "bold",
			labelFontSize: 25,
		},
		axisY:{
			includeZero: false,
			labelFontFamily: "tall_filmsregular",
			labelFontWeight: "bold",
			labelFontSize: 20,
		},
		data: [{        
			type: "line",
			color: "#5c89c7",
			//lineThickness: 3,        
			dataPoints: [
				{ x:  new Date(2015, 06, 15, 08, 30), y: 130 },
				{ x:  new Date(2015, 06, 15, 12, 45), y: 135},
				{ x:  new Date(2015, 06, 15, 19, 20), y: 133},        
			]
	  	}]
	});

	chart.render();
}

/* STATS : CHANGE CURRENT + UPDATE */
$("nav#stats-tri li").click(function(){
	//on supprime la classe current actuel
	$(".current").removeClass('current');
	//on change la classe du nouveau pour qu'il soit current
	$(this).addClass('current');

	/* ________________ AUJOURD'HUI _____________ */
	if ($("nav#stats-tri li.current").text()=="Aujourd'hui") {
		var chart = new CanvasJS.Chart("chartContainer",
		{
			theme: "theme1",
			exportEnabled: true,
			animationEnabled: true,
			title: {
				text: "Mes relevés du jour"               
			},
			legend: {
				fontFamily: "kenyan_coffeeregular",
				fontStyle: "normal",
			},
				axisX: {
				valueFormatString: "HH:mm",
				interval:1,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 25,
			},
			axisY:{
				includeZero: false,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 20,
			},
			data: [{        
				type: "line",
				color: "#5c89c7",
				//lineThickness: 3,        
				dataPoints: [
					{ x:  new Date(2015, 03, 24, 08, 30), y: 130 },
					{ x:  new Date(2015, 03, 24, 12, 45), y: 135},
					{ x:  new Date(2015, 03, 24, 19, 20), y: 133},        
				]
		  	}]
		});
	}

	/* ________________ 7 DERNIERS JOURS _____________ */
	if ($("nav#stats-tri li.current").text()=="7 derniers jours") {
		var chart = new CanvasJS.Chart("chartContainer",
		{
			theme: "theme1",
			exportEnabled: true,
			animationEnabled: true,
			title: {
				text: "Mes statistiques des 7 derniers jours (moyenne sur chaque jour)"               
			},
			legend: {
				fontFamily: "kenyan_coffeeregular",
				fontStyle: "normal",
			},
				axisX: {
				valueFormatString: "DD/MM",
				interval:1,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 25,
			},
			axisY:{
				includeZero: false,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 20,
			},
			data: [{        
				type: "line",
				color: "#5c89c7",
				//lineThickness: 3,        
				dataPoints: [
					{ x:  new Date(2015, 03, 18), y: 130 },
					{ x:  new Date(2015, 03, 19), y: 135},
					{ x:  new Date(2015, 03, 20), y: 133}, 
					{ x:  new Date(2015, 03, 21), y: 136 },
					{ x:  new Date(2015, 03, 22), y: 130},
					{ x:  new Date(2015, 03, 23), y: 145},
					{ x:  new Date(2015, 03, 24), y: 132 },
				]
		  	}]
		});
	}

	/* ________________ DERNIER MOIS _____________ */
	if ($("nav#stats-tri li.current").text()=="Dernier mois") {
		var chart = new CanvasJS.Chart("chartContainer",
		{
			theme: "theme1",
			exportEnabled: true,
			animationEnabled: true,
			title: {
				text: "Mes statistiques du dernier mois (moyenne sur chaque jour)"               
			},
			legend: {
				fontFamily: "kenyan_coffeeregular",
				fontStyle: "normal",
			},
				axisX: {
				valueFormatString: "DD/MM",
				interval:1,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 25,
			},
			axisY:{
				includeZero: false,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 20,
			},
			data: [{        
				type: "line",
				color: "#5c89c7",
				//lineThickness: 3,        
				dataPoints: [
					{ x:  new Date(2015, 03, 01), y: 129},
					{ x:  new Date(2015, 03, 02), y: 136},
					{ x:  new Date(2015, 03, 03), y: 140 },
					{ x:  new Date(2015, 03, 04), y: 145 },
					{ x:  new Date(2015, 03, 05), y: 150},
					{ x:  new Date(2015, 03, 06), y: 123}, 
					{ x:  new Date(2015, 03, 07), y: 156 },
					{ x:  new Date(2015, 03, 08), y: 154},
					{ x:  new Date(2015, 03, 09), y: 140},
					{ x:  new Date(2015, 03, 10), y: 150 },
					{ x:  new Date(2015, 03, 11), y: 143 },
					{ x:  new Date(2015, 03, 12), y: 135},
					{ x:  new Date(2015, 03, 13), y: 157}, 
					{ x:  new Date(2015, 03, 14), y: 138 },
					{ x:  new Date(2015, 03, 15), y: 155},
					{ x:  new Date(2015, 03, 16), y: 145},
					{ x:  new Date(2015, 03, 17), y: 156 },
					{ x:  new Date(2015, 03, 18), y: 125 },
					{ x:  new Date(2015, 03, 19), y: 135},
					{ x:  new Date(2015, 03, 20), y: 133}, 
					{ x:  new Date(2015, 03, 21), y: 136 },
					{ x:  new Date(2015, 03, 22), y: 130},
					{ x:  new Date(2015, 03, 23), y: 145},
					{ x:  new Date(2015, 03, 24), y: 132 },
				]
		  	}]
		});
	}

	/* ________________ 3 DERNIERS MOIS _____________ */
	if ($("nav#stats-tri li.current").text()=="3 derniers mois") {
		var chart = new CanvasJS.Chart("chartContainer",
		{
			theme: "theme1",
			exportEnabled: true,
			animationEnabled: true,
			title: {
				text: "Mes statistiques des 3 derniers mois (moyenne sur chaque jour)"               
			},
			legend: {
				fontFamily: "kenyan_coffeeregular",
				fontStyle: "normal",
			},
				axisX: {
				valueFormatString: "DD/MM",
				interval:1,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 25,
			},
			axisY:{
				includeZero: false,
				labelFontFamily: "tall_filmsregular",
				labelFontWeight: "bold",
				labelFontSize: 20,
			},
			data: [{        
				type: "line",
				color: "#5c89c7",
				//lineThickness: 3,        
				dataPoints: [
					// mois -2
					{ x:  new Date(2015, 01, 01), y: 129},
					{ x:  new Date(2015, 01, 02), y: 136},
					{ x:  new Date(2015, 01, 03), y: 140},
					{ x:  new Date(2015, 01, 04), y: 145},
					{ x:  new Date(2015, 01, 05), y: 150},
					{ x:  new Date(2015, 01, 06), y: 123}, 
					{ x:  new Date(2015, 01, 07), y: 156},
					{ x:  new Date(2015, 01, 08), y: 154},
					{ x:  new Date(2015, 01, 09), y: 140},
					{ x:  new Date(2015, 01, 10), y: 150},
					{ x:  new Date(2015, 01, 11), y: 143},
					{ x:  new Date(2015, 01, 12), y: 135},
					{ x:  new Date(2015, 01, 13), y: 157}, 
					{ x:  new Date(2015, 01, 14), y: 138},
					{ x:  new Date(2015, 01, 15), y: 155},
					{ x:  new Date(2015, 01, 16), y: 145},
					{ x:  new Date(2015, 01, 17), y: 156},
					{ x:  new Date(2015, 01, 18), y: 125},
					{ x:  new Date(2015, 01, 19), y: 135},
					{ x:  new Date(2015, 01, 20), y: 133}, 
					{ x:  new Date(2015, 01, 21), y: 136},
					{ x:  new Date(2015, 01, 22), y: 130},
					{ x:  new Date(2015, 01, 23), y: 145},
					{ x:  new Date(2015, 01, 24), y: 132},
					{ x:  new Date(2015, 01, 25), y: 150},
					{ x:  new Date(2015, 01, 26), y: 143},
					{ x:  new Date(2015, 01, 27), y: 148},
					{ x:  new Date(2015, 01, 28), y: 138},
					{ x:  new Date(2015, 01, 29), y: 150},
					{ x:  new Date(2015, 01, 30), y: 157},

					// mois -1
					{ x:  new Date(2015, 02, 01), y: 129},
					{ x:  new Date(2015, 02, 02), y: 136},
					{ x:  new Date(2015, 02, 03), y: 140},
					{ x:  new Date(2015, 02, 04), y: 145},
					{ x:  new Date(2015, 02, 05), y: 150},
					{ x:  new Date(2015, 02, 06), y: 123}, 
					{ x:  new Date(2015, 02, 07), y: 156},
					{ x:  new Date(2015, 02, 08), y: 154},
					{ x:  new Date(2015, 02, 09), y: 140},
					{ x:  new Date(2015, 02, 10), y: 150},
					{ x:  new Date(2015, 02, 11), y: 143},
					{ x:  new Date(2015, 02, 12), y: 135},
					{ x:  new Date(2015, 02, 13), y: 157}, 
					{ x:  new Date(2015, 02, 14), y: 138},
					{ x:  new Date(2015, 02, 15), y: 155},
					{ x:  new Date(2015, 02, 16), y: 145},
					{ x:  new Date(2015, 02, 17), y: 156},
					{ x:  new Date(2015, 02, 18), y: 125},
					{ x:  new Date(2015, 02, 19), y: 135},
					{ x:  new Date(2015, 02, 20), y: 133}, 
					{ x:  new Date(2015, 02, 21), y: 136},
					{ x:  new Date(2015, 02, 22), y: 130},
					{ x:  new Date(2015, 02, 23), y: 145},
					{ x:  new Date(2015, 02, 24), y: 132},
					{ x:  new Date(2015, 02, 25), y: 150},
					{ x:  new Date(2015, 02, 26), y: 143},
					{ x:  new Date(2015, 02, 27), y: 148},
					{ x:  new Date(2015, 02, 28), y: 138},
					{ x:  new Date(2015, 02, 29), y: 150},
					{ x:  new Date(2015, 02, 30), y: 157},

					// mois en cours
					{ x:  new Date(2015, 03, 01), y: 129},
					{ x:  new Date(2015, 03, 02), y: 136},
					{ x:  new Date(2015, 03, 03), y: 140},
					{ x:  new Date(2015, 03, 04), y: 145},
					{ x:  new Date(2015, 03, 05), y: 150},
					{ x:  new Date(2015, 03, 06), y: 123}, 
					{ x:  new Date(2015, 03, 07), y: 156},
					{ x:  new Date(2015, 03, 08), y: 154},
					{ x:  new Date(2015, 03, 09), y: 140},
					{ x:  new Date(2015, 03, 10), y: 150},
					{ x:  new Date(2015, 03, 11), y: 143},
					{ x:  new Date(2015, 03, 12), y: 135},
					{ x:  new Date(2015, 03, 13), y: 157}, 
					{ x:  new Date(2015, 03, 14), y: 138},
					{ x:  new Date(2015, 03, 15), y: 155},
					{ x:  new Date(2015, 03, 16), y: 145},
					{ x:  new Date(2015, 03, 17), y: 156},
					{ x:  new Date(2015, 03, 18), y: 125},
					{ x:  new Date(2015, 03, 19), y: 135},
					{ x:  new Date(2015, 03, 20), y: 133}, 
					{ x:  new Date(2015, 03, 21), y: 136},
					{ x:  new Date(2015, 03, 22), y: 130},
					{ x:  new Date(2015, 03, 23), y: 145},
					{ x:  new Date(2015, 03, 24), y: 132},
				]
		  	}]
		});
	}
	chart.render();
	return false;
});