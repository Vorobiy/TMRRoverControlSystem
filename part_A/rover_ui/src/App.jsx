import React, { useState } from 'react';
import './App.css';
import useWebSocket from './hooks/useWebSocket';
import PacketList from './components/PacketList';
import ConnectionStatus from './components/ConnectionStatus';
import RoverStatus from './components/RoverStatus';
import ControlsModal from './components/ControlsModal'; // Import the modal component

function App() {
  const { driveCommand, armCommand } = useWebSocket('ws://localhost:8000');
  const [isModalOpen, setIsModalOpen] = useState(false); // Modal open state

  return (
    <div className="App">
      <header className="header">
        <div className="logo">
          <img src="./src/assets/TMR_White_Text_Transparent_No_Subtitle.jpg" alt="Logo" />
        </div>
        <nav className="nav-links">
          <a href="#home">Home</a>
          <a href="#controls" onClick={() => setIsModalOpen(true)}>Controls</a> {/* Trigger modal */}
        </nav>
      </header>
      <div className="box">
        <h1>Rover Control System</h1>
        <PacketList driveCommand={driveCommand} armCommand={armCommand} />
        
        <ConnectionStatus />

        <RoverStatus />
      </div>

      {/* Controls Modal */}
      <ControlsModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </div>
  );
}

export default App;