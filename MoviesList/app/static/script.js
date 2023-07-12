


async function findAllMovies(title){
    const url=
    `https://imdb-api.projects.thetuhin.com/search?query=${title}`
    const response = await fetch(url);
    const data = await response.json()
    return data.results
}


// search result - present with title,year,picture,
const result= findAllMovies("Little Things")
console.log(result)


async function getMovieInfo(id){
    const url=
    `https://imdb-api.projects.thetuhin.com/title/${id}`
    const response = await fetch(url);
    const data = await response.json()
    return data
}

const movie=getMovieInfo('tt10016180')

async function fillObject(){
    // let movie={}
    const returnObj=await getMovieInfo('tt10016180');
    return(({ genre, image, plot, rating, runtime,spokenLanguages,title,year}) =>
      ({ genre, image, plot, rating, runtime,spokenLanguages,title,year }))(returnObj);

}



console.log(fillObject())