import React from 'react';
import { Typography, Paper, Button } from '@mui/material';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom
import StorefrontOutlinedIcon from '@mui/icons-material/StorefrontOutlined';

const styles = {
    container: {
      padding: '2rem',
      display: 'flex',
      justifyContent: 'center'
    },
    mainPaper: {
      position: 'relative', 
      width: '40%',
      backgroundColor: '#325636',
      padding: '2rem', 
      display: 'flex',
      flexDirection: 'column'
    },
    text: {
        fontWeight: 'bold',
        color: '#FFFFFF',
        textAlign: 'left',
        margin: '0 0.3rem'
    },
    icon: {
        color: '#FFFFFF',
    },
    storeDetails: {
        display: 'flex',
        alignItems: 'center',
        marginTop: '1rem'
    },
    btn: {
        fontWeight: 'bold',
        width: '40%',
        marginTop: '0.5rem'
    }
};

const PickupPage = () => {
  return (
    <div style={styles.container}>
      <Paper elevation={3} sx={styles.mainPaper}>
        <Typography variant='h5' style={styles.text}>Store details</Typography>
        <div style={styles.storeDetails}>
            <StorefrontOutlinedIcon style={styles.icon} />
            <Typography style={styles.text}>Relaxing Koala</Typography>
        </div>
            <Typography style={styles.text}>Shop 2, Glenferrie Road, 3122, VIC</Typography>
            <Link to="/menupage"> {/* Use Link to navigate to the menu page */}
                <Button style={styles.btn} variant='contained'>PICKUP NOW</Button>
            </Link>
      </Paper>
    </div>
  );
};

export default PickupPage;
