import React from 'react';

const PacketList = ({ driveCommand, armCommand }) => {
  return (
    <div className="packet-list">
      <h2>Latest Commands</h2>
      <p>Drive Command: {driveCommand || "No command sent"}</p>
      <p>Arm Command: {armCommand || "No command sent"}</p>
    </div>
  );
};

export default PacketList;