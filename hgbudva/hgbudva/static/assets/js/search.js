$(document).ready(function(){
    $("#search").keydown(function(e){
        if(e.keyCode === 13) {
            var current_url = window.location.href;
            var lang;
            console.log(current_url)
            if(current_url.indexOf('/en/') != -1) lang = 'en';
            else if(current_url.indexOf('/me/') != -1) lang = 'me';
            else if(current_url.indexOf('/de/') != -1) lang = 'de';
            else if(current_url.indexOf('/fr/') != -1) lang = 'fr';
            else if(current_url.indexOf('/it/') != -1) lang = 'it';
            else if(current_url.indexOf('/ru/') != -1) lang = 'ru';
            else lang = 'en';
            console.log(lang)
            var query = $("#search").val();
            window.location.href = "/search-results/?lang=" + lang + "&query=" + query;
            return false
            // window.location.href = "/"
        }
    })
})