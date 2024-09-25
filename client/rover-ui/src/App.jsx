import React from 'react';
import './App.css'; // Ensure this line is present
import useWebSocket from './hooks/useWebSocket';
import PacketList from './components/PacketList';
import ConnectionStatus from './components/ConnectionStatus'; // Import your ConnectionStatus component

function App() {
  const { driveCommand, armCommand } = useWebSocket('ws://localhost:8000');

  return (
    <div className="App">
      <header className="header">
        <div className="logo">
          <img src="./src/assets/TMR_White_Text_Transparent_No_Subtitle.jpg" alt="Logo" />
        </div>
        <nav className="nav-links">
          <a href="#home">Home</a>
          <a href="#controls">Controls</a>
        </nav>
      </header>
      <div className="box">
        <h1>Rover Control System</h1>
        <PacketList driveCommand={driveCommand} armCommand={armCommand} />
        
        {/* Add the ConnectionStatus component here */}
        <ConnectionStatus />
      </div>
    </div>
  );
}

export default App;