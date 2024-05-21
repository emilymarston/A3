import React, { useState, useEffect } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import './OrderDetails.css';
import logo from '../images/relaxing_koala_logo.png';
const mockOrder = {
    id: '01',
    name: 'Alex',
    timeOfOrder: '6:00 PM',
    description: 'Flat White',
    status: 'Pending',
    type: 'Dine-In',
    table: 'A1',
    updatedBy: 'Adam Schandler',
    updatedTime: '6:00 PM'
  };
  
  function OrderDetails() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [order, setOrder] = useState(null);
  
    useEffect(() => {
      // Fetch the order by ID (mock for now)
      setOrder(mockOrder);
    }, [id]);
  
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setOrder((prevOrder) => ({
        ...prevOrder,
        [name]: value,
      }));
    };
  
    const handleSaveChanges = (e) => {
      e.preventDefault();
      // Here you would handle saving changes to the backend
      console.log('Order updated:', order);
      // Navigate back to the Restaurant Management page
      navigate('/restaurant-management');
    };
  
    if (!order) return <div>Loading...</div>;
  
    return (
      <div className="order-details-page">
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
          <div className="order-details-wrapper">
            <h2>Order Details</h2>
            <p>Updated by: {order.updatedBy} - Time updated: {order.updatedTime}</p>
            <form className="order-details-form" onSubmit={handleSaveChanges}>
              <div className="form-row">
                <label>Customer Name:</label>
                <input type="text" name="name" value={order.name} readOnly />
              </div>
              <div className="form-row">
                <label>Order ID:</label>
                <input type="text" name="id" value={order.id} readOnly />
              </div>
              <div className="form-row">
                <label>Time of Ordered:</label>
                <input type="text" name="timeOfOrder" value={order.timeOfOrder} readOnly />
              </div>
              <div className="form-row">
                <label>Order Description:</label>
                <input type="text" name="description" value={order.description} onChange={handleInputChange} />
              </div>
              <div className="form-row">
                <label>Order Status:</label>
                <select name="status" value={order.status} onChange={handleInputChange}>
                  <option value="Pending">Pending</option>
                  <option value="Completed">Completed</option>
                </select>
              </div>
              <div className="form-row">
                <label>Order Type:</label>
                <select name="type" value={order.type} onChange={handleInputChange}>
                  <option value="Dine-In">Dine-In</option>
                  <option value="Takeaway">Takeaway</option>
                </select>
              </div>
              <div className="form-row">
                <label>Table Number:</label>
                <input type="text" name="table" value={order.table} onChange={handleInputChange} />
              </div>
              <button type="submit">Save Changes</button>
            </form>
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
  
  export default OrderDetails;