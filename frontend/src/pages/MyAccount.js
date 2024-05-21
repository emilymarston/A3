import React from 'react';
import { Link } from 'react-router-dom';
import './MyAccount.css';
import logo from '../images/relaxing_koala_logo.png';
function MyAccount() {
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
            <p>STAFF LOGIN</p>
            <form>
              <input type="text" name="username" placeholder="Username" />
              <input type="password" name="password" placeholder="Password" />
              <a href="#" className="forgot-password">Forgot your password?</a>
              <button type="submit">LOGIN</button>
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

export default MyAccount;
