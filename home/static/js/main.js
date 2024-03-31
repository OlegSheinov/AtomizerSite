const telegram = window.Telegram.WebApp;
const buttonColor = getComputedStyle(document.documentElement).getPropertyValue('--tg-theme-button-color');
const buttonTextColor = getComputedStyle(document.documentElement).getPropertyValue('--tg-theme-button-text-color');

telegram.expand();
telegram.MainButton.setText("Click to select file"); //изменяем текст кнопки иначе
telegram.MainButton.textColor = buttonColor; //изменяем цвет текста кнопки
telegram.MainButton.color = buttonTextColor; //изменяем цвет бэкграунда кнопки
telegram.MainButton.setParams({"color": buttonColor, "text_color": buttonTextColor}); //так изменяются все параметры
// telegram.MainButton.show();

function fileInputFunc() {
    let input = document.getElementById("fileInput");
    let inputLabel = document.getElementById("fileInputLabel");
    const img = new Image();
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    let imgLoaded = false
    let file = input.files[0];
    let formData = new FormData();
    formData.append("videoFile", file);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/get_frame/");
    xhr.send(formData);
    imgLoaded = false
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let header = document.getElementById('header')
            header.style.marginTop = "calc(100% - 300px)";
            let response = xhr.responseText;
            let b64_img = JSON.parse(response)
            img.src = "data:image/png;base64," + b64_img.first_frame;
            img.onload = function () {
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            }
            imgLoaded = true
            inputLabel.hidden = true;
        }
    }
    console.log('Выбран файл:', file);
}

telegram.MainButton.onClick(() => {

});

console.log("jfsgkjdfsg");