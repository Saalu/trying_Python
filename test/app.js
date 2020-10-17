
const btn = document.getElementById('btn')
const form = document.getElementById('form')
const input = document.getElementById('input')
const result = document.querySelector('.result')

eventListeners()
function eventListeners(){

  form.addEventListener('submit', onSubmit)

}


function uiTemplate(input){
    const p = document.createElement('p')
    const removeBtn = document.createElement('a')
    removeBtn.innerText = 'X'
    removeBtn.classList.add('remove')

    p.textContent = input
    p.appendChild(removeBtn)
    result.appendChild(p)
}

function onSubmit(e){
    e.preventDefault()
  
    const userInput = input.value

    uiTemplate(userInput)


}