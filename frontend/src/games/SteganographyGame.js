import React, { useState } from 'react';
import './SteganographyGame.css';

function SteganographyGame() {
  const [inputMessage, setInputMessage] = useState('');
  const [decodedMessage, setDecodedMessage] = useState('');
  const [imageData, setImageData] = useState(null);

  const handleInputChange = (e) => {
    setInputMessage(e.target.value);
  };

  const handleFileUpload = (event) => {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const reader = new FileReader();
    const image = new Image();

    reader.onload = function (e) {
      image.src = e.target.result;
      image.onload = function () {
        canvas.width = image.width;
        canvas.height = image.height;
        ctx.drawImage(image, 0, 0);
        setImageData(ctx.getImageData(0, 0, canvas.width, canvas.height));
      };
    };

    reader.readAsDataURL(event.target.files[0]);
  };

  const encodeMessage = () => {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    const data = imageData.data;
    let binaryText = '';

    for (let i = 0; i < inputMessage.length; i++) {
      let binaryChar = inputMessage.charCodeAt(i).toString(2).padStart(8, '0');
      binaryText += binaryChar;
    }

    binaryText += '00000000'; // Add null byte at the end

    if (binaryText.length > data.length / 4) {
      alert('Text is too long to encode in this image.');
      return;
    }

    for (let i = 0; i < binaryText.length; i++) {
      data[i * 4] = (data[i * 4] & 0b11111110) | parseInt(binaryText[i]);
    }

    ctx.putImageData(imageData, 0, 0);
    const outputImage = document.getElementById('outputImage');
    outputImage.src = canvas.toDataURL();
  };

  const decodeMessage = () => {
    const data = imageData.data;
    let binaryText = '';
    let decodedText = '';

    for (let i = 0; i < data.length; i += 4) {
      binaryText += (data[i] & 1).toString();
    }

    for (let i = 0; i < binaryText.length; i += 8) {
      let byte = binaryText.slice(i, i + 8);
      if (byte.length < 8) break;
      let charCode = parseInt(byte, 2);
      if (charCode === 0) break;
      decodedText += String.fromCharCode(charCode);
    }

    setDecodedMessage(decodedText);
  };

  return (
    <div className="steganography-game">
      <h2>Steganography Game</h2>
      <input type="file" id="upload" accept="image/*" onChange={handleFileUpload} /><br />
      <canvas id="canvas" style={{ display: 'none' }}></canvas><br />
      <textarea
        id="text"
        placeholder="Enter text to encode"
        value={inputMessage}
        onChange={handleInputChange}
      ></textarea><br />
      <button onClick={encodeMessage}>Encode Text</button>
      <button onClick={decodeMessage}>Decode Text</button>
      <p id="decodedText">{decodedMessage}</p>
      <img id="outputImage" alt="Output Image" />
    </div>
  );
}

export default SteganographyGame;
