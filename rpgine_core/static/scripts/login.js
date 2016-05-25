/**
 * Created by Dominik on 25.05.2016.
 */

$(".dropdown-menu li a").click(function(){
            var selText = $(this).text();
            $(this).parents('.btn-group').find('.dropdown-toggle').html(selText+' <span class="caret"></span>');
        });

        function showPassword()
        {
            var password_attr = $('#password').attr('type');

            if(password_attr != 'text') {

                $('.checkbox').addClass('show');
                $('#password').attr('type', 'text');

            } else {

                $('.checkbox').removeClass('show');
                $('#password').attr('type', 'password');

            }
        }