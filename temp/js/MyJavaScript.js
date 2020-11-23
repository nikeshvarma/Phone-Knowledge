// scroll
(function ($) {
    $(document).ready(function () {
        $("#nav").hide();
        $(function () {
            $(window).scroll(function () {

                // set distance user needs to scroll before we start fadeIn
                if ($(this).scrollTop() < 500) {
                    $('#nav').fadeIn();
                } else {
                    $('#nav').fadeOut();
                }
            });
        });

    });
}(jQuery));


// scroll
(function ($) {
    $(document).ready(function () {
        $("#nav2").hide();
        $(function () {
            $(window).scroll(function () {

                if ($(this).scrollTop() > 600) {
                    $('#nav2').fadeIn();
                } else {
                    $('#nav2').fadeOut();
                }
            });
        });

    });
}(jQuery));

// review function
$('#view_more').click(function () {
    var hidden = $(this).parent().find('.d-none');
    var non_hidden = $(this).parent().find('.test');
    s = $(this).text();
    if (s === 'view more') {
        $(hidden).each(function () {
            $(this).removeClass('d-none').addClass('test');
            $('#view_more').text('view less');
        });
    } else {
        $(non_hidden).each(function () {
            $(this).removeClass('test').addClass('d-none');
            $('#view_more').text('view more');
        });
    }
});

//username checker
$('#id_username').change(function () {
    var username = $(this).val();
    $.ajax({
        url: '/account/valid-username/',
        data: {'username': username},
        dataType: 'json',
        success: function (data) {
            if (data.is_taken) {
                var status = $('#check_user').text('username is already taken');
            } else {
                $('#check_user').text('')
            }
        }
    });
});

$('#id_email').change(function () {
    var email = $(this).val();
    $.ajax({
        url: '/account/valid-email/',
        data: {'email': email},
        dataType: 'json',
        success: function (data) {
            if (data.is_registered) {
                var status = $('#check_email').text('An account is already registered with this email address');
            } else {
                $('#check_email').text('')
            }
        }
    });
});


// live search
$(document).ready(function () {
    $('#phone_search').keyup(function () {
        var phone = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/searchPhone/',
            data: {'phone': phone},
            dataType: 'html',
            success: searchData,
        });
    });

    function searchData(data, textStatus, jqXHR) {
        $('#result').html(data)
    }
});

$(document).ready(function () {
    $('.phone_compare').keyup(function () {
        var query = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/compare/',
            data: {'phone': query},
            dataType: 'html',
            success: searchDone,
        });
    });

    function searchDone(data, textStatus, jqXHR) {
        $('#result').html(data);
    }
});

/*
$(document).ready(function () {
    $("input").change(function () {
        var select = $(this).val();
        console.log(select);
        $.ajax({
            type: 'GET',
            url: '/filter_phones/',
            data: {'data': select},
            dataType: 'html',
            success: filterPhones,
        });
    });

    function filterPhones(data, textStatus, jqXHR) {
        $('#content').html(data);
        $('#show_this').removeClass('d-none');
        $('#hide_this').addClass('d-none');
    }
});
 */
