let observer = new IntersectionObserver((e)=>{
    e.forEach((box)=>{
        box.target.style.opacity = '0';
    })
    e[0].target.style.left = '-50%';
    e[0].target.style.top = '-50%';
    // console.log(e[0].target);
    e[1].target.style.left = '80%';
    e[1].target.style.top = '-50%';
    // console.log(e[1].target);
    e[2].target.style.left = '-50%';
    // console.log(e[2].target);
    e[3].target.style.left = '-50%';
    e[3].target.style.bottom = '-60%';
    // console.log(e[3].target);
    e[4].target.style.right = '-50%';
    // console.log(e[4].target);
    e[5].target.style.right = '-50%';
    e[5].target.style.bottom = '-60%';
    // console.log(e[5].target);
});
let cloud = document.querySelectorAll('.cloud');
observer.observe(cloud[0]);
observer.observe(cloud[1]);
observer.observe(cloud[2]);
observer.observe(cloud[3]);
observer.observe(cloud[4]);
observer.observe(cloud[5]);
let logoObserver = new IntersectionObserver((e)=>{
    e.forEach((box)=>{
        box.target.style.opacity = '1';
        box.target.style.transform = 'scale(100%)';
    })
});
let logo = document.querySelector('.logo img');
logoObserver.observe(logo);
