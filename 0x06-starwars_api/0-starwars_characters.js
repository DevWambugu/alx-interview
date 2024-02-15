#!/usr/bin/node
// import the util library and declare constants
// Access the argument using the argument vector
const util = require('util');
const request = util.promisify(require('request'));
const idFilm = process.argv[2];

// Write an asyn function that accesses the api endpoint and fetches data
async function starwarsFilmCharacters (idFilm) {
  const apiEndpoint = `https://swapi-api.alx-tools.com/api/films/${idFilm}/`;
  let apiResponse = await (await request(apiEndpoint)).body;
  apiResponse = JSON.parse(apiResponse);
  const movieCharacters = apiResponse.characters;

  // loop through the characters and outputhem using console.log
  for (let i = 0; i < movieCharacters.length; i++) {
    const movieUrlCharacter = movieCharacters[i];
    let character = await (await request(movieUrlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsFilmCharacters(idFilm);
