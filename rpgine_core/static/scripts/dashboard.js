/**
 * Created by Dominik on 25.05.2016.
 */

$(function(){
    $(".dropdown-menu").on('click', 'li a', function(){
      $(".btn:first-child").text($(this).text());
      $(".btn:first-child").val($(this).text());
   });

});