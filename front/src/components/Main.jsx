import React from 'react';
import '../style/main.css'; 
import calendarIcon from './image/calendar_icon.png'; 
import titleIcon from './image/tittle.png';

function App() {
  const sites = [
    { name: 'yahooニュースランキング', url: '/news_yahoo' },
    { name: 'CNNニュースランキング', url: 'https://www.cnn.com' }
  ];

  // カレンダーアイコンをクリックしたときの処理
  const handleCalendarClick = () => {
    alert("やまだです。")
  };


  return (
    <div className="App">
      <header>
        <h1>
          <a href="/" className="title-Icon"><img src={titleIcon} alt="title"/></a>
        </h1>
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
        <div className="footer-url">
          <div><a href="https://github.com/PARKUDP/news">GitHub:https://github.com/PARKUDP/news</a></div>
          <div><a href="https://your_render_url">Render:https://your_render_url</a></div>
          <div>お問合せ:your_email@gmail.com</div>
        </div>
      </footer>
    </div>
  );
}

export default App;
