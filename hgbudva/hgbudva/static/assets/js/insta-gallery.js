$(document).ready(function () {
    instafeedContainer = document.getElementById("instafeed");
    if (instafeedContainer) {
        var feed = new Instafeed({
            limit: 20,
            
            accessToken: "IGQVJXVUhoblRydUw5X1FJZAUJtUHp3bUlpblNqX181TEdtSzh0UzRUQkhOTUVCXzdCQ2pXanQ4elR3dEdPbzdaY2VCaUZAnZADdCRkJJcTNXUGJqdjFpN0hwc3Npek5BT0liZAEx0T2M0MW95bzBFWHZAYLQZDZD",
            after: function () {
                let images = $("#instafeed").find('li');
                if (images.length > 8) {
                    $(images.slice(8, images.length)).remove();
                }
            },
            template:
                '<li><figure class="uk-transition-toggle uk-light"><a title="instagram image" href="{{image}}" data-caption="{{caption}}"><img src="{{image}}" alt="HG Budvanska Rivijera Instagram Gallery"/></a></figure></li>'
        });
        feed.run();
    }
});
  