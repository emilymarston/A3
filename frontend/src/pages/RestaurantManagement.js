import React from 'react';
import { Link } from 'react-router-dom';
import './RestaurantManagement.css';
import logo from '../images/relaxing_koala_logo.png';
const mockOrders = [
    { id: '01', customerName: 'Alex', description: 'Flat White', table: 'A1', status: 'Pending', type: 'Dine-in', timeOrdered: '6:00 PM' }
    // Add more mock orders as needed
];

function RestaurantManagement() {
  return (
    <div className="restaurant-management-page">
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
        <div className="order-table-wrapper">
          <h2>Restaurant Management Portal</h2>
          <p>View orders from restaurant staffs.</p>
          <table className="order-table">
            <thead>
              <tr>
                <th>Order ID</th>
                <th>Name</th>
                <th>Order Description</th>
                <th>Table No.</th>
                <th>Order Status</th>
                <th>Order Type</th>
                <th>Time of ordered</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {mockOrders.map(order => (
                <tr key={order.id}>
                  <td><Link to={`/order-details/${order.id}`}>{order.id}</Link></td>
                  <td>{order.customerName}</td>
                  <td>{order.description}</td>
                  <td>{order.table}</td>
                  <td>{order.status}</td>
                  <td>{order.type}</td>
                  <td>{order.timeOrdered}</td>
                  <td>
                    <Link to={`/order-details/${order.id}`}>Edit Order</Link>
                    <br />
                    <Link to="/staff-profile">Staff Profile</Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
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
export default RestaurantManagement;