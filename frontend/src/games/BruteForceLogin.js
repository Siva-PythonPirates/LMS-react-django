import React, { useState } from 'react';
import './BruteForceLogin.css';

function BruteForceLogin() {
  const [username, setUsername] = useState('');
  const [passwordList, setPasswordList] = useState('');
  const [results, setResults] = useState([]);
  const [isBruteForcing, setIsBruteForcing] = useState(false);

  const correctPassword = 'password123'; // Set this as the correct password for the demonstration

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordListChange = (e) => {
    setPasswordList(e.target.value);
  };

  const startBruteForceAttack = () => {
    setResults([]);
    setIsBruteForcing(true);
    const passwords = passwordList.split('\n');

    passwords.forEach((password, index) => {
      setTimeout(() => {
        const result = password === correctPassword ? 'Success' : 'Failed';
        setResults((prevResults) => [
          ...prevResults,
          { password, result },
        ]);
        if (index === passwords.length - 1) {
          setIsBruteForcing(false);
        }
      }, index * 500); // Adding delay to simulate the process
    });
  };

  return (
    <div className="brute-force-login">
      <h2>Brute-Force Login Simulation</h2>
      <div>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={handleUsernameChange}
            disabled={isBruteForcing}
          />
        </label>
      </div>
      <div>
        <label>
          Password List (One per line):
          <textarea
            value={passwordList}
            onChange={handlePasswordListChange}
            disabled={isBruteForcing}
          ></textarea>
        </label>
      </div>
      <button onClick={startBruteForceAttack} disabled={isBruteForcing}>
        Start Brute-Force Attack
      </button>

      <div className="results">
        <h3>Results</h3>
        <ul>
          {results.map((result, index) => (
            <li key={index}>
              Password: <strong>{result.password}</strong> - Result: <strong>{result.result}</strong>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default BruteForceLogin;
