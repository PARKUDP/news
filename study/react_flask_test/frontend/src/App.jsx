import React, { useState, useEffect } from 'react';
import axios from 'axios';


const App = () => {
  const [jsonData, setJsonData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const result = await axios('http://127.0.0.1:5000/data');
      setJsonData(result.data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);
    }
  };

  const renderData = () => {
    if (jsonData) {
      return (
        <div>
          {Object.entries(jsonData).map(([key, value]) => (
            <div key={key}>
              <strong>{key}: </strong>
              {value}
            </div>
          ))}
        </div>
      );
    } else {
      return <p>Loading...</p>;
    }
  };
  
  
  
  

  return (
    <div>
      <h1>JSON Data</h1>
      <button>reload</button>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error: {error}</p>
      ) : (
        renderData()
      )}
    </div>
  );
};

export default App;
