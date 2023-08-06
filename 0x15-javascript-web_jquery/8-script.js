$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movieTitles = data.results;
    const listElement = $('UL#list_movies');
    movieTitles.forEach(function (movie) {
      listElement.append('<li>' + movie.title + '</li>');
    })
  });
});
