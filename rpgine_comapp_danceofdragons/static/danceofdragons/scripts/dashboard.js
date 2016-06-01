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
            $("#split-bar-sidebar").css({"margin-left":"-15px"});
            $("#sidebar").css({"display":"none"});
            $("div#page-content-wrapper.page-content-wrapper").css({"padding-left":"-20px"});
        }
    });

    $("#navbar-settings-icon").on("mouseover",function(e) {
        e.preventDefault();
        $("#navbar-settings-icon").removeClass("fa fa-cog fa-2x fa-fw").addClass("fa fa-cog fa-spin fa-2x fa-fw");
    });

    $("#navbar-settings-icon").on("mouseleave",function(e) {
        e.preventDefault();
        $("#navbar-settings-icon").removeClass("fa fa-cog fa-spin fa-2x fa-fw").addClass("fa fa-cog fa-2x fa-fw");
    });
});