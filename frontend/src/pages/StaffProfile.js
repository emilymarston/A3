import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './StaffProfile.css';
import logo from '../images/relaxing_koala_logo.png';
function StaffProfile() {
    const navigate = useNavigate();
  
    const [editMode, setEditMode] = useState(false);
    const [profile, setProfile] = useState({
      name: 'Adam Schandler',
      role: 'Waitstaff',
      workShift: '3:00PM - 10:00PM (Thursday)',
      contactNumber: '+61456789346',
    });
  
    const handleChange = (e) => {
      const { name, value } = e.target;
      setProfile((prevProfile) => ({
        ...prevProfile,
        [name]: value,
      }));
    };
  
    const handleSaveChanges = () => {
      setEditMode(false);
      // Here you would usually make an API call to save the changes.
      console.log('Profile saved:', profile);
      navigate('/restaurant-management');
    };
  
    return (
      <div className="staff-profile-page">
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
          <div className="profile-wrapper">
            <div className="profile-box">
              <h2>Staff Profile</h2>
              <div className="profile-picture">
                <img src="https://via.placeholder.com/150" alt="Profile" />
              </div>
              {editMode ? (
                <>
                  <input 
                    type="text" 
                    name="name" 
                    value={profile.name} 
                    onChange={handleChange} 
                    placeholder="Name" 
                  />
                  <input 
                    type="text" 
                    name="role" 
                    value={profile.role} 
                    onChange={handleChange} 
                    placeholder="Role" 
                  />
                  <input 
                    type="text" 
                    name="workShift" 
                    value={profile.workShift} 
                    onChange={handleChange} 
                    placeholder="Work Shift" 
                  />
                  <input 
                    type="text" 
                    name="contactNumber" 
                    value={profile.contactNumber} 
                    onChange={handleChange} 
                    placeholder="Contact Number" 
                  />
                  <button onClick={handleSaveChanges}>Save Changes</button>
                </>
              ) : (
                <>
                  <h3>{profile.name}</h3>
                  <p>Role: {profile.role}</p>
                  <p>Work shift: {profile.workShift}</p>
                  <p>Contact Number: {profile.contactNumber}</p>
                  <button onClick={() => setEditMode(true)}>Edit Profile</button>
                </>
              )}
              <Link to="/restaurant-management" className="back-link">Back to Restaurant Management</Link>
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
  
  export default StaffProfile;