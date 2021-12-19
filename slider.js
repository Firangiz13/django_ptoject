const swiper1 =new Swiper(".slider-1", {

autoplay:{
    delay:3500,
    disableOnIteraction:false,
},
grapbCursor:true,
effect:"fade",
loop:true,
navigation:{
   nextEl:".swiper-next",
   prevEl:".swiper-prev",
},

});