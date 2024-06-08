import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Yahoo from './Yahoo';
import HomePage from './Homepage';

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/news_yahoo" element={<Yahoo />} />
      </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
