$(function() {
	$(document).on('shown.calendar.calendario', function(e, instance){
		if(!instance) instance = cal;
		var $cell = instance.getCell(new Date().getDate());
		if($cell.hasClass('fc-today')) $cell.trigger('click.calendario');
	});

	var transEndEventNames = {
			'WebkitTransition' : 'webkitTransitionEnd',
			'MozTransition' : 'transitionend',
			'OTransition' : 'oTransitionEnd',
			'msTransition' : 'MSTransitionEnd',
			'transition' : 'transitionend'
		},
		transEndEventName = transEndEventNames[ Modernizr.prefixed( 'transition' ) ],
		$wrapper = $( '#custom-inner' ),
		$calendar = $( '#calendar' ),
		cal = $calendar.calendario({
			onDayClick : function( $el, data, dateProperties ) {
				if(data.content.length > 0 ) {
					showEvents(data.content, dateProperties );
				}
			},
			caldata : codropsEvents,
			displayWeekAbbr : true,
			events: 'click'
		} ),
		$month = $( '#custom-month' ).html( cal.getMonthName() ),
		$year = $( '#custom-year' ).html( cal.getYear() );

	$( '#custom-next' ).on( 'click', function() {
		cal.gotoNextMonth( updateMonthYear );
	} );
	$( '#custom-prev' ).on( 'click', function() {
		cal.gotoPreviousMonth( updateMonthYear );
	} );

	function updateMonthYear() {                
		$month.html( cal.getMonthName() );
		$year.html( cal.getYear() );
	}

	// just an example..
	function showEvents( contentEl, dateProperties ) {
		hideEvents();
		var $events = $( '<div id="custom-content-reveal" class="custom-content-reveal"><h4>Événements du ' + dateProperties.day + ' ' + dateProperties.monthname + ' ' + dateProperties.year + '</h4></div>' ),
			$close = $( '<span class="custom-content-close"></span>' ).on( 'click', hideEvents );
		$events.append( contentEl.join('') , $close ).insertAfter( $wrapper );
		setTimeout( function() {
			$events.css( 'top', '0%' );
		}, 25 );
	}

	function hideEvents() {
		var $events = $( '#custom-content-reveal' );
		if( $events.length > 0 ) {
			$events.css( 'top', '100%' );
			Modernizr.csstransitions ? $events.on( transEndEventName, function() { $( this ).remove(); } ) : $events.remove();
		}
	}
});