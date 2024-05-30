import React, { useState } from 'react'
import { Box, Paper, Typography, TextField, Button, FormControl, FormLabel, RadioGroup, FormControlLabel, Radio } from '@mui/material';
import { useNavigate } from 'react-router-dom'

const styles = {
    button: {
        fontWeight: 'bold', 
        width: '12rem', 
        fontSize: '1.5rem',
        marginRight: '0.5rem',
        marginBottom:'1rem'
    },
    selectedButton: {
        fontWeight: 'bold',
        width: '12rem',
        fontSize: '1.5rem',
        marginRight: '0.5rem',
        marginBottom: '1rem',
        backgroundColor: '#4caf50',
        color: 'white'
    }
}
const CustomerForm = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        name: '',
        phone: '',
        email: '',
        address: ''
    });

    const [selectedOption, setSelectedOption] = useState(null);
    const [showThankYouMessage, setShowThankYouMessage] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        if (name === 'phone') {
            if (!/^\d+$/.test(value)) {
                alert('Please insert numbers only for the phone number.');
                return; // exit the function without updating the state
            }
        }
        setFormData({
          ...formData,
          [name]: value
        });
      };

      const handleOptionSelect = (option) => {
        setSelectedOption(option);
      }

      const handleSubmit = (e) => {
        e.preventDefault();
        setShowThankYouMessage(true);
        setTimeout(() => {
            setShowThankYouMessage(false);
            navigate('/');
        }, 3000);
      }

    return (
        <Box>
            <Typography variant='h5' sx={{ textAlign: 'left', margin: '1rem', fontFamily: 'Verdana, sans-serif'}}>Customer Details</Typography>
            <div>
                <Button 
                    variant='contained'
                    style={selectedOption === 'DELIVERY' ? styles.selectedButton : styles.button}
                    onClick={() => handleOptionSelect('DELIVERY')}
                >
                    DELIVERY
                </Button>
                <Button 
                    variant='contained'
                    style={selectedOption === 'PICK-UP' ? styles.selectedButton : styles.button}
                    onClick={() => handleOptionSelect('PICK-UP')}       
                    >
                    PICK-UP
                </Button>
            </div>
            <form style={{ display: 'flex', flexDirection: 'column', gap: '1rem', alignItems: 'center'}} onSubmit={handleSubmit}>
                <TextField
                    label="Name"
                    variant="outlined" 
                    name="name" 
                    value={formData.name} 
                    onChange={handleChange} 
                    sx={{ width: '500px' }} 
                    required 
                />
                <TextField
                    label="Phone"
                    variant="outlined" 
                    name="phone" 
                    value={formData.phone} 
                    onChange={handleChange} 
                    sx={{ width: '500px' }} 
                    required 
                />
                <TextField
                    label="Email"
                    variant="outlined" 
                    name="email" 
                    value={formData.email} 
                    onChange={handleChange} 
                    sx={{ width: '500px' }} 
                    required 
                />
                {selectedOption === 'DELIVERY' && (
                    <TextField
                        label="Address"
                        variant="outlined" 
                        name="address" 
                        value={formData.address} 
                        onChange={handleChange} 
                        sx={{ width: '500px' }} 
                        required 
                    />
                )}
                <Button 
                    type="submit"   
                    variant="contained" 
                    sx={{ 
                    width: '200px',
                    fontWeight: 'bold',
                    padding: '1rem',
                    marginBottom: '1rem'
                    }}
                >
                    PAY NOW
                </Button>
            </form>
            {showThankYouMessage && (
                <Typography  variant="h6" sx={{ textAlign: 'center', color: 'green', fontWeight: 'bold' }}>
                    Thank you for your order!
                </Typography>
            )}
        </Box>
    )
};
export default CustomerForm;

