/**
 * Created by Dominik on 25.05.2016.
 */

console.log("JQUERY")

$( document ).ready(function() {
    $("div#split-bar").on("click",function(e){
        e.preventDefault()
        console.log("CLICKED!")
        $("div#sidebar-wrapper").hide();
        $("div#split-bar").show();
    });
});