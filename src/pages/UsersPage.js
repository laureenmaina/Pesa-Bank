import React, { useState, useEffect } from 'react';
import UserForm from '../components/UserForm';

const Users = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('/users')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    const handleCreateUser = (values) => {
        fetch('/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(values)
        })
        .then(response => response.json())
        .then(data => setUsers([...users, data]));
    };

    return (
        <div>
            <h1>Users</h1>
            <UserForm onSubmit={handleCreateUser} />
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.username} - {user.email}</li>
                ))}
            </ul>
        </div>
    );
};

export default Users;
