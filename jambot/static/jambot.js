$(document).ready( function(){
  Typed.new(".writing", {
    strings: ["> Hi, I'm Jambot!<br>> Press play and I will write you a song..."],
    typeSpeed: 0,
    showCursor: false
  });
});

$(function() {
  $('#playbutton').on('click', function() {
    $.getJSON('/create', {
    }, function(data) {
      Typed.new(".song", {
        strings: ["> Here's your song!<br>> " + data.notation + "<br>> I hope you like it!<br>>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<3 Jambot"],
        typeSpeed: 0,
        showCursor: false
      });
      var soundFile = document.createElement("audio");
      soundFile.preload = "auto";
      var src = document.createElement("source");
      src.src = data.url;
      soundFile.appendChild(src);
      soundFile.load();
      soundFile.volume = 0.000000;
      soundFile.play();
      
      function play() {
          soundFile.currentTime = 0.01;
          soundFile.volume = 1.0;
          setTimeout(function(){soundFile.play();},1);
      }           
      play()
      $('#btnholder').html("<input type='button' class='btn' id='replaybutton' onclick='javascript:void();' value='Replay' />")
      $('#replaybutton').on('click', function() {
        play() 
      });
    });
    return false;
  });
});
