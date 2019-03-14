function sign() {
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

function sign() {
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




function logout() {
    sessionStorage.setItem("storageName", null);
    alert("You are logged out")
    window.location.href = 'index.html';
}

function signUp() {
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


function evaluat() {
    alert("Thanks. \n Your report is generated !!!");
    // window.location.href = 'result.html';
    document.getElementById("result").innerHTML = `
    
    <h2> Overall Pass % </h2>

    <div class="progress">
    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width:60%">
      60% (success)
    </div>
  </div>
  <br>

  <h2> Overall fail % </h2>

  <div class="progress">
    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:40%">
      40% (failure)
    </div>
  </div>

  <br>
  <h2> Aptitude pass % </h2>

  <div class="progress">
    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:40%">
      40% Complete (warning)
    </div>
  </div>

  
  <br>
  <h2> Personality pass % </h2>
  <div class="progress">
    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width:20%">
      20% Complete (danger)
    </div>
  </div>


  <button onclick="alertuser()"> Apply for jobs </button>

    
    `
}


function alertuser(){

    alert('Based on your result % \n Some jobs have been applied \n Thanks')
    window.location.href = 'index.html';

}