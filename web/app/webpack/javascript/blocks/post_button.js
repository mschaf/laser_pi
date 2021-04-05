up.compiler('[post-button]', (element) => {

  element.addEventListener('click', () => {
    up.request(element.dataset.url, { method: 'POST', params: JSON.parse(element.dataset.params) })
  })
})



