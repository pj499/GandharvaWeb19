console.log('Hello');

$("#timer")
  .countdown("2019/01/01", function(event) {
    $(this).text(
      event.strftime('%D days %H:%M:%S')
    );
  });


(function ($) {
        "use strict";
        $('.next').click(function () {
            $('.carousel').carousel('next');
            return false;
        });
        $('.prev').click(function () {
            $('.carousel').carousel('prev');
            return false;
        });
    })
    (jQuery);

