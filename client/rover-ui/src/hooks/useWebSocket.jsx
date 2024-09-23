import { useEffect, useState } from "react";

const useWebSocket = (url) => {
  const [driveCommand, setDriveCommand] = useState(null);
  const [armCommand, setArmCommand] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const socket = new WebSocket(url);

    socket.onopen = () => {
      console.log("WebSocket connection established.");
    };

    socket.onmessage = (event) => {
      const data = event.data;
      console.log("Message received: ", data);

      // Update commands based on the prefix
      if (data.startsWith('D_')) {
        setDriveCommand(data);
      } else if (data.startsWith('A_')) {
        setArmCommand(data);
      }
    };

    socket.onerror = (error) => {
      console.error("WebSocket error: ", error);
      setError(error.message);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed.");
    };

    return () => {
      socket.close();
    };
  }, [url]);

  return { driveCommand, armCommand, error };
};

export default useWebSocket;