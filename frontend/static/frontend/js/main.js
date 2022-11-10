var images = [];

function image_Select(){
  var image = document.getElementById('image').files;
  for(i=0; i<image.length; i++){
    if(check_duplicate(image[i].name)){
      images.push({
        "name":image[i],
        "url": URL.createObjectURL(image[i]),
        "file":image[i],
      })
    }else{
      alert(image[i].name + " is already added to the list");
    }
    
  }
  // document.getElementById('form').reset();
  document.getElementById('con').innerHTML = image_Show()
};

function image_Show(){
  var image = "";
  images.forEach((i) => {
    image += `<div class="image_container d-flex justify-content-center position-relative">
    <img src="`+ i.url +`" alt="Image">
    <span class="position-absolute" onclick="delete_image(`+ images.indexOf(i) +`)">&times;</span>

</div>`;
  });
  return image;
};

function delete_image(e){
  images.splice(e, 1);
  document.getElementById('con').innerHTML = image_Show()
  
}


function check_duplicate(name){
  var image = true;
  if(images.length > 0){
    for(e=0; e <images.length; e++){
      if(images[e].name == name){
        image = false;
        break;
      }
    }
  }
  return image;
}
// =======================================================


var pictures = [];

function image_Selector(){
  var image = document.getElementById('imag').files;
  for(i=0; i<image.length; i++){
    if(check_duplicate(image[i].name)){
      pictures.push({
        "name":image[i],
        "url": URL.createObjectURL(image[i]),
        "file":image[i],
      })
    }else{
      alert(image[i].name + " is already added to the list");
    }
    
  }
  // document.getElementById('form').reset();
  document.getElementById('conn').innerHTML = image_Showed()
};

function image_Showed(){
  var image = "";
  pictures.forEach((i) => {
    image += `<div class="image_container d-flex justify-content-center position-relative">
    <img src="`+ i.url +`" alt="Image">
    <span class="position-absolute" onclick="delete_image(`+ pictures.indexOf(i) +`)">&times;</span>

</div>`;
  });
  return image;
};

function delete_image(e){
  pictures.splice(e, 1);
  document.getElementById('conn').innerHTML = image_Showed()
  
}


function check_duplicate(name){
  var image = true;
  if(pictures.length > 0){
    for(e=0; e <pictures.length; e++){
      if(pictures[e].name == name){
        image = false;
        break;
      }
    }
  }
  return image;
}


// ==========================product slides===============

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("demo");
  let captionText = document.getElementById("caption");
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
  captionText.innerHTML = dots[slideIndex-1].alt;
}