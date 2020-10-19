
const btn = document.getElementById('btn')
const form = document.getElementById('form')
const input = document.getElementById('input')
const result = document.querySelector('.result')

eventListeners()
function eventListeners(){

  form.addEventListener('submit', onSubmit)
    document.addEventListener('DOMContentLoaded', onPageLoad)
    document.addEventListener('click', removeItem)
}



function onSubmit(e){
    e.preventDefault()
  
    const userInput = input.value

    uiTemplate(userInput)

    addToStorage(userInput)
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

function onPageLoad(){
    let storeItems = getFromStorage()

     console.log('onLoad', storeItems)
    storeItems.forEach(item =>{

    uiTemplate(item)

    })
}

function removeItem(e){
    if(e.target.classList.contains('remove')){
        console.log('yes')
        e.target.parentElement.remove()
    }

    deleteFromStorage(e.target.parentElement.textContent)
}

function addToStorage(input){
    let storeItems = getFromStorage()

    storeItems.push(input)
    
    localStorage.setItem('items', JSON.stringify(storeItems))
   
    console.log(storeItems)
}

function getFromStorage(){
    let items ;
    
    const storeItems = localStorage.getItem('items')

    if(storeItems === null){
        items = [];
    }else{
        items = JSON.parse(storeItems)
    }

    return items

}



function deleteFromStorage(item){
let storeItems = getFromStorage()

    const deleteX = item.substring(0, item.length -1)
    console.log(deleteX)

    storeItems.forEach((item, index) =>{

        if(item === deleteX){
           item.splice( index, 1) 
        }
    })

    localStorage.setItem('items', storeItems)
}