// 스크롤시 페이지 상단에 네비게이션바 고정
window.onscroll = () => {

    if (window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }
    else {
        document.querySelector('.header .header-2').classList.remove('active');
    }

}

// index.html 홈화면 섹션 슬라이더

var timeOut = 2000;
var slideIndex = 0;
var autoOn = true;

autoSlides();

function autoSlides() {
    timeOut = timeOut - 20;

    if (autoOn == true && timeOut < 0) {
        showSlides();
    }
    setTimeout(autoSlides, 20);
}

function prevSlide() {

    timeOut = 2000;

    var slides = document.getElementsByClassName("slides");
    var dots = document.getElementsByClassName("dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slideIndex--;

    if (slideIndex > slides.length) {
        slideIndex = 1
    }
    if (slideIndex == 0) {
        slideIndex = 5
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

function showSlides() {

    timeOut = 2000;

    var slides = document.getElementsByClassName("slides");
    var dots = document.getElementsByClassName("dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

function currentSlide(n) {
  var slides = document.getElementsByClassName("slides");
  var dots = document.getElementsByClassName("dot");

  if (n > slides.length) {n = 1}
    else if(n < 1) {n = slides.length}

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
       
  slides[n-1].style.display = "block";  
  dots[n-1].className += " active";
}