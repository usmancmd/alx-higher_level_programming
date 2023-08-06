// Fetch and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    if (languageCode !== '') {
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
        const translation = data.hello;

        $('#hello').text(translation);
      }).fail(function () {
        $('#hello').text('Error: Language code not found');
      });
    }
  });
});
