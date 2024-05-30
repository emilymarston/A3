import React from 'react';
import { Button, Paper, TextField, Typography } from '@mui/material';
import { Link } from 'react-router-dom';

const StaffLogin = () => {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
      <Paper elevation={2} sx={{ padding: '2rem', mt: '2rem', width: '40%' }}>
        <Typography variant='h5' textAlign='center' sx={{ fontFamily: 'Verdana, sans-serif', marginBottom: '1rem' }}>Staff Login</Typography>
        <form style={{ display: 'flex', flexDirection: 'column', gap: '1rem', alignItems: 'center' }}>
          <TextField
            label='Username'
            fullWidth
          />
          <TextField
            label='Password'
            type="password"
            fullWidth
          />
          <Link to="/managementportal">
            <Button variant='contained' fullWidth> LOGIN </Button>
          </Link>
        </form>
      </Paper>
    </div>
  );
};

export default StaffLogin;
