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
              <h3>Button Mappings</h3>
              <p><strong>Button 0 (A)</strong>: Max PWM on both wrists</p>
              <p><strong>Button 1 (B)</strong>: Wrist down</p>
              <p><strong>Button 2 (X)</strong>: Wrist up</p>
              <p><strong>Button 3 (Y)</strong>: Min PWM on both wrists</p>
              <p><strong>Button 4 (Left Shoulder)</strong>: Rotate left</p>
              <p><strong>Button 5 (Right Shoulder)</strong>: Rotate right</p>
            </div>

            <div className="axes">
              <h3>Joystick Axes</h3>
              <p><strong>Left Joystick (Y-axis)</strong>: Left wheels</p>
              <p><strong>Right Joystick (Y-axis)</strong>: Right wheels</p>
            </div>

            <div className="triggers">
              <h3>Triggers</h3>
              <p><strong>Left Trigger (Axis 4)</strong>: Open claw</p>
              <p><strong>Right Trigger (Axis 5)</strong>: Close claw</p>
            </div>

            <div className="dpad">
              <h3>D-Pad Controls</h3>
              <p><strong>D-Pad Up</strong>: Elbow up</p>
              <p><strong>D-Pad Down</strong>: Elbow down</p>
              <p><strong>D-Pad Right</strong>: Gantry up</p>
              <p><strong>D-Pad Left</strong>: Gantry down</p>
            </div>
          </div>
        </div>
        <button className="close-btn" onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default ControlsModal;