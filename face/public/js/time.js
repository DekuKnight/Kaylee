var time = {
	timeFormat: config.time.timeFormat || 24,
	dateLocation: '.date',
	timeLocation: '.time',
	updateInterval: 1000,
	intervalId: null
};

time.update = function()
	{
		var now = moment();
		var date = now.format('LLLL').split(' ',4);
		date = date[0] + ' ' + date[1] + ' ' + date[2] + ' ' + date[3];

		$(time.dateLocation).html(date);
		$(time.timeLocation).html(now.format('hh') + ':' + now.format('mm') + '<span class="sec">'+now.format('ss')+ '</span>');

};

time.init = function () {

	if (parseInt(time.timeFormat) === 12) {
		time._timeFormat = 'hh'
	} else {
		time._timeFormat = 'HH';
	}

	this.intervalId = setInterval(function () {
		this.update();
	}.bind(this), this.updateInterval);

}