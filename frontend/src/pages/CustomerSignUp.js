import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './CustomerSignUp.css';
import logo from '../images/relaxing_koala_logo.png';
function CustomerSignUp() {
  const [formValues, setFormValues] = useState({
    username: '',
    password: '',
    address: '',
    cardNumber: '',
    cvv: '',
    expiryDate: ''
  });

  const [formErrors, setFormErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  };

  const validate = () => {
    let errors = {};
    if (!formValues.username) errors.username = 'Username is required';
    if (!formValues.password) errors.password = 'Password is required';
    if (!formValues.address) errors.address = 'Address is required';
    
    const cardNumber = formValues.cardNumber.replace(/\s+/g, '');
    if (!cardNumber) {
      errors.cardNumber = 'Card Number is required';
    } else if (!/^\d{16}$/.test(cardNumber)) {
      errors.cardNumber = 'Card Number must be 16 digits';
    }
    
    if (!formValues.cvv) {
      errors.cvv = 'CVV is required';
    } else if (!/^\d{3,4}$/.test(formValues.cvv)) {
      errors.cvv = 'CVV must be 3 or 4 digits';
    }
    if (!formValues.expiryDate) errors.expiryDate = 'Expiry Date is required';

    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      console.log('Form submitted successfully');
      // Submit form data to the server
    }
  };

  return (
    <div className="account-page">
      <header>
        <div className="logo-wrapper">
          <img src={logo} alt="Relaxing Koala Logo" />
        </div>
        <nav>
          <ul>
            <li><Link to="/">HOME</Link></li>
            <li><Link to="/menu">MENU</Link></li>
            <li><Link to="/reservation">RESERVATION</Link></li>
            <li><Link to="/contact">CONTACTS</Link></li>
            <li><Link to="/account">MY ACCOUNT</Link></li>
          </ul>
        </nav>
      </header>
      <main className="main-content">
        <div className="login-wrapper">
          <div className="login-box">
            <p>Customer Sign Up</p>
            <form onSubmit={handleSubmit}>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={formValues.username}
                onChange={handleChange}
                required
              />
              {formErrors.username && <span className="error">{formErrors.username}</span>}
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={formValues.password}
                onChange={handleChange}
                required
              />
              {formErrors.password && <span className="error">{formErrors.password}</span>}
              <input
                type="text"
                name="address"
                placeholder="Address"
                value={formValues.address}
                onChange={handleChange}
                required
              />
              {formErrors.address && <span className="error">{formErrors.address}</span>}
              <p>Payment Details</p>
              <input
                type="text"
                name="cardNumber"
                placeholder="Card Number"
                value={formValues.cardNumber}
                onChange={handleChange}
                required
              />
              {formErrors.cardNumber && <span className="error">{formErrors.cardNumber}</span>}
              <div className="cvv-expiry-wrapper">
                <input
                  type="text"
                  name="cvv"
                  placeholder="CVV"
                  value={formValues.cvv}
                  onChange={handleChange}
                  required
                />
                {formErrors.cvv && <span className="error">{formErrors.cvv}</span>}
                <input
                  type="date"
                  name="expiryDate"
                  placeholder="Expiry Date"
                  value={formValues.expiryDate}
                  onChange={handleChange}
                  required
                />
                {formErrors.expiryDate && <span className="error">{formErrors.expiryDate}</span>}
              </div>
              <button type="submit">SIGN UP</button>
            </form>
          </div>
        </div>
      </main>
      <footer className="footer">
        <div className="footer-content">
          <div>
            <p>CONNECT</p>
            <p>+6173647449595</p>
            <p>RelaxingKoala@gmail.com</p>
            <p>Eight Avenue, Glenferrie Road, 3122, VIC, AU</p>
          </div>
          <div>
            <p>CORPORATE</p>
            <Link to="/member-login">Member Portal</Link>
            <p>Staff Portal</p>
            <Link to="/customer-signup">Join a member</Link>
          </div>
          <div>
            <p>NEWSLETTER</p>
            <form>
              <input type="email" placeholder="Your Email" />
              <button type="submit">SUBSCRIBE</button>
            </form>
          </div>
        </div>
        <div className="social-media-icons">
          <a href="https://www.youtube.com" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-youtube"></i>
          </a>
          <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-twitter"></i>
          </a>
          <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-instagram"></i>
          </a>
          <a href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">
            <i className="fab fa-facebook"></i>
          </a>
        </div>
      </footer>
    </div>
  );
}

export default CustomerSignUp;
