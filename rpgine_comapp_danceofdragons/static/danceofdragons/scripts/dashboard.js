/**
 * Created by Dominik on 25.05.2016.
 */

$(document).ready(function() {
    $("div.split-bar-sidebar").on("click",function(e){
        e.preventDefault();

        if ($('#sidebar').css('display') == 'none')
        {
            $("#split-bar-sidebar").css({"margin-left":"160px"});
            $("#sidebar").css({"display":"initial"});
            $("div#page-content-wrapper.page-content-wrapper").css({"padding-left":"40px"});
        }
        else
        {
            $("#split-bar-sidebar").css({"margin-left":"-10px"});
            $("#sidebar").css({"display":"none"});
            $("div#page-content-wrapper.page-content-wrapper").css({"padding-left":"-20px"});
        }
    });
});