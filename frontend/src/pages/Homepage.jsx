import React from 'react';
import { Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';
import Reservation from './Reservation'; // Import the Reservation component

const Homepage = () => {
  return (
    <div style={{ position: 'relative', width: '100%', height: 'auto' }}>
      <img 
        src="/image1.jpg" alt="Description of the image" 
        style={{ width: '100%', height: 'auto' }} 
      />
      <div id="services" style={{position: 'absolute', top: '0', display: 'flex', justifyContent: 'center', width: '100%', gap: '1rem'}}>
        <Link to="/deliverypage">
          <Button 
            sx={{
              backgroundColor: "rgba(217, 217, 217, 0.8)", 
              color: '#FFFFFF', 
              fontWeight: 'bold', 
              width: '12rem', 
              fontSize: '1.5rem',
            }}
          >
            DELIVERY
          </Button>
        </Link>
        <Link to="/pickup"> 
          <Button 
            sx={{
              backgroundColor: "rgba(217, 217, 217, 0.8)", 
              color: '#FFFFFF', 
              fontWeight: 'bold', 
              width: '12rem', 
              fontSize: '1.5rem',
            }}          
          >
            PICK-UP
          </Button>
        </Link>
      </div>
      <div 
        style={{
          position: 'absolute',
          top: '5%',
          width: '100%',
          height: '400px',
          backgroundColor: 'rgba(255, 255, 255, 0.6)'
        }}
      >
        <Typography variant="h3" align="left" color="#000000" sx={{ paddingTop: '8rem', paddingLeft: '2rem', fontWeight: 'bold'}}>
          WELCOME TO RELAXING KOALA 
        </Typography>
        <Typography variant="h3" align="left" color="#000000" sx={{ paddingTop: '1rem', paddingLeft: '2rem', fontWeight: 'bold'}}>
          - WHERE FLAVOURS MEET FRIENDS
        </Typography>
      </div>
      <div id="menu">
        <Typography variant="h4" sx={{ fontWeight: 'bold', padding:'2rem'}}>MENU</Typography>
      
        <img 
          src="/Menu.jpg" alt="Description of the image" 
          style={{ width: '100%', height: 'auto' }} 
        />
      </div>
      <Reservation />
    </div>
  );
}

export default Homepage;
