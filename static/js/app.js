document.addEventListener("DOMContentLoaded", (e) => {
    console.log("Hello, world from app.js");
});



// back links
const back_links = document.querySelectorAll(".back-link");
for(let item of back_links) {
    item.addEventListener("click", (e) => {
        e.preventDefault();
        window.history.back();
    });
}