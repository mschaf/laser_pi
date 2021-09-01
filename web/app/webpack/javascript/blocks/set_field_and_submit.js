up.compiler('[set-field-and-submit]', (element, data) => {

    let form = element.closest('form')

    element.addEventListener('click', () => {
        form.querySelector('input[name="' + data['field'] + '"]').value = data['value']
        up.submit(form)
    })
})



