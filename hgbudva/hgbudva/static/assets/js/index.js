let path = window.location.pathname;
let page = path.split("/").pop();

// FOR RETURN MESSAGE
function isVisible(e) {
    return !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
}

// FOR DATEPICKER
$(function () {
    let lang = getLannguage();
    $.datepicker.setDefaults($.datepicker.regional[lang]);
    let $dp1 = $("#datepicker1");
    let $dp2 = $("#datepicker2");
    let date_format = "mm/dd/yy";
    if(lang === 'me') {
        date_format = "dd/mm/yy"
    }
    $("#datepicker1").datepicker({
        minDate: new Date(),
        dateFormat: date_format,
        onSelect: function (value, date) {
            if (date_format == "dd/mm/yy") {
                value = value.substring(6,10)+"-"+value.substring(3,5)+"-"+value.substring(0,2)
            }
            const tomorrow = new Date(value);
            tomorrow.setDate(tomorrow.getDate() + 1);
            $("#datepicker2").datepicker("destroy");
            $dp2.datepicker({
                dateFormat: date_format,
                minDate: tomorrow,
                firstDay: 1
            });
            $("#datepicker2").datepicker("setDate", tomorrow);
        },
        firstDay: 1,
        onClose: function () {
            // $("#datepicker2").datepicker("show");
        }
    });
    $dp2.datepicker({
        dateFormat: date_format,
        minDate: 1
    });
    const tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    $dp1.datepicker().datepicker("setDate", new Date());
    $dp2.datepicker().datepicker("setDate", tomorrow);
});
// FOR DATEPICKER

// fix header css depending on device
const w = window.innerWidth;
const h = window.innerHeight;
let headerContainer = document.getElementById("header-container"),
    headerHero = document.getElementById("hero-header"),
    navbar = document.getElementById("navbar"),
    bookingForm = document.getElementById("phobs_book"),
    hotelMenu = document.getElementById("hotel-menu");
let formInHeader = $(bookingForm)
    .parent()
    .attr("id")
    ? true
    : false;
if (w > 960) {
    headerContainer.classList.add("width-padding");

    // headerHero.classList.remove("width-padding");
    if (formInHeader) {
        bookingForm.classList.remove("width-padding")
        bookingForm.style.opacity = 1;
    } else bookingForm.style.opacity = 1;
}
if (w < 960) {
    $(".accommodation-wrapper-alignment-correct").addClass("width-padding");
}
// w > 1200 ? navbar.classList.add("width-padding") : null;
window.onscroll = function () {
    window.innerWidth > 960 ? scrollFunction(window.innerWidth) : null;
    // if(window.innerWidth > 960) {
    //   if (
    //     document.body.scrollTop > 480 ||
    //     document.documentElement.scrollTop > 480
    //   ){
    //   }
    // }
};

function scrollFunction(windowInnerWidth) {
    var scroll = 265;
    if (windowInnerWidth < 1200) scroll = 480;
    if (
        document.body.scrollTop > scroll ||
        document.documentElement.scrollTop > scroll
    ) {
        headerHero.classList.add("removig-header");
        bookingForm.classList.add("width-padding", "booking-form-fixed");
        bookingForm.style.opacity = 1;
        hotelMenu.classList.add("hotel-menu-fixed");
        headerContainer.classList.remove("width-padding");
        $(".hotel-menu-slide").attr("uk-sticky", "offset: 102")
    } else {
        headerHero.classList.remove("removig-header");
        headerContainer.classList.add("width-padding");
        hotelMenu.classList.remove("hotel-menu-fixed");
        $(".hotel-menu-slide").attr("uk-sticky", "offset: 50")
        formInHeader
            ? bookingForm.classList.remove("booking-form-fixed", "width-padding")
            : bookingForm.classList.remove("booking-form-fixed");
    }
}

// PHOBS BOOKING
// PHOBS BOOKING
$("#phobs_book").submit(function (e) {
    let lang = getLannguage() ? getLannguage() : "en";
    let arrivalDate = $("#datepicker1").val(),
        departureDate = $("#datepicker2").val()
    if (lang == "me"){
        arrivalDate = arrivalDate.substring(3,6) + arrivalDate.substring(0,3) + arrivalDate.substring(6,10)
        departureDate = departureDate.substring(3,6) + departureDate.substring(0,3) + departureDate.substring(6,10)
    }
    let arrivalDateArray = arrivalDate.split("/");
    const date1 = new Date(arrivalDate);
    const date2 = new Date(departureDate);
    const diffTime = Math.abs(date2 - date1);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    // setting language for phobs
    $("input[name=lang]").val(lang);
    $("<input />")
        .attr("type", "hidden")
        .attr("name", "check_in_day")
        .attr("value", arrivalDateArray[1])
        .appendTo("#phobs_book");
    $("<input />")
        .attr("type", "hidden")
        .attr("name", "check_in_month")
        .attr("value", arrivalDateArray[0])
        .appendTo("#phobs_book");
    $("<input />")
        .attr("type", "hidden")
        .attr("name", "check_in_year")
        .attr("value", arrivalDateArray[2])
        .appendTo("#phobs_book");
    $("<input />")
        .attr("type", "hidden")
        .attr("name", "nights")
        .attr("value", diffDays)
        .appendTo("#phobs_book");
    return true;
});

function isMobile() {
    if (w < 960) {
        $("#phobs_book").attr(
            "action",
            "https://secure.phobs.net/webservice/mobile/booking.php"
        );
    } else {
        $("#phobs_book").attr("action", "https://secure.phobs.net/booking.php");
    }
}

