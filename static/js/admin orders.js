/*  global $, alert, console */

// To Reseve The Meal (User Show Order Page)

const addToBasket = document.getElementsByClassName('order-button');

Array.from(addToBasket).forEach( el => {
  el.addEventListener('click', () => {
    changeButton(el);
    changeOpacity(el);
  });
});

const changeButton = el => {
  el.textContent = 'Reserved';
  el.style.backgroundColor = '#333';
}

const changeOpacity = el => {
  const mealCard = el.closest('.image');
  mealCard.style.opacity = '0.5';
}


$(function() {

    'use strict';

    // Adjust Slider Section Center (User Show Order Page)
    
    $('.slider').each(function(){

        $(this).css('paddingTop', ($('.slider').height() -$('.intro').height())  /2)
        
    })

  // Adjust About-us Section Center (User Show Order Page)

    $('.about').each(function(){

        $(this).css('paddingTop', ($('.about').height() - $('.about-us').height()) /2)
        
    })

// Adjust Form Section Center ( Add New Meal + User Fill Order )

    $('form').each(function() {

        $(this).css('marginTop',(($('.image').height() - $('form').height()) /4))
    })

})

// Reservation (user fill order) To Check Validity Of Fields

var myInput = document.getElementById('reserve'),

    myName = document.getElementById('name'),

    myAddress = document.getElementById('address');


  myInput.onclick = function () {

    if(myName.checkValidity() && myAddress.checkValidity()){
      alert("Request Successfully Completed");
    }
   
  }




