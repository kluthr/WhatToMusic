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
      var song = new Howl({
          urls: [data.url],
          autoplay: true,
          loop: true,
          volume: 0.5,
          onend: function() {
             alert('Finished!');      
          }
      });        
      song.play()
      $('#btnholder').html("<input type='button' class='btn' id='replaybutton' onclick='javascript:void();' value='Replay' />")
      $('#replaybutton').on('click', function() {
        song.play() 
      });
    });
    return false;
  });
});

