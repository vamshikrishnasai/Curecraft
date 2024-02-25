
// // For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAdvEoAWF0vwpJEe0Qkm4MCs2sk4SPzehI",
    authDomain: "curecraft-5775c.firebaseapp.com",
    projectId: "curecraft-5775c",
    storageBucket: "curecraft-5775c.appspot.com",
    messagingSenderId: "261713539538",
    appId: "1:261713539538:web:218b0d6456c7818e5b180b",
    measurementId: "G-2FNMEZHHWK"
  };

  
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
const auth = firebase.auth();

// Sign up function
function signUp() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    console.log(email, password);

    // Firebase code
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((result) => {
            // Signed in 
            window.open("signup.html", '_self');
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message);
            // Handle error
        });
}

// Sign In function
function signIn() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Firebase code
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((result) => {
            // Signed in
            window.open("userprofile.html", '_self');
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message);
            // Handle error
        });
}
