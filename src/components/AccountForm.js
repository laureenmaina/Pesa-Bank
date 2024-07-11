import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const AccountForm = ({ onSubmit }) => {
    const validationSchema = Yup.object({
        account_number: Yup.string().required('Account number is required'),
        balance: Yup.number().required('Balance is required'),
        user_id: Yup.number().required('User ID is required')
    });

    return (
        <Formik
            initialValues={{ account_number: '', balance: '', user_id: '' }}
            validationSchema={validationSchema}
            onSubmit={onSubmit}
        >
            <Form>
                <div>
                    <label htmlFor="account_number">Account Number</label>
                    <Field name="account_number" type="text" />
                    <ErrorMessage name="account_number" component="div" />
                </div>
                <div>
                    <label htmlFor="balance">Balance</label>
                    <Field name="balance" type="number" />
                    <ErrorMessage name="balance" component="div" />
                </div>
                <div>
                    <label htmlFor="user_id">User ID</label>
                    <Field name="user_id" type="number" />
                    <ErrorMessage name="user_id" component="div" />
                </div>
                <button type="submit">Submit</button>
            </Form>
        </Formik>
    );
};

export default AccountForm;
