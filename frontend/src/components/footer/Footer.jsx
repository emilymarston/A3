import React from 'react';
import { Box, Typography, Link } from '@mui/material';

const Footer = () => {
  return (
    <Box 
      id="footer"
      sx={{
        backgroundColor: '#f8f8f8',
        padding: '1rem',
        textAlign: 'center',
        position: 'relative',
        bottom: '0',
        marginTop: '1rem'
      }}
    >
      <Typography variant="body2" color="textSecondary" align="center">
        {'© '}
        {new Date().getFullYear()}
        {' Relaxing Koala. All rights reserved.'}
      </Typography>
      <Typography variant="body2" color="textSecondary" align="center">
        <Link href="#" color="inherit">
          Privacy Policy
        </Link>{' | '}
        <Link href="#" color="inherit">
          Terms of Service
        </Link>{' | '}
        <Link href="#" color="inherit">
          Contact Us
        </Link>
      </Typography>
    </Box>
  );
}

export default Footer;
