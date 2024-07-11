import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const TransactionForm = ({ onSubmit }) => {
    const validationSchema = Yup.object({
        amount: Yup.number().required('Amount is required'),
        account_id: Yup.number().required('Account ID is required')
    });

    return (
        <Formik
            initialValues={{ amount: '', account_id: '' }}
            validationSchema={validationSchema}
            onSubmit={onSubmit}
        >
            <Form>
                <div>
                    <label htmlFor="amount">Amount</label>
                    <Field name="amount" type="number" />
                    <ErrorMessage name="amount" component="div" />
                </div>
                <div>
                    <label htmlFor="account_id">Account ID</label>
                    <Field name="account_id" type="number" />
                    <ErrorMessage name="account_id" component="div" />
                </div>
                <button type="submit">Submit</button>
            </Form>
        </Formik>
    );
};

export default TransactionForm;
