
document.querySelector("form").onsubmit = function (event) {
    event.preventDefault(); 

  
    var formData = new FormData();
    formData.append("file", document.getElementById("file-input").files[0]);
    formData.append("paragraph", document.getElementById("paragraph").value);
    alert(
        "파일 업로드: " +
        formData.get("file") +
        "\n텍스트 내용: " +
        formData.get("paragraph")
    );
};

// 팝업
document.querySelector(".left-button").addEventListener("click", function () {
    openPopup("popup1");
});

document.querySelector(".right-button").addEventListener("click", function () {
    openPopup("popup2");
});

function openPopup(popupId) {
    var popup = document.getElementById(popupId);
    if (popup) {
        popup.style.display = "block";
    }
}

function closePopup(popupId) {
    var popup = document.getElementById(popupId);
    if (popup) {
        popup.style.display = "none";
    }
function saveContent() {
        var textareaContent = document.getElementById("paragraph").value;
        console.log("저장되었습니다:", textareaContent);
        closePopup("popup2");
      }
}
