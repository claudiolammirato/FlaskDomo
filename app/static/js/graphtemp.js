var chart;

function get_data() {

  $.ajax({
      url: '/gettempdata',
      type: 'GET',
      dataType: 'json',
      success: on_data
    })
  }

function on_data(data) {


  var d = new Array();

  for (i=0;i<Object.keys(data).length;i++) {
    d[i]=new Array();
    d[i][1]=data[i].temperature;
    d[i][0]=data[i].date*1000+3600000;

  }

  var options = {

    xaxis: {show: true, mode: "time", timeformat: "%I:%M %p", minTickSize: [1,"second"], twelveHourClock: true},
    yaxis: {min:-30, max: 50,  tickSize: 5},
    // DAYS xaxis: { show: true, mode: "time",  timeformat: "%m/%d/%y%",   minTickSize: [1, "day"]},
    grid: { hoverable: true },
    tooltip: { show: true, content: "%s | date: %x; temp: %y" }
   };
   //alert(d);
  //var d2 = [[data[0].date, data[0].temperature], [data[1].date, data[1].temperature]];
  //chart.setData([{data: data.values}]);
  $.plot(("#placeholder"),[d], options);
  //chart.setData([d2]);
  //chart.setupGrid();

  //chart.draw();

  //setTimeout(get_data, 1000);
}

$(function() {
//  chart = $.plot("#placeholder", [ ], {xaxis: {mode: "time"}});

  get_data();

});
