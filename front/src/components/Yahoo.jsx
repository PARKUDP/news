import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Layout from './Layout'; 
import '../style/Yahoo.css';

const Yahoo = () => {
  const [jsonData, setJsonData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await axios('http://127.0.0.1:5000/news_yahoo');
      setJsonData(result.data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);
    }
  };

  const openLink = (e) => {
    window.open(e.target.value, '_blank');
  };

  const renderData = () => {
    if (jsonData) {
      return (
        <div>
          {Object.entries(jsonData).map(([key, value]) => (
            <div key={key}>
              <strong>{key}: </strong>
              <button onClick={openLink} value={value} className="arrow">記事へ</button>
            </div>
          ))}
        </div>
      );
    } else {
      return <p>Loading...</p>;
    }
  };

  return (
    <Layout>
      <button onClick={fetchData}>reload</button>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>Error: {error}</p>
      ) : (
        renderData()
      )}
    </Layout>
  );
};

export default Yahoo;
