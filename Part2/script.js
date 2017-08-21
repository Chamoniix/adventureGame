var nbClic = 0;


$(document).ready(function(){
    $("#egg").click(function(){
      nbClic++;
      if (nbClic < 5) {
        $('#notif').prepend("<p>Stop</p>").slideDown();;
      }
      else if (nbClic == 8) {
        $('#notif').prepend("<p>Arrete !!</p>");
      }
      else if (nbClic == 13) {
        $('#notif').prepend("<p>Ne fais pas ça... </p>");
      }
      else if (nbClic == 18) {
        $('#notif').prepend("<p>Tu vois pas le panneau rouge ?!</p>");
      }
      else if (nbClic == 25) {
        $('#notif').prepend("<p>Ok t'as gagné... Continue</p>");
        $('#egg').css({"cursor": "pointer"})
      }
      else if (nbClic == 50) {
        $('#notif').prepend("<p>Tu t'amuse bien ?</p>");
      }
      else if (nbClic == 70) {
        $('#notif').prepend("<p>Que ce passe-t-il..?</p>");
        setTimeout(function() {
        $('#notif').css('opacity', '0')
        $('#oeuf').css('opacity', '0')
        document.location.href = "base.html";
      }, 1000);
      }

    });
});
