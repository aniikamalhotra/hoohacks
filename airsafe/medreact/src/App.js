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
            <div>
                <h1 style={{ color: "white" }}>Welcome to Medical Modeling!</h1>
            </div>
            <div className="content">
                <div>
                    {isLoggedIn ? (
                        <div className="centered-container">
                            <h3 style={{color: "white"}}>The User is logged in</h3>
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
