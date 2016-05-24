$(document).ready(function () {
  $('[data-toggle=offcanvas]').click(function () {
    if ($('.sidebar-offcanvas').css('background-color') == 'rgb(255, 255, 255)') {
	    $('.list-group-item').attr('tabindex', '-1');
    } else {
	    $('.list-group-item').attr('tabindex', '');
    }
    $('.row-offcanvas').toggleClass('active');

  });

    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });
});

var min = 300;
var max = 3600;
var mainmin = 200;

$('#split-bar').mousedown(function (e) {
    e.preventDefault();
    $(document).mousemove(function (e) {
        e.preventDefault();
        var x = e.pageX - $('#sidebar-wrapper').offset().left;
        if (x > min && x < max && e.pageX < ($(window).width() - mainmin)) {
          $('#sidebar-wrapper').css("width", x);
          $('#page-content-wrapper').css("margin-left", x);
        }
    })
});
$(document).mouseup(function (e) {
    $(document).unbind('mousemove');
});