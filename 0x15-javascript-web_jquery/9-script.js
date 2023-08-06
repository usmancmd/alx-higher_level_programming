//  Fetch from https://fourtonfish.com/hellosalut/?lang=fr and 
// displays the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const translation = data.hello;
      console.log('data', data)
    $('DIV#hello').text(translation);
  });
});
