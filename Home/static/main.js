const navigationHeight = document.querySelector('#primary-navigation').offsetHeight;

console.log("Height of the navbar is: ", navigationHeight)
document.documentElement.style.setProperty('--scroll-padding', navigationHeight + "px");

document.documentElement.style.setProperty('--scroll-intro', navigationHeight + "px");
console.log("Height is: ", navigationHeight);
