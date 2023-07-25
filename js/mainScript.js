let bubble = document.querySelectorAll('.bubble');
let flag = 1;
function bubbleUp(){
    setInterval(function(){
        if(flag == 1){
            flag = 0;
            bubble[flag].style.display = 'block';
            bubble[flag+1].style.display = 'none';
        }
        else{
            flag = 1;
            bubble[flag].style.display = 'block';
            bubble[flag-1].style.display = 'none';
        }
        console.log('!');
    }, 4000);
}
bubbleUp();
