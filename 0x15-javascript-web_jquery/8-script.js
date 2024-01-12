$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, textStatus) {
    const titles = data.results;

    for (let i = 0; i < titles.length; i++) {
      $('ul#list_movies').append(`<li>${titles[i].title}</li>`);
    }
  }
);
