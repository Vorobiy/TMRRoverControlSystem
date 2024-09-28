import React from 'react';

const ControlsModal = ({ isOpen, onClose }) => {
  if (!isOpen) return null; // If modal is not open, don't render it

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}> {/* Prevent closing when clicking inside */}
        <h2>Joystick Controls</h2>
        <div className="controls-diagram">
          <div className="joystick-diagram">
            <div className="buttons">
              <p>Buttons 1-4: Arm movements.</p>
            </div>
            <div className="axes">
              <p>Left Joystick (Y-axis): Left wheels.</p>
              <p>Right Joystick (Y-axis): Right wheels.</p>
            </div>
            <div className="triggers">
              <p>Left Trigger: Open claw.</p>
              <p>Right Trigger: Close claw.</p>
            </div>
            <div className="dpad">
              <p>D-Pad: Gantry and elbow control.</p>
            </div>
          </div>
        </div>
        <button className="close-btn" onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default ControlsModal;