import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [accountInfo, setAccountInfo] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:5000/api/account")
      .then(response => setAccountInfo(response.data))
      .catch(error => console.error("Error fetching account data:", error));
  }, []);

  return (
    <div>
      <h1>MEXC Trading Dashboard</h1>
      {accountInfo ? (
        <pre>{JSON.stringify(accountInfo, null, 2)}</pre>
      ) : (
        <p>Loading account data...</p>
      )}
    </div>
  );
}

export default App;
