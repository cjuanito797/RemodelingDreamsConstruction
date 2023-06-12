const navigationHeight = document.querySelector('#primary-navigation').offsetHeight;

console.log("Height of the navbar is: ", navigationHeight)
document.documentElement.style.setProperty('--scroll-padding', navigationHeight + "px");

const socialNavHeight = document.querySelector('#social_nav').offsetHeight;
console.log("Height of the social navbar is: ", socialNavHeight)

console.log(navigationHeight + socialNavHeight)
