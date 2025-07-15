const user_id = document.getElementById('userid').value
const csrfToken= document.getElementById('csrf').value;
function searchMovie() {
    const query = document.getElementById('searchBox').value;
    if (!query) {
        alert("Please enter a movie name");
        return;
    }

     fetch(`/search/?query=${query}`)
    .then(response => response.json())
    .then(data => {
      const movies = data.Search || []; 
      displayMovies(movies); 
                  
    })
    .catch(error => console.error('Error:', error));
}


function displayMovies(movies) {
  const container = document.getElementById("movie-list");
  container.innerHTML = "";

  if (movies.length === 1) {
    container.classList.add("single-card");
  } else {
    container.classList.remove("single-card");
  }

  if (movies.length === 0) {
    container.innerHTML = '<p class="text-white ms-3">No results found.</p>';
    return;
  }

  movies.forEach((movie) => {
    const poster = movie.Poster !== "N/A" ? movie.Poster : "https://via.placeholder.com/300x400?text=No+Image";

    container.innerHTML += `
      <div class="col-sm-6 col-md-4 col-lg-3 mb-4">
        <div class="card first-card h-100">
          <img src="${poster}" alt="${movie.Title}" class="card-img-top movie-image">
          <div class="card-body second-card d-flex flex-column align-items-center">
            <h5 class="card-title">${movie.Title}</h5>
            <p class="card-text"><strong>Year:</strong> ${movie.Year}</p>
            
            <form action="/movie_add/${user_id}" method="post" >
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">

            <input type="hidden" name="user_id" value="${user_id}">
            <input name=poster type="hidden" value="${movie.Poster}">
            <input name="title" type="hidden" value="${movie.Title}">
            <input name="year" type="hidden" value="${movie.Year}">
            
            
            <button type="submit" class="btn btn-danger mt-auto"  >Add to list </button>
            </form>
          </div>
        </div>
      </div>
    `;
  });
  
}





