import React from 'react';

function ServerCard({ server }) {
  return (
    <div className="server-card">
      <h3>{server.name}</h3>
      <p>IP: {server.ip}</p>
      <p>Status: {server.status || 'unknown'}</p>
      <p>Color: {server.color}</p>
      <p>Badges: {server.badges?.join(', ')}</p>
    </div>
  );
}

export default ServerCard;