    $(function () {
      UIkit.util.on('#gallery-mobile-slider', 'itemshown', function (event) {
        var max_images = parseInt(
          $(".gallery-counting-element").attr("max-count")
        );
        var current_element = parseInt(
          $(event.target).attr("count")
        );
        $(".gallery-counting-element").html(current_element + "/" + max_images);
    });
      //handle gallery navigation arrows and images preview at the bottom
      $(".gallery-next").click(function () {
        var max_images = parseInt(
          $(".gallery-counting-element").attr("max-count")
        );
        var current_element = parseInt(
          $(".gallery-counting-element").attr("count")
        );
        current_element++;
        if (current_element > max_images) current_element = 1;
        $(".gallery-counting-element").attr("count", current_element);
        $(".gallery-counting-element").html(current_element + "/" + max_images);
        UIkit.slider("#gallery-slider-navigation").show("next");
      });
      $(".gallery-previous").click(function () {
        var max_images = parseInt(
          $(".gallery-counting-element").attr("max-count")
        );
        var current_element = parseInt(
          $(".gallery-counting-element").attr("count")
        );
        current_element--;
        if (current_element < 1) current_element = max_images;
        $(".gallery-counting-element").attr("count", current_element);
        $(".gallery-counting-element").html(current_element + "/" + max_images);
        UIkit.slider("#gallery-slider-navigation").show("previous");
      });
    });
