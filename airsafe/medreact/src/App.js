import logo from './logo.svg';
import React from 'react';
import { useLogoutFunction, withAuthInfo, useRedirectFunctions } from '@propelauth/react';
import './App.css';


function App({ isLoggedIn }) {
    const logoutFn = useLogoutFunction();
    const { redirectToSignupPage, redirectToLoginPage } = useRedirectFunctions();
    const color = '#4F4FAE';

    return (
        <div className="welcome-screen" style={{ backgroundColor: color }}>
            <h1 style={{ color: "white" }}>Welcome to Medical Modeling!</h1>
            {isLoggedIn ? (
                <div>
                    The User is logged in
                    <button onClick={() => logoutFn()}>Click here to log out</button>
                </div>
            ) : (
                <div>
                    To get started, please log in as a test user.
                    <br />
                    <button onClick={() => redirectToSignupPage()}>Sign up</button>
                    <button className="login-button" onClick={() => redirectToLoginPage()}>Login</button>
                </div>
            )}
        </div>
    );
}

export default withAuthInfo(App);
