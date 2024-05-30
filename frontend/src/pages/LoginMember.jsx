import React from 'react';
import { Button, Paper, TextField, Typography } from '@mui/material';

const CustomerLogin = () => {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
      <Paper elevation={2} sx={{ padding: '2rem', mt: '2rem', width: '40%' }}>
        <Typography variant='h5' textAlign='center' sx={{ fontFamily: 'Verdana, sans-serif', marginBottom: '1rem' }}>Customer Login</Typography>
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
          <Button variant='contained' fullWidth> LOGIN </Button>
        </form>
      </Paper>
    </div>
  );
};

export default CustomerLogin;
