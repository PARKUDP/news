// Yahoo.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../style/Yahoo.css';
import calendarIcon from './image/calendar_icon.png'; 
import titleIcon from './image/tittle.png';

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

  const handleCalendarClick = () => {
    alert("やまだです。")
  };
  // URLを開く関数
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
    <div>
      <header>
        <h1>
          <a href="/" className="title-Icon"><img src={titleIcon} alt="title"/></a>
        </h1>
        <button className="calendar-button" onClick={handleCalendarClick}>
          <img src={calendarIcon} alt="Calendar" />
        </button>
      </header>
      <main>
        <button onClick={fetchData}>reload</button>
        {loading ? (
          <p>Loading...</p>
        ) : error ? (
          <p>Error: {error}</p>
        ) : (
          renderData()
        )}
      </main>
    </div>
    
    
  );
};

export default Yahoo;