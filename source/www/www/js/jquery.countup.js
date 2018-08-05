(function($){
	// Number of seconds in every time division
	var days	= 24*60*60,
		hours	= 60*60,
		minutes	= 60;
	// Creating the plugin
	$.fn.countup = function(prop){
		
		var options = $.extend({
			callback	: function(){},
			timestamp	: 0
		},prop);
		
		var left, d, h, m, s, positions;

		// Initialize the plugin
		init(this, options);
		
		positions = this.find('.position');
		
		(function tick(){
			
			// Time left
			left = Math.floor(((new Date()) - options.timestamp) / 1000);
			
			if(left < 0){
				left = 0;
			}
			
			// Number of days left
			d = Math.floor(left / days);
			switchDigit(positions.eq(0),Math.floor(d/1000)%10);
			switchDigit(positions.eq(1),Math.floor(d/100)%10);
			switchDigit(positions.eq(2),Math.floor(d/10)%10);
			switchDigit(positions.eq(3),d%10);
			left -= d*days;
			
			// Number of hours left
			h = Math.floor(left / hours);
			updateDuo(4, 5, h);
			left -= h*hours;
			
			// Number of minutes left
			m = Math.floor(left / minutes);
			updateDuo(6, 7, m);
			left -= m*minutes;
			
			// Number of seconds left
			s = left;
			updateDuo(8, 9, s);
			
			// Calling an optional user supplied callback
			options.callback(d, h, m, s);
			
			// Scheduling another call of this function in 1s
			setTimeout(tick, 1000);
		})();
		
		// This function updates two digit positions at once
		function updateDuo(minor,major,value){
			switchDigit(positions.eq(minor),Math.floor(value/10)%10);
			switchDigit(positions.eq(major),value%10);
		}
		
		return this;
	};


	function init(elem, options){
		elem.addClass('countupHolder');

		// Creating the markup inside the container
		$.each(['Days','Hours','Minutes','Seconds'],function(i){
			var boxName;
			if(this=="Days") {
				boxName = "天";
			}
			else if(this=="Hours") {
				boxName = "小时";
			}
			else if(this=="Minutes") {
				boxName = "分钟";
			}
			else {
				boxName = "秒";
			}

			if(this=="Days") {
				$('<div class="count'+this+'">' +
					'<span class="position">' +
						'<span class="digit static">0</span>' +
					'</span>' +
					'<span class="position">' +
						'<span class="digit static">0</span>' +
					'</span>' +
					'<span class="position">' +
						'<span class="digit static">0</span>' +
					'</span>' +
					'<span class="position">' +
						'<span class="digit static">0</span>' +
					'</span>' +
					'<span class="boxName">' +
						'<span class="'+this+'">' + boxName + '</span>' +
					'</span>'
				).appendTo(elem);
			}else{
				$('<div class="count'+this+'">' +
					'<span class="position">' +
						'<span class="digit static">0</span>' +
					'</span>' +
					'<span class="position">' +
						'<span class="digit static">0</span>' +
					'</span>' +
					'<span class="boxName">' +
						'<span class="'+this+'">' + boxName + '</span>' +
					'</span>'
				).appendTo(elem);
			}
			
			if(this!="Seconds"){
				elem.append('<span class="points">:</span><span class="countDiv countDiv'+i+'"></span>');
			}
		});

	}

	// Creates an animated transition between the two numbers
	function switchDigit(position,number){
		
		var digit = position.find('.digit')
		
		if(digit.is(':animated')){
			return false;
		}
		
		if(position.data('digit') == number){
			// We are already showing this number
			return false;
		}
		
		position.data('digit', number);
		
		var replacement = $('<span>',{
			'class':'digit',
			css:{
				top:0,
				opacity:0
			},
			html:number
		});
		
		// The .static class is added when the animation
		// completes. This makes it run smoother.
		
		digit
			.before(replacement)
			.removeClass('static')
			.animate({top:0,opacity:0},'fast',function(){
				digit.remove();
			})

		replacement
			.delay(100)
			.animate({top:0,opacity:1},'fast',function(){
				replacement.addClass('static');
			});
	}
})(jQuery);