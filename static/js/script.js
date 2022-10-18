// setInterval(() => {
//     // api url
// const api_url =
// "http://127.0.0.1:8000/en/api/blog";

// // Defining async function
// async function getapi(url) {

// // Storing response
// const response = await fetch(url);

// // Storing data in form of JSON
// var data = await response.json();
// console.log(data);
// if (response) {
// hideloader();
// }
// show(data);
// }
// // Calling that async function
// getapi(api_url);

// // Function to hide the loader
// function hideloader() {
// document.getElementById('loading').style.display = 'none';
// }
// // Function to define innerHTML for HTML table
// function show(data) {
// document.querySelector('#employees').innerHTML = data[0].title
// }
// }, 10);