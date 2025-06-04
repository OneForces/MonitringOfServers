import React, { useState } from 'react';

function AddServerForm({ onAdd }) {
  const [name, setName] = useState('');
  const [ip, setIp] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd({ name, ip });
    setName('');
    setIp('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Server</h2>
      <input
        type="text"
        placeholder="Server name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="IP address"
        value={ip}
        onChange={(e) => setIp(e.target.value)}
        required
      />
      <button type="submit">Add</button>
    </form>
  );
}

export default AddServerForm;