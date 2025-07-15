const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')
const message = document.querySelector('.password-mismatch')

password2.addEventListener('input',function(){
    if(password1.value !== password2.value){
        message.style.display = 'block'
    }
    else{
        message.style.display = 'none'
    }
})
let passwordmax = document.querySelector('.password-minimum')
password1.addEventListener('input', () => {
    pass1 = password1.value
    console.log(pass1,'password 1')
    if (pass1.length === 0 || pass1.length >= 8){
        passwordmax.classList.add('d-none')
        
    }
    else if (pass1.length < 8) {
        passwordmax.classList.remove('d-none')
        
    }
   
})

