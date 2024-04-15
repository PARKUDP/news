// App.jsx
import React from 'react';
import VerticalList from './VerticalList';

const App = () => {
  const items = ["Item 1", "Item 2", "Item 3"];
  
  return (
    <div>
      <h1>Todays NEWS List</h1>
      <VerticalList items={items} />
    </div>
  );
};

export default App;
