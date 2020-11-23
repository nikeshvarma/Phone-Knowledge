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

// incomplete
$(document).ready(function () {
    $('#search_brand').keyup(function () {
        var query = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/filter/filter-brands/brand-search/',
            data: {'query': query},
            dataType: 'html',

            success: function () {
                $('#include_brand_search');
            }
        });
    });
});


var checkboxValues = JSON.parse(localStorage.getItem('checkboxValues')) || {};
var $checkboxes = $("#checkbox-container :checkbox");
$checkboxes.on("change", function () {
    $checkboxes.each(function () {
        checkboxValues[this.id] = this.checked;
    });

    localStorage.setItem("checkboxValues", JSON.stringify(checkboxValues));
});

// On page load
$.each(checkboxValues, function (key, value) {
    $("#" + key).prop('checked', value);
});

// On close window
$(window).on('reset', function () {
    localStorage.removeItem('checkboxValues');
});
// Close


//  image slider
let thumbnails = document.getElementsByClassName('thumbnail');
let activeImg = document.getElementsByClassName('thumbnail');

for (var i = 0; i < thumbnails.length; i++) {
    thumbnails[i].addEventListener('mouseover', function () {
        if (activeImg.length > 0) {
            activeImg[0].classList.remove('active')
        }
        this.classList.add('active');
        document.getElementById('feature').src = this.src;
    });
}
