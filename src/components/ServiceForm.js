import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const ServiceForm = ({ onSubmit }) => {
    const validationSchema = Yup.object({
        name: Yup.string().required('Service name is required'),
        description: Yup.string().required('Description is required')
    });

    return (
        <Formik
            initialValues={{ name: '', description: '' }}
            validationSchema={validationSchema}
            onSubmit={onSubmit}
        >
            <Form>
                <div>
                    <label htmlFor="name">Service Name</label>
                    <Field name="name" type="text" />
                    <ErrorMessage name="name" component="div" />
                </div>
                <div>
                    <label htmlFor="description">Description</label>
                    <Field name="description" type="text" />
                    <ErrorMessage name="description" component="div" />
                </div>
                <button type="submit">Submit</button>
            </Form>
        </Formik>
    );
};

export default ServiceForm;
