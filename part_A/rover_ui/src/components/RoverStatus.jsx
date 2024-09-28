import React, { useState, useEffect } from 'react';

const RoverStatus = () => {
  const [isRoverConnected, setIsRoverConnected] = useState(false);

  useEffect(() => {
    const checkRoverConnection = async () => {
      try {
        // Replace with actual API/WebSocket check logic
        const response = await fetch('http://localhost:8000/checkRoverStatus'); 
        const data = await response.json();
        
        // Assuming API returns a boolean in data.connected
        setIsRoverConnected(data.connected);
      } catch (error) {
        console.error('Error checking rover connection:', error);
        setIsRoverConnected(false); // set to false if there’s an error
      }
    };

    const intervalId = setInterval(checkRoverConnection, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="rover-status">
      <div className="status-item">
        <span>Rover Status:</span>
        <div
          className={`status-indicator ${isRoverConnected ? 'connected' : 'disconnected'}`}
        />
      </div>
    </div>
  );
};

export default RoverStatus;