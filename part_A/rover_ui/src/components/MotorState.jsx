import React, { useState, useEffect } from 'react';

const MotorState = ({ packets }) => {
  const [motorStates, setMotorStates] = useState({
    elbow: 128,
    wristRight: 128,
    wristLeft: 128,
    claw: 128,
    gantry: 128,
    shoulder: 128,
    wheels: [128, 128, 128, 128, 128, 128],
  });

  useEffect(() => {
    if (packets.length > 0) {
      const latestPacket = packets[packets.length - 1];
      
      // Split the packet by underscores and parse the command
      const packetParts = latestPacket.split("_");

      // Parse based on command type (A_ for arm, D_ for drive)
      if (latestPacket.startsWith("A_")) {
        const [, elbow, wristRight, wristLeft, claw, gantry, shoulder] = packetParts.map(Number);
        setMotorStates((prevState) => ({
          ...prevState,
          elbow,
          wristRight,
          wristLeft,
          claw,
          gantry,
          shoulder,
        }));
      } else if (latestPacket.startsWith("D_")) {
        const [, ...wheels] = packetParts.map(Number);
        setMotorStates((prevState) => ({
          ...prevState,
          wheels,
        }));
      }
    }
  }, [packets]);  // Re-run effect when new packets are received

  return (
    <div className="motor-states">
      <h2>Motor States</h2>
      <p>Elbow: {motorStates.elbow}</p>
      <p>Wrist Right: {motorStates.wristRight}</p>
      <p>Wrist Left: {motorStates.wristLeft}</p>
      <p>Claw: {motorStates.claw}</p>
      <p>Gantry: {motorStates.gantry}</p>
      <p>Shoulder: {motorStates.shoulder}</p>
      <p>Wheels: {motorStates.wheels.join(", ")}</p>
    </div>
  );
};

export default MotorState;