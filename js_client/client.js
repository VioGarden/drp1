const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://http://127.0.0.1:8000/api"
if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData() // get form data from element
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData, bodyStr)

    const options = {
        method: "POST",
        headers: {
            "ContentType": "appliction/json"
        },
        body: bodyStr
    }

    //fetch returns back a promise
    //.then handles the promise (like a function)
    fetch(loginEndpoint, options).then(response=>{
        console.log(response)
        return response.json()
    }).then(x => {
        console.log(x)
    }).catch(err=> {
        console.log('err', err)
    })
    // requests.post
}