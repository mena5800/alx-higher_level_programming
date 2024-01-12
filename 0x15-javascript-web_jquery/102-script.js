$(document).ready(function () {
  $('INPUT#btn_translate').click(function (e) {
    const lang = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.getJSON(url,
      function (data, textStatus) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});
