import React from 'react';
import './App.css'; // Ensure this line is present
import useWebSocket from './hooks/useWebSocket';
import PacketList from './components/PacketList';

function App() {
  const { driveCommand, armCommand } = useWebSocket('ws://localhost:8000');

  return (
    <div className="App">
      <header className="header">
        <div className="logo"><img src ="./src/assets/TMR_White_Text_Transparent_No_Subtitle.jpg"></img></div>
        <nav className="nav-links">
          <a href="#home">Home</a>
          <a href="#controls">Controls</a>
        </nav>
      </header>
      <div className = "box">
      <h1>Rover Control System</h1>
      <PacketList driveCommand={driveCommand} armCommand={armCommand} />
      </div>
    </div>
  );
}

export default App;