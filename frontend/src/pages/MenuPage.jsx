import React, { useState, useEffect } from 'react';
import { experimentalStyled as styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';

const Item = styled(Paper)(({ theme }) => ({
  color: '#000000',
  padding: theme.spacing(2),
  textAlign: 'center',
  marginTop: '2rem'
}));

export default function MenuPage() {
  const [items, setItems] = useState([]);
  const [orderDetails, setOrderDetails] = useState([]);

  useEffect(() => {
    fetch('/assets/MenuItems.json')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setItems(data.map(item => ({ ...item, quantity: 0 })));
      })
      .catch(error => {
        console.error('Error fetching menu items:', error);
      });
  }, []);

  const handleIncrement = (id) => {
    setItems(items.map(item =>
      item.id === id ? { ...item, quantity: item.quantity + 1 } : item
    ));
    addToOrder(id);
  };

  const handleDecrement = (id) => {
    setItems(items.map(item =>
      item.id === id && item.quantity > 0 ? { ...item, quantity: item.quantity - 1 } : item
    ));

    const existingItemIndex = orderDetails.findIndex(item => item.id === id);
    if (existingItemIndex !== -1) {
      const updatedOrderDetails = [...orderDetails];
      updatedOrderDetails[existingItemIndex].quantity -= 1;
      if (updatedOrderDetails[existingItemIndex].quantity === 0) {
        updatedOrderDetails.splice(existingItemIndex, 1);
      }
      setOrderDetails(updatedOrderDetails);
    }
  };

  const addToOrder = (id) => {
    const menuItem = items.find(item => item.id === id);
    const existingItem = orderDetails.find(item => item.id === menuItem.id);
    if (existingItem) {
      const updatedOrderDetails = orderDetails.map(item =>
        item.id === menuItem.id ? { ...item, quantity: item.quantity + 1 } : item
      );
      setOrderDetails(updatedOrderDetails);
    } else {
      setOrderDetails([...orderDetails, { ...menuItem, quantity: 1 }]);
    }
  };

  const calculateTotal = () => {
    return orderDetails.reduce((total, item) => {
      return total + item.price * item.quantity;
    }, 0);
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant='h5' sx={{ textAlign: 'left', margin: '1rem', fontFamily: 'Verdana, sans-serif' }}>
        Menu
      </Typography>
      <Grid container spacing={2}>
        <Grid item md={9}>
          <Grid container spacing={2}>
            {items.map((menuItem) => (
              <Grid item xs={12} sm={6} md={4} key={menuItem.id}>
                <Item>
                  <img
                    src={menuItem.image}
                    alt={menuItem.name}
                    style={{ width: '50%', height: '50%', objectFit: 'cover', aspectRatio: '1' }}
                  />
                  <Typography variant='h6' sx={{ fontWeight: 'bold' }}>{menuItem.name}</Typography>
                  <Typography variant='body1'>{menuItem.description}</Typography>
                  <Typography>${menuItem.price.toFixed(2)}</Typography>
                  <Typography>Quantity: {menuItem.quantity}</Typography>
                  <Button
                    variant='contained'
                    onClick={() => { handleIncrement(menuItem.id); }}
                    sx={{ mr: 1 }}
                  >
                    +
                  </Button>
                  <Button
                    variant='contained'
                    onClick={() => handleDecrement(menuItem.id)}
                  >
                    -
                  </Button>
                </Item>
              </Grid>
            ))}
          </Grid>
        </Grid>
        <Grid item md={3}>
          <Paper sx={{ marginTop: '50%' }}>
            <Typography variant='h5' sx={{ textAlign: 'left', paddingLeft: '1rem', fontWeight: '400' }}>
              Order Details
            </Typography>
            {orderDetails.map((item) => (
              <div key={item.id}>
                <Typography>{item.name}</Typography>
                <Typography>Quantity: {item.quantity}</Typography>
              </div>
            ))}
            <Typography>Total: ${calculateTotal().toFixed(2)}</Typography>
            <Link to='/customerform'>
              <Button
                variant='contained'
                disabled={orderDetails.length === 0}
                sx={{ mb: '0.5rem' }}
              >
                PROCEED
              </Button>
            </Link>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}

