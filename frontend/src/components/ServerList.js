import React from 'react';
import ServerCard from './ServerCard';

function ServerList({ servers }) {
  if (!servers.length) {
    return <p>No servers found.</p>;
  }

  return (
    <div className="server-list">
      {servers.map((server) => (
        <ServerCard key={server.id} server={server} />
      ))}
    </div>
  );
}

export default ServerList;