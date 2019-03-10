const sign = () => {
    let user = document.getElementById("user").value;
    let pas = document.getElementById("pass").value;
    if ((user === "") || (pas === "")) {
        alert("Enter userid and password")
    }
    if ((user === "Ramya") && (pas === "12345")) {
        sessionStorage.setItem("storageName", "Ramya");
        window.location.href = 'User.html';
    }
}


const logout = () => {
    sessionStorage.setItem("storageName", null);
    alert("You are logged out")
    window.location.href = 'index.html';
}

const signUp = () => {

    let a = document.getElementById("pass").value
    let b = document.getElementById("pass1").value
    if (a === b) {
        console.log("done")
        alert("User created !!!")
    }
    else {
        alert("Password did not match. \n Sign Up again !!!");
        window.location.href = 'index.html';
    }


}