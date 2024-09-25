import React, { useState, useEffect } from 'react';
import '../ConnectionStatus.css';

const ConnectionStatus = () => {
  const [isControllerConnected, setIsControllerConnected] = useState(false);

  useEffect(() => {
    const checkControllerConnection = () => {
      const connected = navigator.getGamepads && navigator.getGamepads()[0] !== null;
      setIsControllerConnected(connected);
    };

    const intervalId = setInterval(checkControllerConnection, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="connection-status">
      <div className="status-item">
        <span>Controller Status:</span>
        <div
          className={`status-indicator ${isControllerConnected ? 'connected' : 'disconnected'}`}
        />
      </div>
    </div>
  );
};

export default ConnectionStatus;