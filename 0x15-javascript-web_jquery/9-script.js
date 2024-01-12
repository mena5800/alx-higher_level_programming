
$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data, textStatus) {
      $('div#hello').text(data.hello);
    }
  );
});
