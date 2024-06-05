import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Yahoo from './Yahoo';
import Main from './Main';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/main" element={<Main />} />
        <Route path="/news_yahoo" element={<Yahoo />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
