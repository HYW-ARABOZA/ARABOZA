
const openModalBtn = document.getElementById('open-modal');
const modal = document.getElementById('modal');
const closeModalBtn = document.getElementsByClassName('close')[0];

// 모델 열기
openModalBtn.addEventListener('click', function(event) {
  event.preventDefault(); // Prevent the default behavior of the link
  modal.style.display = 'block';
});

// 닫기 버튼 누르면 닫히게
closeModalBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

// 박 눌렀을때 닫히게 
window.addEventListener('click', function(event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});

