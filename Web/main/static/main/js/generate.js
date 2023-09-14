const input = document.getElementById('input_text_main');
const generateText = document.getElementById('generate_button');
const saveText = document.getElementById('save_button');

input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      generateText.click();
    }
});

generateText.addEventListener('click', () => {
    if (input.value !== "") {
        saveText.style.opacity = 1;
        saveText.style.pointerEvents = 'auto';
    }
});

saveText.addEventListener('click', () => {
    var textToSave1 = document.getElementById("text_output_1").innerText;
    var textToSave2 = document.getElementById("text_output_2").innerText;
    var textToSave3 = document.getElementById("text_output_3").innerText;

    var fileName = "generated_text.txt";

    var blob = new Blob(["Первый вариант текста:\n" + textToSave1 + "\n\nВторой вариант текста:\n" + textToSave2 + "\n\nТретий вариант текста:\n" + textToSave3], {type: "text/plain;charset=utf-8"});
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
});