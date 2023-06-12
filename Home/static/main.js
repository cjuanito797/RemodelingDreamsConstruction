const navigationHeight = document.querySelector('#primary-navigation').offsetHeight;

console.log("Height of the navbar is: ", navigationHeight)

const socialNavHeight = document.querySelector('#social_nav').offsetHeight;
console.log("Height of the social navbar is: ", socialNavHeight)

console.log("Height of both the primary nav and social nav is: ", (navigationHeight + socialNavHeight))
const height = (navigationHeight + socialNavHeight)
document.documentElement.style.setProperty('--scroll-padding', height + "px");
