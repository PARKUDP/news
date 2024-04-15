// VerticalList.jsx
import React from 'react';

const VerticalList = ({ items }) => {
  return (
    <div>
      {items.map((item, index) => (
        <div key={index}>{item}</div>
      ))}
    </div>
  );
};

export default VerticalList;
