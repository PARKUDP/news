import React from 'react';
import Layout from './Layout';

const HomePage = () => {
  const sites = [
    { name: 'yahooニュースランキング', url: '/news_yahoo' },
    { name: 'CNNニュースランキング', url: '/news_cnn' }
  ];

  return (
    <Layout>
      <div className="section-title">主要サイト</div>
      <div className="site-list">
        {sites.map((site, index) => (
          <div key={index} className="site-item" onClick={() => window.location.href = site.url}>
            {site.name}
          </div>
        ))}
      </div>
    </Layout>
  );
};

export default HomePage;
