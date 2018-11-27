const __interval = setInterval(() => {
    if (document.querySelector('.popupContent .time').innerText == ':00') {
        setTimeout(() => {
            y = new XMLHttpRequest();
            y.open('GET', 'http://localhost:8080/' + document.querySelector('.inputPanel span').parentElement.innerText);
            y.send();
        }, 516);

        window.clearInterval(__interval);
    }
})
