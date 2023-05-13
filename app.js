const searchForm = document.querySelector('#search-form');
const searchInput = document.querySelector('#search-input');
const recommendationsList = document.querySelector('#recommendations-list');


// #######using Fetch ajax - Web API#########

searchForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const movieName = searchInput.value;

  fetch(`http://localhost:2121/api/recommendations?name=${movieName}`) 
  // fetch('http://localhost:2121/api/recommendations', {
  //   method: 'POST',
  //   body: JSON.stringify({ movie_name: movieName }),
  //   headers: { 'Content-Type': 'application/json' }
  // })
    .then(response => response.json())
    .then(data => {
      recommendationsList.innerHTML = '';
      data.movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.innerText = movie;
        recommendationsList.appendChild(listItem);
      });

    console.log (data.movies)

    });
});





// // #######using XMLHttpRequest - Web API#########

// searchForm.addEventListener('submit', (e) => {
//   e.preventDefault();
//   const movieName = searchInput.value;
  
//   const xhr = new XMLHttpRequest();
//   xhr.open('POST', 'http://localhost:2121/api/recommendations', true);
//   xhr.open('GET', 'http://localhost:2121/api/recommendations', true);
//   xhr.setRequestHeader('Content-Type', 'application/json');
//   xhr.onreadystatechange = function () {
//     if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
//       const response = JSON.parse(this.responseText);
//       recommendationsList.innerHTML = '';
//       response.movies.forEach(movie => {
//         const listItem = document.createElement('li');
//         listItem.innerText = movie;
//         recommendationsList.appendChild(listItem);
//       });
//     }
//   };
//   xhr.send(JSON.stringify({ movie_name: movieName }));
// });