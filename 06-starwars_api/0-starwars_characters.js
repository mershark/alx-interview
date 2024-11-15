#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) return console.error(err);

  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) return console.error(err);
      console.log(JSON.parse(body).name);
    });
  });
});
