import React from 'react';
import { PropelAuth } from '@propelauth/client';

const LoginPage = () => {
  const handleLogin = async () => {
    try {
      const propelAuth = new PropelAuth({
        clientId: 'YOUR_CLIENT_ID',
        clientSecret: 'YOUR_CLIENT_SECRET',
        redirectUri: 'YOUR_REDIRECT_URI',
        // Other configuration options as needed
      });

      // Redirect the user to the PropelAuth login page
      await propelAuth.login();
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <div>
      <h1>Login Page</h1>
      <button onClick={handleLogin}>Login with PropelAuth</button>
    </div>
  );
};

export default LoginPage;