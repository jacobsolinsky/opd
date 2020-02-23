$(document).ready(function() {

  $('.flexslider').flexslider({
    animation: "fade",
    controlNav: false,
    directionNav: false,
    slideshowSpeed: 7000,
    animationSpeed: 1500,
    initDelay: 0,
    start: function(slider){
      $('body').removeClass('loading');
    }
  });

  $('#Grid').mixitup();

  $(".grid").fitVids();

  $('a[rel*=leanModal]').leanModal({ top : 200, closeButton: ".modal_close" });

  $( "#accordion" ).accordion({
    collapsible: true,
    active: false,
    heightStyle: "content",
  });

});