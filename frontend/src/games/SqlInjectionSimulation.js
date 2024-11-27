import React, { useState } from 'react';

function SqlInjectionSimulation() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [result, setResult] = useState('');
  const [attackLog, setAttackLog] = useState([]);

  const handleLogin = () => {
    // Simulate a vulnerable SQL query
    const simulatedDatabase = {
      user: 'admin',
      pass: 'password123',
    };

    const sqlQuery = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

    // Check for SQL Injection
    let logEntry = `Attempted SQL Query: ${sqlQuery}\n`;

    if (sqlQuery.includes("' OR '1'='1") || sqlQuery.includes("' OR 1=1")) {
      setResult('Access Granted! (SQL Injection Detected)');
      logEntry += 'Result: Access Granted! (SQL Injection Detected)\n';
    } else if (username === simulatedDatabase.user && password === simulatedDatabase.pass) {
      setResult('Access Granted! (Correct Credentials)');
      logEntry += 'Result: Access Granted! (Correct Credentials)\n';
    } else {
      setResult('Access Denied! (Invalid Credentials)');
      logEntry += 'Result: Access Denied! (Invalid Credentials)\n';
    }

    setAttackLog([...attackLog, logEntry]);
  };

  return (
    <div>
      <h2>SQL Injection Simulation</h2>
      <div style={{ marginBottom: '10px' }}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            style={{ marginLeft: '10px' }}
          />
        </label>
      </div>
      <div style={{ marginBottom: '10px' }}>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{ marginLeft: '10px' }}
          />
        </label>
      </div>
      <button onClick={handleLogin}>Attempt Login</button>
      <div style={{ marginTop: '20px' }}>
        <h3>Result:</h3>
        <p>{result}</p>
      </div>
      <div style={{ marginTop: '20px' }}>
        <h3>Attack Log:</h3>
        <pre>{attackLog.join('\n')}</pre>
      </div>
    </div>
  );
}

export default SqlInjectionSimulation;
