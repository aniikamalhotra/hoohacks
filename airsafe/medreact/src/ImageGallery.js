import React from 'react';
import './ImageGallery.css'; // Styles for the image gallery
import AliceCarousel from "react-alice-carousel";
//import "react-alice-carousel/lib/alice-carousel.css";

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