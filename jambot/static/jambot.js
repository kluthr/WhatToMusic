Typed.new(".writing", {
  strings: ["> Hi, I'm Jambot!<br>> Press play and I will write you a song..."],
  typeSpeed: 0,
  showCursor: false
});

$.ajax({
  url: "/create", 
  cache: false, 
  success: function(data) {
    var soundFile = document.createElement("audio");
    var src = document.createElement("source");
    src.src = "";
    soundFile.appendChild(src);
    soundFile.load();
    soundFile.volume = 0.000000;
          
    function play() {
      soundFile.currentTime = 0.01;
      soundFile.volume = .25;
      setTimeout(function(){soundFile.play();},1);
    }
    src.src = data.url;
    soundFile.appendChild(src);
    $('#playbutton').on('click', function() {
      play()
      Typed.new(".song", {
        strings: ["> Here's your song!<br>> " + data.notation + "<br>> I hope you like it!<br>>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<3 Jambot"],
        typeSpeed: 0,
        showCursor: false
      });
      $('#btnholder').html("<input type='button' class='btn' id='replaybutton' onclick='javascript:void();' value='Replay' />")
      $('#replaybutton').on('click', function() {
        play() 
      });
    });
  }
});

