import React, { useState, useEffect } from 'react';
import ServiceForm from '../components/ServiceForm';

const Services = () => {
    const [services, setServices] = useState([]);

    useEffect(() => {
        fetch('/services')
            .then(response => response.json())
            .then(data => setServices(data));
    }, []);

    const handleAddService = (values, { resetForm }) => {
        fetch('/services', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        })
        .then(response => response.json())
        .then(data => {
            setServices([...services, data]);
            resetForm();
        });
    };

    return (
        <div>
            <h1>Services</h1>
            <ServiceForm onSubmit={handleAddService} />
            <ul>
                {services.map(service => (
                    <li key={service.id}>{service.name} - Description: {service.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default Services;
