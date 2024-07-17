import React, { useState } from 'react';
import './styles/Footer.css'; // Ensure you have a CSS file for the styles

function Footer() {
    const [contactInfo, setContactInfo] = useState('');

    const handleCallClick = () => {
        setContactInfo('+254-123-456790');
    };

    const handleEmailClick = () => {
        setContactInfo('Pesabank@gmail.com');
    };

    return (
        <footer className="footer">
            <p>For any inquiries contact us:                 
                <span className="contact-link" onClick={handleEmailClick}>Email &#128228; </span> 
                or 
                <span className="contact-link" onClick={handleCallClick}>Call &#128222;</span>
            </p>
            {contactInfo && <p className="contact-info-popup">{contactInfo}</p>}
            <hr></hr>
            <p>Developed by Group 2 &copy; 2024</p>
        </footer>
    );
}

export default Footer;
