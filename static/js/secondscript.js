document.querySelector('.search-button').addEventListener("click",function(){
	  this.parentElement.classList.toggle("open");
	  document.querySelector('button').classList.toggle("display");
	  console.log(document.querySelector('button'));
});
