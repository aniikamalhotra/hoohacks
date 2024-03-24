import logo from './images/medical_modeling_logo.png';
import React from 'react';
import { useLogoutFunction, withAuthInfo, useRedirectFunctions } from '@propelauth/react';
import { useNavigate } from 'react-router-dom';
import './App.css';


function App({ isLoggedIn }) {
    const logoutFn = useLogoutFunction();
    const { redirectToSignupPage, redirectToLoginPage } = useRedirectFunctions();
    const navigate = useNavigate();
    const handleRedirectToHome = () => {
        navigate('/home/');
    };
    const color = '#4F4FAE';

    return (
        <div className="welcome-screen" style={{ backgroundColor: color, justifyContent: 'center' }}>
            <div>
                <img src={logo} width={200} height={200} />
                <h1 style={{ color: "white" }}>Welcome to Medical Modeling!</h1>
            </div>
            <div className="content">
                <div>
                    {isLoggedIn ? (
                        <div className="centered-container">
                            <h3 style={{color: "white"}}>The User is logged in</h3>
                            <button type="button" class="btn btn-info">
                                <a href="http://127.0.0.1:8000/home/">Go to Home</a>
                            </button>
                            <button onClick={() => logoutFn()}>Click here to log out</button>
                        </div>
                    ) : (
                        <div>
                            <h3 style={{color: "white"}}>To get started, please log in or create a new account.</h3>
                            <br />
                            <button onClick={() => redirectToSignupPage()}>Sign up</button>
                            <button className="login-button" onClick={() => redirectToLoginPage()}>Login</button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
export default withAuthInfo(App);