isMobile();
//return message
jQuery(document).ready(function ($) {
    var currentLanguage = getLannguage();
    var returnMessage;
    if (currentLanguage == 'en') {
        returnMessage = ' 🔔 Book on time'
    } else if (currentLanguage == 'me') {
        returnMessage = ' ☞ Hej, vrati se'
    } else if (currentLanguage == 'it') {
        returnMessage = ' ☞ Ehi, torna indietro'
    } else if (currentLanguage == 'de') {
        returnMessage = ' ☞ Hey komm zurück'
    } else if (currentLanguage == 'fr') {
        returnMessage = ' ☞ Hé, reviens'
    } else if (currentLanguage == 'ru') {
        returnMessage = ' ☞ Эй, вернись'
    }
    // Get page title
    var pageTitle = $("title").text();
    // Change page title on blur
    $(window).blur(function () {
        $("title").text(returnMessage);
    });
    // Change page title back on focus
    $(window).focus(function () {
        $("title").text(pageTitle);
    });
});
// handling events
$(function () {
    //close hamburger menu
    $(document).mouseup(e => {
        if (!$(".mobile-menu").is(e.target) // if the target of the click isn't the container...
            && $(".mobile-menu").has(e.target).length === 0 && $(".uk-navbar-toggle-icon").has(e.target).length === 0) // ... nor a descendant of the container
        {
            if ($(".mobile-menu").attr('aria-hidden') == 'false') {
                UIkit.toggle('#toggle-animation').toggle();
            }
        }
    });
    $("#hotel-overview-dropdown").mouseenter(function () {
        $("#hotel-overview-dropdown-content").css("display", "block");
    });
    $("#hotel-overview-dropdown").mouseleave(function () {
        $("#hotel-overview-dropdown-content").css("display", "none");
    });
    $("#all-hotels-first-dropdown").mouseenter(function () {
        $("#all-hotels-dropdown-list").css("display", "block");
    });
    $("#all-hotels-first-dropdown").mouseleave(function () {
        $("#all-hotels-dropdown-list").css("display", "none");
    });
    $("#dropdown1").mouseenter(function () {
        $("#dropdown_content1").css("display", "block");
    });
    $("#dropdown1").mouseleave(function () {
        $("#dropdown_content1").css("display", "none");
    });
    $("#dropdown2").mouseenter(function () {
        $("#dropdown_content2").css("display", "block");
    });
    $("#dropdown2").mouseleave(function () {
        $("#dropdown_content2").css("display", "none");
    });
    $("#dropdown3").mouseenter(function () {
        $("#dropdown_content3").css("display", "block");
    });
    $("#dropdown3").mouseleave(function () {
        $("#dropdown_content3").css("display", "none");
    });
    $("#dropdown4").mouseenter(function () {
        $("#dropdown_content4").css("display", "block");
    });
    $("#dropdown4").mouseleave(function () {
        $("#dropdown_content4").css("display", "none");
    });
    $("#dropdown5").mouseenter(function () {
        $("#dropdown_content5").css("display", "block");
    });
    $("#dropdown5").mouseleave(function () {
        $("#dropdown_content5").css("display", "none");
    });
    $("#dropdown6").mouseenter(function () {
        $("#dropdown_content6").css("display", "block");
    });
    $("#dropdown6").mouseleave(function () {
        $("#dropdown_content6").css("display", "none");
    });
    $("#all-hotels-dropdown1").mouseenter(function () {
        $("#all-hotels-dropdown-content1").css("display", "block");
    });
    $("#all-hotels-dropdown1").mouseleave(function () {
        $("#all-hotels-dropdown-content1").css("display", "none");
    });
    $("#all-hotels-dropdown2").mouseenter(function () {
        $("#all-hotels-dropdown-content2").css("display", "block");
    });
    $("#all-hotels-dropdown2").mouseleave(function () {
        $("#all-hotels-dropdown-content2").css("display", "none");
    });
    $("#all-hotels-dropdown3").mouseenter(function () {
        $("#all-hotels-dropdown-content3").css("display", "block");
    });
    $("#all-hotels-dropdown3").mouseleave(function () {
        $("#all-hotels-dropdown-content3").css("display", "none");
    });
    $("#all-hotels-dropdown4").mouseenter(function () {
        $("#all-hotels-dropdown-content4").css("display", "block");
    });
    $("#all-hotels-dropdown4").mouseleave(function () {
        $("#all-hotels-dropdown-content4").css("display", "none");
    });
    $("#all-hotels-dropdown5").mouseenter(function () {
        $("#all-hotels-dropdown-content5").css("display", "block");
    });
    $("#all-hotels-dropdown5").mouseleave(function () {
        $("#all-hotels-dropdown-content5").css("display", "none");
    });
    $("#all-hotels-dropdown6").mouseenter(function () {
        $("#all-hotels-dropdown-content6").css("display", "block");
    });
    $("#all-hotels-dropdown6").mouseleave(function () {
        $("#all-hotels-dropdown-content6").css("display", "none");
    });
    // click on hotel card opens hotel overview page
    $(".hotel-card-container").click(function () {
        var url = $(this).attr("data-url");
        window.open(url, '_self');
    });
});

// FOR LANGUAGE DETECTION
function getLannguage() {
    const pathArray = window.location.pathname.split("/");
    let language = pathArray[1] ? pathArray[1] : "en";
    return language;
}

