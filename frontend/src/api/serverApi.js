const API_URL = '/api/servers/';

export async function fetchServers() {
  const res = await fetch(API_URL);
  if (!res.ok) {
    throw new Error('Failed to fetch servers');
  }
  return res.json();
}

export async function addServer(data) {
  const res = await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    throw new Error('Failed to add server');
  }
  return res.json();
}