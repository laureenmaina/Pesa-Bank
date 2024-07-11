import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const UserForm = ({ onSubmit }) => {
    const validationSchema = Yup.object({
        username: Yup.string().required('Username is required'),
        email: Yup.string().email('Invalid email address').required('Email is required')
    });

    return (
        <Formik
            initialValues={{ username: '', email: '' }}
            validationSchema={validationSchema}
            onSubmit={onSubmit}
        >
            <Form>
                <div>
                    <label htmlFor="username">Username</label>
                    <Field name="username" type="text" />
                    <ErrorMessage name="username" component="div" />
                </div>
                <div>
                    <label htmlFor="email">Email</label>
                    <Field name="email" type="email" />
                    <ErrorMessage name="email" component="div" />
                </div>
                <button type="submit">Submit</button>
            </Form>
        </Formik>
    );
};

export default UserForm;
