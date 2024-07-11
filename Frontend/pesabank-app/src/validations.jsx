import React from 'react';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';

// Validation schema
const UserSchema = Yup.object().shape({
  username: Yup.string()
    .min(3, 'Too Short!')
    .max(50, 'Too Long!')
    .required('Required'),
  email: Yup.string().email('Invalid email').required('Required'),
  phone_number: Yup.number()
    .typeError('Must be a number')
    .required('Required'),
});

function UserForm() {
  return (
    <div>
      <h1>Create User</h1>
      <Formik
        initialValues={{
          username: '',
          email: '',
          phone_number: '',
        }}
        validationSchema={UserSchema}
        onSubmit={(values) => {
    
          console.log(values);
        }}
      >
        {({ errors, touched }) => (
          <Form>
            <div>
              <label htmlFor="username">Username</label>
              <Field name="username" type="text" />
              <ErrorMessage name="username" className="error" />
            </div>

            <div>
              <label htmlFor="email">Email</label>
              <Field name="email" type="email" />
              <ErrorMessage name="email" className="error" />
            </div>

            <div>
              <label htmlFor="phone_number">Phone Number</label>
              <Field name="phone_number" type="text" />
              <ErrorMessage name="phone_number" className="error" />
            </div>

            <button type="submit">Submit</button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default UserForm;