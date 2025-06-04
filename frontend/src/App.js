import React, { useState, useEffect } from 'react';
import ServerList from './components/ServerList';
import AddServerForm from './components/AddServerForm';
import { fetchServers, addServer } from './api/serverApi';

function App() {
  const [servers, setServers] = useState([]);
  const [filter, setFilter] = useState('');

  useEffect(() => {
    fetchServers().then(setServers);
  }, []);

  const handleAddServer = async (data) => {
    const newServer = await addServer(data);
    setServers((prev) => [...prev, newServer]);
  };

  const filteredServers = servers.filter((srv) =>
    srv.name.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div>
      <h1>Server Monitor</h1>
      <input
        type="text"
        placeholder="Filter by name"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
      />
      <ServerList servers={filteredServers} />
      <AddServerForm onAdd={handleAddServer} />
    </div>
  );
}

export default App;