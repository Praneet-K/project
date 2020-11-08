document.querySelector('.search-button').addEventListener("click",function(){
	  this.parentElement.classList.toggle("open");
	  document.querySelector("#s").classList.toggle("display");
	  console.log(document.querySelector("#s"));
});
