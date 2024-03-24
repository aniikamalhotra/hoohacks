import logo from './images/medical_modeling_logo.png';
import React from 'react';
import { useLogoutFunction, withAuthInfo, useRedirectFunctions } from '@propelauth/react';
import { useNavigate } from 'react-router-dom';
import './App.css';

const App = withAuthInfo((props) => {
    // isLoggedIn and user are injected automatically from withAuthInfo
    const logoutFn = useLogoutFunction();
    const color = '#4F4FAE';
    if (props.isLoggedIn) {
        return (
            <div className="welcome-screen" style={{ backgroundColor: color, justifyContent: 'center' }}>
                <div>
                    <img src={logo} width={200} height={200} />
                    <h1 style={{ color: "white" }}>Welcome to Medical Modeling!</h1>
                </div>
                <div className="content">
                    <div className="centered-container">
                        <h3 style={{color: "white"}}> You are currently logged in as {props.user.firstName}</h3>
                        <button type="button" className="btn btn-info">
                            <a href="http://127.0.0.1:8000/home/">Go to Home</a>
                        </button>
                        <button onClick={() => props.logoutFn()}>Click here to log out</button>
                    </div>
                </div>
            </div>
        );
    } else {
        const { redirectToSignupPage, redirectToLoginPage } = useRedirectFunctions();
        return (
            <div className="welcome-screen" style={{ backgroundColor: color, justifyContent: 'center' }}>
                <div>
                    <img src={logo} width={200} height={200} />
                    <h1 style={{ color: "white" }}>Welcome to Medical Modeling!</h1>
                </div>
                <div className="content">
                    <div>
                        <h3 style={{color: "white"}}>To get started, please log in or create a new account.</h3>
                        <br />
                        <button onClick={() => redirectToSignupPage()}>Sign up</button>
                        <button className="login-button" style="background: darkcyan;color:white;" onClick={() => redirectToLoginPage()}>Login</button>
                    </div>
                </div>
            </div>
        );
    }
});

export default App;
