/**
 * Created by Dominik on 25.05.2016.
 */

$(document).ready(function() {
    $("div.split-bar-horizontal-navbar").on("click",function(e){
        e.preventDefault();

        console.log("LOGGER");

        if ($('#navbar').css('display') == 'none')
        {
            $("#navbar").css({"display":"initial"});
            $("div.split-bar-horizontal-navbar").css({"margin-top":"-7px"});
            $("#split-bar-sidebar").css({"margin-top":"-7px"});
            $(".nav.nav-sidebar").css({"margin-top":"-7px"});
            $("#page-content-wrapper").css({"margin-top":"10px"});
        }
        else
        {
            $("#navbar").css({"display":"none"});
            $("div.split-bar-horizontal-navbar").css({"margin-top":"-70px"});
            $("#split-bar-sidebar").css({"margin-top":"-100px","height":"120vh"});
            $(".nav.nav-sidebar").css({"margin-top":"-70px"});
            $("#page-content-wrapper").css({"margin-top":"-60px"});
        }
    });

    $("div.split-bar-sidebar").on("click",function(e){
        e.preventDefault();

        if ($('#sidebar').css('display') == 'none')
        {
            $("#split-bar-sidebar").css({"margin-left":"160px"});
            $("#sidebar").css({"display":"initial"});
            $("div.split-bar-horizontal-navbar").css({"margin-left":"175px"});
            $("#page-content-wrapper").css({"margin-left":"20px"});
        }
        else
        {
            $("#split-bar-sidebar").css({"margin-left":"-15px"});
            $("#sidebar").css({"display":"none"});
            $("div.split-bar-horizontal-navbar").css({"margin-left":"-20px","width":"120vw"});
            $("#page-content-wrapper").css({"margin-left":"-180px"});
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