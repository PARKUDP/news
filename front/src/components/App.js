import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Yahoo from './Yahoo';
import Main from './Main';

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/news_yahoo" element={<Yahoo />} />
      </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
