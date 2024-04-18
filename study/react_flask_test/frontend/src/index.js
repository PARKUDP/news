// frontend/src/index.js
import React, { useState } from 'react';
import ReactDOM from 'react-dom';

function App() {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async () => {
    const response = await fetch(' http://127.0.0.1:5000/api/hello', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name })
    });
    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <div>
      <h1>React Frontend with Flask Backend</h1>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <button onClick={handleSubmit}>reload</button>
      {message && <p>{message}</p>}
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
