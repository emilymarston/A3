import React, { useState } from 'react';
import { experimentalStyled as styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import menuItems from '/assets/menuItems.json';
import { Link } from 'react-router-dom';

const Item = styled(Paper)(({ theme }) => ({
  color: '#000000',
  padding: theme.spacing(2),
  textAlign: 'center',
  marginTop: '2rem'
}));

export default function MenuPage() {
    // spreads the property of the item in the menuItems  
    // and add a new property called quantity and initialised it to 0
   const [items, setItems] = useState(menuItems.map(item => ({ ...item, quantity: 0 })));
   const [orderDetails, setOrderDetails] = useState([]);

  const handleIncrement = (id) => {
    setItems(items.map(item =>
      item.id === id ? { ...item, quantity: item.quantity + 1 } : item
    ));
  };

  const handleDecrement = (id) => {
    setItems(items.map(item =>
      item.id === id && item.quantity > 0 ? { ...item, quantity: item.quantity - 1 } : item
    ));
  
    // find which index to reduce
    const existingItemIndex = orderDetails.findIndex(item => item.id === id);
    // if findIndex doesnt return -1 meaning, the item exists, then update the orderDetails.
    if (existingItemIndex !== -1) {
        // update the orderDetails by spreading the property in the object
      const updatedOrderDetails = [...orderDetails];
      // after spreading it, retrieves the quantity property from the orderDetails at the index specified
      // reduce the quantity
      updatedOrderDetails[existingItemIndex].quantity -= 1;
      if (updatedOrderDetails[existingItemIndex].quantity === 0) {
        // If the quantity becomes 0, remove the item from order details
        updatedOrderDetails.splice(existingItemIndex, 1);
      }
      setOrderDetails(updatedOrderDetails);
    }
  };
  
  const addToOrder = (menuItem) => {
    // find if the menuItem exists or not
    const existingItem = orderDetails.find(item => item.id === menuItem.id);
    // If it exists, then updates the orderDetails
    if (existingItem) {
        // create a new object updatedOrderDetails and spread the original items from the orderDetails and updates it with the new quantity
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
      <Typography variant='h5' sx={{ textAlign: 'left', margin: '1rem', fontFamily: 'Verdana, sans-serif'}}>Menu</Typography>
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
                        <Typography variant='h6' sx={{ fontWeight: 'bold'}}>{menuItem.name}</Typography>
                        <Typography variant='body1'>{menuItem.description}</Typography>
                        <Typography>${menuItem.price.toFixed(2)}</Typography>
                        <Typography>Quantity: {menuItem.quantity}</Typography>
                        <Button variant='contained' onClick={() => {handleIncrement(menuItem.id); addToOrder(menuItem)}} sx={{ mr: 1 }}>+</Button>
                        <Button variant='contained' onClick={() => handleDecrement(menuItem.id)}>-</Button>
                    </Item>
                </Grid>
                ))}
            </Grid>
        </Grid>
        <Grid item md={3}>
            <Paper sx={{ marginTop: '50%'}}>
                <Typography variant='h5' sx={{ textAlign: 'left', paddingLeft: '1rem', fontWeight: '400'}}>Order Details</Typography>
                {orderDetails.map((item) =>(
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
                    sx={{mb: '0.5rem'}}
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
