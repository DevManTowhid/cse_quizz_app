// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyByl8jfzmLku9OSLBNijqGsLvS2Rb0c2fw",
  authDomain: "cse-quizz-app.firebaseapp.com",
  projectId: "cse-quizz-app",
  storageBucket: "cse-quizz-app.firebasestorage.app",
  messagingSenderId: "87173902689",
  appId: "1:87173902689:web:71b588f7ea53448462d520",
  measurementId: "G-J6YJ6EBKD5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);