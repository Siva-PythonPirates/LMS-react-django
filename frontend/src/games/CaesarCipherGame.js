// CaesarCipherGame.js

import React, { useState } from 'react';

function CaesarCipherGame() {
  const [inputText, setInputText] = useState('');
  const [shift, setShift] = useState(0);
  const [encodedText, setEncodedText] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleShiftChange = (e) => {
    setShift(parseInt(e.target.value, 10));
  };

  const encodeCaesarCipher = (text, shift) => {
    return text.replace(/[a-z]/gi, (char) => {
      const charCode = char.charCodeAt(0);
      const base = charCode >= 65 && charCode <= 90 ? 65 : 97;
      return String.fromCharCode(((charCode - base + shift) % 26) + base);
    });
  };

  const handleEncode = () => {
    const result = encodeCaesarCipher(inputText, shift);
    setEncodedText(result);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h2>Caesar Cipher Game</h2>
      <div>
        <label>
          Enter text:
          <input
            type="text"
            value={inputText}
            onChange={handleInputChange}
            style={{ marginLeft: '10px' }}
          />
        </label>
      </div>
      <div style={{ marginTop: '10px' }}>
        <label>
          Shift:
          <input
            type="number"
            value={shift}
            onChange={handleShiftChange}
            style={{ marginLeft: '10px', width: '60px' }}
          />
        </label>
      </div>
      <button onClick={handleEncode} style={{ marginTop: '10px' }}>
        Encode
      </button>
      {encodedText && (
        <div style={{ marginTop: '20px' }}>
          <h3>Encoded Text:</h3>
          <p>{encodedText}</p>
        </div>
      )}
    </div>
  );
}

export default CaesarCipherGame;
