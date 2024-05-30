import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Box, AppBar, Toolbar, Container, Avatar, Typography, Button, Menu, MenuItem } from '@mui/material';

const pages = [
 {label: 'Home', id: '/'},
 {label: 'Menu', id: 'menu'}, 
 {label: 'Reservation', id: 'reservation'},
 {label:'Contact', id: 'footer' },
 {
    label: 'My Account', 
    id: 'my-account',
    handler: (event, setAnchorEl) => {
      setAnchorEl(event.currentTarget);
    }
  }
];
const credentials = [
  {label: 'Staff Login', id: 'stafflogin'},
  {label: 'Customer Login', id: 'customerlogin'}
];

const NavBar = () => {
  const [anchorEl, setAnchorEl] = useState(null);
  const navigate = useNavigate();

  // determines the action to take when a page is clicked. 
  // If the page has a 'handler', it calls the handler, otherwise,
  // it scrolls to the corresponding section
  const handleNavClick = (id, event) => {
    event.preventDefault(); // Prevent the default link behavior
    const page = pages.find((page) => page.id === id);
    if (page && page.handler) {
      page.handler(event, setAnchorEl);
    } 
    else {
      if (window.location.pathname !== '/')
      {
        navigate('/');
      }
        // give a specific timer before scrolling to the specific section
        setTimeout(() => {
        const element = document.getElementById(id);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
        }, 100)
    }
  };


  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="static" sx={{ backgroundColor: 'transparent'}}>
      <Container maxWidth="xl">
        <Toolbar>
          <Link to="/" style={{ textDecoration : 'none'}}>
            <Avatar 
                alt="Logo" 
                src={`logo.png`} 
                sx={{ width: '6rem', paddingTop: '1rem'}}
            />
            <Typography
              sx={{ 
                color: 'black',
                fontSize: '0.7rem',
                fontFamily: 'Knewave',
                paddingBottom: '1rem'
              }}
            >
              RELAXING KOALA
            </Typography>
          </Link>
          <Box sx={{ flexGrow: 1, display: "flex" }} />
            {pages.map((page) => (
              <Link 
               key={page.label}
               to={page.id}
               style={{ marginRight: '1rem', cursor: 'pointer', textDecoration: 'none', color:'black', fontWeight: '600' }}
               onClick={(event) => handleNavClick(page.id, event)}
              >
               {page.label}
            </Link>
            ))}

        </Toolbar>
      </Container>
      <Menu
      id="login-details"
      anchorEl={anchorEl}
      keepMounted open={Boolean(anchorEl)}
      onClose={handleClose}
      >
        {credentials.map((credential) =>(
          <MenuItem key={credential.id} >
            <Link to={credential.id} style={{ textDecoration: 'none', color: 'inherit'}}>
              {credential.label}
            </Link>
          </MenuItem>
        ))}

      </Menu>
    </AppBar>
  );
}

export default NavBar;
