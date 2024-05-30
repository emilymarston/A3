import React, { useState } from 'react';
import { TextField, Button, Typography } from '@mui/material';

const Reservation = () => {
  const [formData, setFormData] = useState({
    name: '',
    phoneNumber: '',
    date: '',
    time: '',
    numbOfPeople: '',
    specialRequests: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can perform any actions you need here, such as sending the form data to a server
    console.log('Form submitted:', formData);
  };

  return (
    <div id="reservation">
      <Typography variant="h4" sx={{ fontWeight: 'bold', padding:'2rem'}}>BOOK A TABLE</Typography>
      <form style={{ display: 'flex', flexDirection: 'column', gap: '1rem', alignItems: 'center'}} onSubmit={handleSubmit}>
        <TextField 
          label="Name"
          variant="outlined" 
          name="name" 
          InputLabelProps={{
            shrink: true,
          }}
          value={formData.name} 
          onChange={handleChange} 
          sx={{ width: '500px' }} 
          required 
        />

        <TextField 
          label="Phone Number"
          variant="outlined" 
          name="phoneNumber" 
          type="tel"
          InputLabelProps={{
            shrink: true,
          }}
          value={formData.phoneNumber} 
          onChange={handleChange} 
          sx={{ width: '500px' }} 
          required 
        />

        <TextField 
          label="Date"
          variant="outlined" 
          name="date" 
          type="date"
          InputLabelProps={{
            shrink: true,
          }}
          value={formData.date} 
          onChange={handleChange} 
          sx={{ width: '500px' }} 
          required 
        />

        <TextField 
          label="Time"
          type="time"
          variant="outlined" 
          name="time" 
          InputLabelProps={{
            shrink: true,
          }}
          value={formData.time} 
          onChange={handleChange} 
          sx={{ width: '500px' }} 
          required 
        />

        <TextField 
          label="Number of People"
          variant="outlined" 
          name="numbOfPeople" 
          InputLabelProps={{
            shrink: true,
          }}
          value={formData.numbOfPeople} 
          onChange={handleChange} 
          sx={{ width: '500px' }} 
          required 
        />

        <TextField 
          label="Special Requests"
          variant="outlined" 
          name="specialRequests" 
          InputLabelProps={{
            shrink: true,
          }}
          value={formData.specialRequests} 
          onChange={handleChange} 
          sx={{ width: '500px' }} 
          required 
        />
        <Button 
          type="submit"   
          variant="contained" 
          sx={{ width: '500px', 
          color: '#FFFFFF', 
          fontWeight: 'bold', 
          padding: '1rem',
          marginBottom: '1rem'
          }}
        >
          Submit
        </Button>
      </form>
    </div>
  );
}

export default Reservation;
