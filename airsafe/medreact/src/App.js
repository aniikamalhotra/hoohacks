import logo from './logo.svg';
import { useRedirectFunctions } from '@propelauth/react';
import './App.css';


function App() {
  const {redirectToLoginPage} = useRedirectFunctions();
  const color = '#4F4FAE';
  return (
    <div className="welcome-screen" style={{backgroundColor: color}}>
            <h1 style={{color:"white"}}>Welcome to Medical Modeling!</h1>
            <button className="login-button" onClick = {() => redirectToLoginPage()}>Login</button>
    </div>
  );
}

export default App;
