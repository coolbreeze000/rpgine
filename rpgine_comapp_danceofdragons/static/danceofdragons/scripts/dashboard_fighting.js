/**
 * Created by Dominik on 29.05.2016.
 */
$(document).ready(function() {
     $("div.split-bar-horizontal-top").on("click",function(e){
        e.preventDefault();

        if ($('#headline').css('display') == 'none')
        {
            $("#split-bar-horizontal-top").css({"margin-top":"100px"});
            $("#headline").css({"display":"initial"});
        }
        else
        {
            $("#split-bar-horizontal-top").css({"margin-top":"-100px"});
            $("#headline").css({"display":"none"});
        }
    });
});