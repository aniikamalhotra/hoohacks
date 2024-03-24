import React from 'react';
import './ImageGallery.css'; // Styles for the image gallery

function ImageGallery() {
    // Array of image paths
    const images = [
        require('./images/mri-scan.jpg'),
        require('./images/mri-cardiac.jpg'),
        // Add more image paths as needed
    ];

    return (
        <div className="image-gallery">
            <div className="image-list">
                {images.map((image, index) => (
                    <img src={image} alt={`Image ${index + 1}`} key={index} />
                ))}
            </div>
        </div>
    );
}

export default ImageGallery;