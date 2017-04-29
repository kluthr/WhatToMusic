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
      $.post( "/play", { "verse": JSON.stringify(data.verse) } )
      .done(function(wave) {   
        alert(wave.song);
        var audio = new Audio(wave.song);
        audio.play();         
        $('#btnholder').html("<input type='button' class='btn' id='replaybutton' onclick='javascript:void();' value='Replay' />")
        $('#replaybutton').on('click', function() {
          audio.play() 
        });
      });
    });
    return false;
  });
});

