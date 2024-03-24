import logo from './images/medical_modeling_logo.png';
import React from 'react';
import { useLogoutFunction, withAuthInfo, useRedirectFunctions } from '@propelauth/react';
import { useNavigate } from 'react-router-dom';
import './App.css';
import ImageGallery from "./ImageGallery";

function App({ isLoggedIn, user }) {
    const logoutFn = useLogoutFunction();
    const { redirectToSignupPage, redirectToLoginPage } = useRedirectFunctions();
    const navigate = useNavigate();
    const handleRedirectToHome = () => {
        navigate('/home/');
    };
    const color = '#4F4FAE';

    return (
        <div className="welcome-screen" style={{ backgroundColor: color, justifyContent: 'center' }}>
            <div className="centered-content">
                <img src={logo} alt="Medical Modeling Logo" className="centered-logo" />
                <h1 style={{ color: "white" }}>Welcome to Medical Modeling!</h1>
            </div>
            <div className="content">
                <div className="centered-container">
                    {isLoggedIn ? (
                        <>
                            <h3 style={{color: "white"}}> You are currently logged in as {user.firstName}</h3>
                            <button type="button" className="btn btn-info" onClick={() => navigate('/home/')}>
                                Go to Home
                            </button>
                            <button onClick={() => logoutFn()}>Click here to log out</button>
                        </>
                    ) : (
                        <>
                            <h3 style={{color: "white"}}>To get started, please log in or create a new account.</h3>
                            <br />
                            <button onClick={() => redirectToSignupPage()}>Sign up</button>
                            <button className="login-button" onClick={() => redirectToLoginPage()}>Login</button>
                        </>
                    )}
                </div>
                <ImageGallery />
            </div>
        </div>
    );
}

export default withAuthInfo(App);
