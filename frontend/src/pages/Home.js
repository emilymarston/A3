import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <header>
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/menu">Menu</Link></li>
            <li><Link to="/reservation">Reservation</Link></li>
            <li><Link to="/delivery">Delivery</Link></li>
            <li><Link to="/pickup">Pickup</Link></li>
            <li><Link to="/order">Order</Link></li>
            <li><Link to="/cart">Cart</Link></li>
            <li><Link to="/account">My Account</Link></li>
          </ul>
        </nav>
      </header>
      <main>
        <h1>Home Page</h1>
      </main>
    </div>
  );
}

export default Home;
