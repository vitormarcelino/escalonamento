var resultados = (function () {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': 'resultados.json',
        'dataType': "json",
        'success': function (data) {
            json = data;
        }
    });
    return json;
})();

window.onload = function(){
	var ctx = document.getElementById("grafico").getContext("2d");
	ctx.canvas.width  = window.innerWidth*0.70;
  	ctx.canvas.height = window.innerHeight*0.70;
	window.myLine = new Chart(ctx).Bar(resultados);
}