
const openModalBtn = document.getElementById('open-modal');
// open-modal id를 가진 요소를 openModalBtn에 할당 - 모달요소를 열기 위함
const modal = document.getElementById('modal');
// modal id를 가진 요소를 modal에 할당 - 실제 모달창
const closeModalBtn = document.getElementsByClassName('close')[0];
// close 라는 class를 가진 요소를 closeModalBtn 에 할당 - 'close'[0]인 이유는 엔티티코드에 할당하기위해서

// 모델 열기
openModalBtn.addEventListener('click', function(event) {
  event.preventDefault(); 
  modal.style.display = 'block';
});

// 클릭하면 modal창 표시

closeModalBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});
//  엔티티코드를 클릭하면 display = 'none'해서 안보이게 = 닫히게


window.addEventListener('click', function(event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});
// window 전체에 클릭이벤트리스너 추가 >  if 문으로 event.target이 modal 일때만 modal이 닫히게 만들어짐 

