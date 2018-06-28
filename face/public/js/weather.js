var weather = {
		lang: config.lang || 'en',
		params : config.weather.params || null,
		iconTable : {
			'01d':'wi-day-sunny',
			'02d':'wi-day-cloudy',
			'03d':'wi-cloudy',
			'04d':'wi-cloudy-windy',
			'09d':'wi-showers',
			'10d':'wi-rain',
			'11d':'wi-thunderstorm',
			'13d':'wi-snow',
			'50d':'wi-fog',
			'01n':'wi-night-clear',
			'02n':'wi-night-cloudy',
			'03n':'wi-night-cloudy',
			'04n':'wi-night-cloudy',
			'09n':'wi-night-showers',
			'10n':'wi-night-rain',
			'11n':'wi-night-thunderstorm',
			'13n':'wi-night-snow',
			'50n':'wi-night-alt-cloudy-windy'
		},
		temperatureLocation: '.temp',
		locationLocation: '.location',
		forecastLocation: '.forecast',
		apiVersion: '2.5',
		apiBase: 'http://api.openweathermap.org/data/',
		weatherEndpoint: 'weather',
		forecastEndpoint: 'forecast',
		updateInterval: config.weather.interval || 10000,
		fadeInterval: config.weather.fadeInterval || 1000,
		intervalId: null
}

weather.round = function (temp)
{
	return Math.round(temp);
}

weather.updateCurrentWeather = function()
{
	$.getJSON(weather.apiBase + '/' + weather.apiVersion + '/' + weather.weatherEndpoint, weather.params, function(json, textStatus) {

		var temp = weather.round(json.main.temp);
		var wind = json.wind.speed;
		
		//Display Location
		var loc = $('<span class=".location">'+ weather.params['q'] +'</span>');
		$(weather.locationLocation).updateWithText(loc,weather.fadeInterval);

		//Display Current Weather
		var iconClass = weather.iconTable[json.weather[0].icon];
		var icon = $('<span/>').addClass('icon').addClass('dimmed').addClass('wi').addClass(iconClass);
		$(weather.temperatureLocation).updateWithText(icon.outerHTML()+temp+'&deg; F', weather.fadeInterval);

	});

};

weather.updateWeatherForecast = function()
{
	$.getJSON(weather.apiBase + '/' + weather.apiVersion + '/' + weather.forecastEndpoint, weather.params, function(json, textStatus) {

		var forecastData = {};

		for (var i in json.list) {
			var forecast = json.list[i];
			var dateKey  = forecast.dt_txt.substring(0, 10);

			if (forecastData[dateKey] == undefined) {
				forecastData[dateKey] = {
					'timestamp':forecast.dt * 1000,
					'icon':forecast.weather[0].icon,
					'temp_min':forecast.main.temp,
					'temp_max':forecast.main.temp
				};
			} else {
				forecastData[dateKey]['icon'] = forecast.weather[0].icon;
				forecastData[dateKey]['temp_min'] = (forecast.main.temp < forecastData[dateKey]['temp_min']) ? forecast.main.temp : forecastData[dateKey]['temp_min'];
				forecastData[dateKey]['temp_max'] = (forecast.main.temp > forecastData[dateKey]['temp_max']) ? forecast.main.temp : forecastData[dateKey]['temp_max'];
			}

		}
		
		var forecastTable = $('<table />').addClass('forecast-table');
		var opacity = 1.155;
		
		for (var i in forecastData) {
			if(opacity <= 1){
				var forecast = forecastData[i];
				var iconClass = weather.iconTable[forecast.icon];
				var dt = new Date(forecast.timestamp);
				var row = $('<tr />').css('opacity', opacity);
	
				row.append($('<td/>').addClass('temp-min').html('/'+weather.round(forecast.temp_min)+'&deg;'));
				row.append($('<td/>').addClass('temp-max').html(weather.round(forecast.temp_max)+'&deg;'));
				row.append($('<td/>').addClass('icon-small').addClass('wi').addClass(iconClass));

				if(opacity == 1){
					row.append($('<td/>').addClass('day').html("Today"));
				} else{					
					row.append($('<td/>').addClass('day').html(moment.weekdays(dt.getDay())));
				}


				forecastTable.append(row);
			}
			opacity -= 0.155;							
		}

		$(weather.forecastLocation).updateWithText(forecastTable, weather.fadeInterval);
	});

};


weather.init = function () {

	if (this.params.lang === undefined) {
		this.params.lang = this.lang;
	}

	this.intervalId = setInterval(function () {
		this.updateCurrentWeather();
		this.updateWeatherForecast();
	}.bind(this), this.updateInterval);

}