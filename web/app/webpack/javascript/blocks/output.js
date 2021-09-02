up.compiler('output', (element, data) => {

    let input = element.parentElement.querySelector('input')
    let form = element.closest('form')

    let updateValue = () => {
        if(data.round) {
            element.innerText = parseInt(input.value)
        }else{
            element.innerText = input.value
        }

    }

    if(input){
        updateValue()
        input.addEventListener('change', (event) => {
            updateValue()
            up.submit(form)
        })

    }


})



