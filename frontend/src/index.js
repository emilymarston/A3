import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './index.css';
import Home from './pages/Home';
import Menu from './pages/Menu';
import Reservation from './pages/Reservation';
import Delivery from './pages/Delivery';
import Pickup from './pages/Pickup';
import Order from './pages/Order';
import Cart from './pages/Cart';
import MyAccount from './pages/MyAccount';
import MemberLogin from './pages/MemberLogin';
import CustomerSignUp from './pages/CustomerSignUp';
import OrderList from './pages/OrderList';
import OrderDetails from './pages/OrderDetails';
import RestaurantManagement from './pages/RestaurantManagement';
import StaffProfile from './pages/StaffProfile'; // Import StaffProfile
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/menu" element={<Menu />} />
        <Route path="/reservation" element={<Reservation />} />
        <Route path="/delivery" element={<Delivery />} />
        <Route path="/pickup" element={<Pickup />} />
        <Route path="/order" element={<Order />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/account" element={<MyAccount />} />
        <Route path="/member-login" element={<MemberLogin />} />
        <Route path="/customer-signup" element={<CustomerSignUp />} />
        <Route path="/order-list" element={<OrderList />} />
        <Route path="/order-details/:id" element={<OrderDetails />} />
        <Route path="/restaurant-management" element={<RestaurantManagement />} />
        <Route path="/staff-profile" element={<StaffProfile />} />  {/* Add this line */}
      </Routes>
    </Router>
  </React.StrictMode>
);

reportWebVitals();
