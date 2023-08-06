// Fetch and prints how to say “Hello” depending on the language
$(document).ready(function () {
  function fetchAndDisplayTranslation() {
    const languageCode = $('#language_code').val();

    if (languageCode !== '') {
      $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
        const translation = data.hello;

        $('#hello').text(translation);
      }).fail(function () {
        $('#hello').text('Error: Language code not found');
      });
    }
  }

  $('#btn_translate').click(function () {
    fetchAndDisplayTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchAndDisplayTranslation();
    }
  });
});
