import React from 'react';
import '../style/main.css'; 
import calendarIcon from './image/calendar_icon.png'; 

function App() {
  const sites = [
    { name: 'yahooニュース', url: '/news_yahoo' },
    { name: 'CNNニュース', url: 'https://www.cnn.com' }
  ];

  const handleCalendarClick = () => {
    alert('カレンダーボタンがクリックされました');
  };

  return (
    <div className="App">
      <header>
        Todays News
        <button className="calendar-button" onClick={handleCalendarClick}>
          <img src={calendarIcon} alt="Calendar" />
        </button>
      </header>
      <main>
        <div className="section-title">主要サイト</div>
        <div className="site-list">
          {sites.map((site, index) => (
            <div key={index} className="site-item" onClick={() => window.location.href = site.url}>
              {site.name}
            </div>
          ))}
        </div>
      </main>
      <footer>
        <div>Github: <a href="https://github.com/PARKUDP/news">https://github.com/PARKUDP/news</a></div>
        <div>Render: <a href="https://your_render_url">https://your_render_url</a></div>
        <div>お問合せ: your_email@gmail.com</div>
      </footer>
    </div>
  );
}

export default App;
