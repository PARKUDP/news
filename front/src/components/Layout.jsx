import React, { useState } from "react";
import "../style/main.css";
import calendarIcon from "./image/calendar_icon.png";
import titleIcon from "./image/tittle.png";
import arrowUpIcon from "./image/arrow_up_icon.png";
import arrowDownIcon from "./image/arrow_down_icon.png";

const Layout = ({ children }) => {
  const [footerVisible, setFooterVisible] = useState(true);

  const toggleFooter = () => {
    setFooterVisible(!footerVisible);
  };

  return (
    <div className="App">
      <header>
        <h1>
          <a href="/" className="title-Icon">
            <img src={titleIcon} alt="title" />
          </a>
        </h1>
        <button
          className="calendar-button"
          onClick={() => alert("やまだです。")}
        >
          <img src={calendarIcon} alt="Calendar" />
        </button>
      </header>
      <main>{children}</main>
      <footer className={footerVisible ? "footer-visible" : "footer-hidden"}>
        <div className="footer-url">
          <div>
            <a href="https://github.com/PARKUDP/news">
              GitHub:https://github.com/PARKUDP/news
            </a>
          </div>
          <div>
            <a href="https://your_render_url">Render:https://your_render_url</a>
          </div>
          <div>お問合せ:your_email@gmail.com</div>
        </div>
      </footer>
      <button className="toggle-footer-button" onClick={toggleFooter}>
        <img
          src={footerVisible ? arrowDownIcon : arrowUpIcon}
          alt="Toggle Footer"
        />
      </button>
    </div>
  );
};

export default Layout;
