/**
 * Created by Dominik on 25.05.2016.
 */

console.log("JQUERY")

$(document).ready(function() {
    $("div#split-bar").on("click",function(e){
        console.log("COLLAPSE");
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
        //$("div#split-bar").css({"left":"250px","position":"absolute","width":"1000px"});
        $('<div id="split-bar-return"></div>').insertBefore("div#wrapper");
        //$("#wrapper").removeClass("toggled");
    });

    $("div#split-bar-return").on("click",function(e){
        console.log("RETURN");
        e.preventDefault();
        $("#wrapper").removeClass("toggled");
    });
});