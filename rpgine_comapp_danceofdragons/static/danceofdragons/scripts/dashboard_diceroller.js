$(document).ready(function () {
    $('img[class^="social-image"]').on("dragstart", function (e) {
        e.preventDefault();
    });
});
