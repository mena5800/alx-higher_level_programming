function setLanguage () {
  const lang = $('INPUT#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
  $.getJSON(url,
    function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    }
  );
}

$(document).ready(function () {
  $('INPUT#btn_translate').click(setLanguage);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      setLanguage();
    }
  });
});
