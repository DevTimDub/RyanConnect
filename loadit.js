const url = 'https://timetable-lookup.p.rapidapi.com/TimeTable/ARN/STN/20230620/';
const params = new URLSearchParams({ Airline: 'FR' });

fetch(url + '?' + params, {
  headers: {
    'X-RapidAPI-Key': 'f97e3dbab8mshb83b4a869cc05bbp1448fajsna77ddd7b5e76',
    'X-RapidAPI-Host': 'timetable-lookup.p.rapidapi.com'
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
