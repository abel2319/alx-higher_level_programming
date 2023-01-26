const $ = window.jQuery;
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
    let tmp = data.results;
    for (let i in tmp) {
      console.log(i)
      $('UL#list_movies').append('<li>' + tmp[i].title + '</li>')
    }
  });
});
