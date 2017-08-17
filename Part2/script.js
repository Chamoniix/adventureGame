var nbClic = 0;


$(document).ready(function(){
    $("#egg").click(function(){
      nbClic++;
      if (nbClic < 5) {
        $('#notif').prepend("<p>Stop</p>").slideDown();;
      }
      else if (nbClic == 8) {
        $('#notif').prepend("<p>Please Stop </p>");
      }
      else if (nbClic == 15) {
        $('#notif').prepend("<p>Stop this !!</p>");
      }
      else if (nbClic == 30) {
        $('#notif').prepend("<p>Can't you see the red sign ?</p>");
      }
      else if (nbClic == 50) {
        $('#notif').prepend("<p>Ok you won.... Keep going</p>");
        $('#egg').css({"cursor": "pointer"})
      }
      else if (nbClic == 80) {
        $('#notif').prepend("<p>Are you having fun ?</p>");
      }
      else if (nbClic == 150) {
        $('#notif').prepend("<p>What's happenning ...?</p>");
      }

    });
});
