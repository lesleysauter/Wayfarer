
  var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("sqSlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}

  console.log("WayFAYer")

const closeBoxes = document.querySelectorAll('.close-box') || null;
const dialogueContainer = document.querySelector('.dialogueContainer') || null
const deleteModal = document.querySelector('.delete-modal') || null
const profileCity = document.querySelectorAll('.profile-city') || null
const profilePost = document.querySelectorAll('.profile-post') || null
const cities = document.querySelector('.cities-click') || null // profile and show-city pages
const postHeaderCount = document.querySelector('.profile-post-header') || null // profile and show-city pages

let count = 0;

if (cities !== null && postHeaderCount !== null ) {
    count = 0;
    profilePost.forEach(post => {
        post.hidden = false;
        count++
    })
    postHeaderCount.innerText = `Posts (${count})`
    
    cities.addEventListener('click', e => {
        profileCity.forEach(city => city.style.background = 'seashell')
        count = 0;
        profilePost.forEach(post => {
            post.hidden = false;
            count++
        })
        postHeaderCount.innerText = `Posts (${count})`
    })
}

if (profileCity !== null ) {
    profileCity.forEach(city => city.addEventListener('click', e => {
        profileCity.forEach(city => city.style.backgroundColor = 'seashell')
        city.style.backgroundColor = 'plum'
        const chosenCity = city.dataset.city
        count = 0;
        profilePost.forEach(post => {
            post.hidden = false;
            if (post.dataset.city !== chosenCity) {
                post.hidden = true
            } else {
                count++
            }
        })
        postHeaderCount.innerText = `Posts (${count})`
    })
    )
}

if (closeBoxes !== null) {
    closeBoxes.forEach(closeBox => {
        closeBox.addEventListener('click', e => {
            dialogueContainer.classList.add('hidden')
            if (deleteModal !== null && closeBox.dataset.modalshown === "true") {
                deleteModal.hidden = true
            } else {
                window.history.back()
            }
        })
    })
}

