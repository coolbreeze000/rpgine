$(document).ready(function () {
    $("#page-content").on('dragstart', 'img[class^="social-image"]', function(e) {
        e.preventDefault();
    });
});
