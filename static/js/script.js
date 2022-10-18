setInterval(() => {
    let texts = document.querySelectorAll('.helptext')
    texts.forEach(function(text){
        text.remove()
    })
}, 10);
