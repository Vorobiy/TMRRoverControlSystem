import React from 'react';

const ErrorDisplay = ({ error }) => {
  return (
    <div className="error-message">
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
};

export default ErrorDisplay;