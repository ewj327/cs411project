import React, { useState } from 'react';
import './index.css';

// Function to get the CSRF token from the cookie
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const Demo = () => {
  const [image, setImage] = useState();
  const [im, setIm] = useState();
  const [output_image, setOutputImage] = useState();
  const [text, setText] = useState('');
  //const [imageFileName, setImageFileName] = useState('');
  const [isLoading, setIsLoading] = useState(false); // New state to track loading status
  const [isDragging, setIsDragging] = useState(false);
  //const [initialPosition, setInitialPosition] = useState({ x: 0, y: 0 });
  //const [currentPosition, setCurrentPosition] = useState({ x: 0, y: 0 });


  function handleChange(e) {
    setImage(e.target.files[0]);
    setIm(URL.createObjectURL(e.target.files[0]));
    setOutputImage(null); // Clear the output_image state when a new image is uploaded
    setText(''); // Clear the text state when a new image is uploaded
  }

  const newImage = () => {
    setIsLoading(true); // Set isLoading to true when new image is submitted

    const csrftoken = getCookie('csrftoken'); // Fetch the CSRF token from the cookie
    const headers = {
      'X-CSRFToken': csrftoken, // Include the CSRF token in the headers
    };

    const uploadData = new FormData();
    uploadData.append('image', image, image.name);

    // First, make the request to upload the image
    fetch('http://localhost:8000/images/', {
      method: 'POST',
      headers: headers, // Include the headers with the CSRF token
      body: uploadData,
    })
      .then((res) => {
        console.log(res);
        return res.json();
      })
      .then((data) => {
        // Assuming the response from the backend contains the evaluated image name
        console.log(image.name);

        const imageUrl = `http://localhost:8000/media/outputimages/outputimages/${image.name}`;
        setOutputImage(imageUrl);

        // Now make the request to fetch the calculation text
        console.log(image.name);

        fetch(`http://localhost:8000/media/calculations/calculations/${(image.name).split(".")[0] + ".txt"}`, {
          method: 'GET',
          headers: headers,
        })
          .then((res) => res.text())
          .then((data) => {
            setText(data); // Update the text state with the received content
          })
          .catch((error) => console.error(error));
      })
      .catch((error) => console.error(error))
      .finally(() => {
        setIsLoading(false); // Set isLoading back to false once image is loaded
      });
  };

  /*
  function zoom(id, zoomIn) {
    const maxScale = 2.0; // Maximum allowed scale value
    const minScale = 0.5; // Minimum allowed scale value
    const step = 0.1;     // Step size for zooming
  
    var myImg = document.getElementById(id);
    var currScale = 1.0;
  
    // Extract the current scale from the transform property
    var transformStyle = window.getComputedStyle(myImg).getPropertyValue('transform');
    if (transformStyle && transformStyle !== 'none') {
      var matrix = new DOMMatrixReadOnly(transformStyle);
      currScale = matrix.a;
    }
  
    // Calculate the new scale based on zoomIn and the current scale
    var newScale = zoomIn ? currScale + step : currScale - step;
  
    // Limit the scale to the defined boundaries
    newScale = Math.min(maxScale, Math.max(minScale, newScale));
  
    // Calculate the new position to keep the image centered on the original spot
    var offsetX = (1 - newScale) * myImg.offsetWidth / 2;
    var offsetY = (1 - newScale) * myImg.offsetHeight / 2;
  
    // Apply the new scale and position to the image
    myImg.style.transform = `scale(${newScale}) translate(${offsetX}px, ${offsetY}px)`;
  }
  
  */
  // handling zoom in & zoom out & drag
  const [scale, setScale] = useState(1);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleZoomIn = () => {
    setScale(scale + 0.1);
  };

  const handleZoomOut = () => {
    setScale(scale - 0.1);
  };

  const handleMouseDown = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleMouseMove = (e) => {
    if (isDragging) {
      setPosition({
        x: position.x + e.movementX / scale,
        y: position.y + e.movementY / scale,
      });
    }
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };


  return (
    <div className="demo">
      <div id="description">
        <p>Click on the button to upload the image that you want to evaluate.</p>
        <br />
        <p>
          &#40; Click on the uploaded image to resubmit &#41;
          <br />
          After submitting an image, click on <strong>'evaluate'</strong> button to assess biopsy adequacy.
        </p>
      </div>

      <div className="upload">
        <label>
          Upload image
          <input style={{ display: "none" }} type="file" onChange={handleChange} />
        </label>
      </div>

      <div id="zoombutton">
      
      <button id="b1" type="button" onClick={handleZoomIn}>Updated Image Zoom In</button>
      <button id="b2" type="button" onClick={handleZoomOut}>Updated Image Zoom Out</button>
      <button id="b3" type="button" onClick={handleZoomIn}>Evaluated Image Zoom In</button>
      <button id="b4" type="button" onClick={handleZoomOut}>Evaluated Image Zoom Out</button>

      </div>

      <div id="images">
  <div id="Inimg">
    <img id="inimg" src={im} alt="" style={{width: `${100 * scale}%`, transform: `translate(${position.x}px, ${position.y}px)`, cursor: isDragging ? 'grabbing' : 'grab',}} 
          onMouseDown={handleMouseDown}
          onMouseMove={handleMouseMove}
          onMouseUp={handleMouseUp}/>
  </div>
  <div id="Outimg">
    {isLoading ? (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
        <div className="loader"></div>
      </div>
    ) : (
      <>
        <img id="outimg" src={output_image} width="80%" alt="" />
        <div id="output-text">
          <pre>{text}</pre>
        </div>
      </>
    )}
  </div>
</div>

      <div id="segment">
        <button onClick={newImage}>Evaluate</button>
      </div>
    </div>
  );
}

export default Demo;