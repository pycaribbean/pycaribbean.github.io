jQuery(document).ready(function($) {
      $('#slider-with-blocks-1').royalSlider({
        arrowsNav: true,
        loop: true,
        keyboardNavEnabled: true,
        controlsInside: false,
        imageScaleMode: 'fill',
        arrowsNavAutoHide: true,
        autoScaleSlider: true, 
        controlNavigation: 'bullets',
        thumbsFitInViewport: false,
        navigateByClick: true,
        startSlideId: 0,
        autoPlay: false,
        transitionType:'move',
        globalCaption: false,
        deeplinking: {
          enabled: true,
          change: false
        },
        /* size of all images http://help.dimsemenov.com/kb/royalslider-jquery-plugin-faq/adding-width-and-height-properties-to-images */
    
        autoPlay: {
        enabled: true,
        pauseOnHover: true
      }
      });
    });
 