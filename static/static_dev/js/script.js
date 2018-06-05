// $(document).ready(function() {
//   let isButtonGrey = true;
//   $(".item-div").on("click", function(){
//       $(this).css("background-color", isButtonGrey ?"#000" : "#888" );
//       isButtonGrey = !isButtonGrey;
//     });
//   });


$('.click-container').on("click",function(){
 let itemid = $(this).attr("data-item-id");
 let $a_children = $(this).children();
 let $count_container = $a_children.find(".clicks-number");

 $.ajax(
   {
     type:"GET",
     url: '/items/click-count/',
     data: {
       item_id: itemid
     },
     success: function(data){
       $count_container.html(data)
     }
   });
 });
