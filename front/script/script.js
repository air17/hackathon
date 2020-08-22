const inputData = document.getElementById('inputData'); // входные данные
const outputData = document.getElementById('outputData'); // выходные данные
const sendBtn = document.getElementById('sendRequest'); // кнопка отправить запрос

const API_URL = 'https://161e.tk/api/words'; // API

const request = (URL,Method = 'GET',value) => {
    // URL - Адрес куда будет ссылаться запрос
    // по умолчанию будет метод GET, если не передавать параметр Method
    // value - значение поля во входных данных

    fetch(URL,{
        method: Method,
        body: JSON.stringify({input: value})
    })

        .then((response) => {
            return response.json();
        })
        .then((data) => {
            outputData.innerHTML = data.editedInput
        })

}

sendBtn.onclick = () => request(API_URL,'POST',inputData.value);
