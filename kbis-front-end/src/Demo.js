import React, { useState } from 'react';
import before from './5before.jpg';
import after from './5after.png';

const Demo = () => {
    const [image, setImage] = useState([]);
    
    const handleChange = e => {
        if (e.target.files.length) {
          setImage({
            preview: URL.createObjectURL(e.target.files[0]),
            raw: e.target.files[0]
          });
        }
      };
    
    const handleUpload = async e => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", image.raw);
    
        await fetch("YOUR_URL", {
          method: "POST",
          headers: {
            "Content-Type": "multipart/form-data"
          },
          body: formData
        });
      };

    return (
        <div className="demo">
            <div id="description">
              <p>Click on the button to upload the image that you want to segment.</p>
              <br />
              <p> &#40; Click on the uploaded image to resubmit &#41;
                <br />
                After submitting an image, click on <strong>'segment'</strong> button to get the segmented image
              </p>
            </div>
            <label htmlFor="upload-button">
                {image.preview ? (
                  <div id="Uimage">
                    <img src={image.preview} alt="dummy" width="60%" height="" />
                  </div>
                ) : (
                <>
                    <span className="fa-stack fa-2x mt-3 mb-2">
                        <i className="fas fa-circle fa-stack-2x" />
                        <i className="fas fa-store fa-stack-1x fa-inverse" />
                    </span>
                <h5 className="upload">Upload Image</h5>
            </>
        )}
            </label>
            <input
                type="file"
                id="upload-button"
                style={{ display: "none" }}
                onChange={handleChange}
            />
            <div id="segment">
              <button onClick={handleUpload}>Segment</button>
            </div>
            {/* <div id="sample">
              <p>Sample: </p>
              <div id="Simage">
              <img src={before} alt="kidney before segmentation" />
              <img src={after} alt="kidney after segmentation" />
              <br />
              <p style={{display: 'inline', padding: '0 8vw',}}>kidney before segmentation</p>
              <p style={{display: 'inline', padding: '0 8vw',}}>kidney after segmentation</p>
              </div>
            </div> */}
        </div>
    );
}
 
export default Demo;