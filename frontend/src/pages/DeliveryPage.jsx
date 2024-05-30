import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { TextField, Typography, Button, Paper } from '@mui/material';
import { Link } from 'react-router-dom';
import Test from './test.json';


const DeliveryPage = () => {
    const [postcode, setPostcode] = useState('');
    const [isValidPostcode, setIsValidPostcode] = useState(false);
    const [melbournePostcodes, setMelbournePostcodes] = useState(null);

    const handlePostcodeChange = (e) => {
        setPostcode(e.target.value);
    };

    // fetched the data from the .json file
    useEffect(() => {
       const fetchPostcodes = async () => {
        try {
            const response = await axios.get('assets/MelbournePostCodes.json');
            setMelbournePostcodes(response.data.Australia['Victoria, Melbourne City']);
            console.log('Fetching data successful:', response.data.Australia['Victoria, Melbourne City']);
        } catch (error) {
            console.error('Error fetching Melbourne postcodes: ', error);
        }
       };
       fetchPostcodes();
    }, []); // Empty dependency array ensures this runs once on mount

    const checkPostcodeValidity = () => {
        // checks if the melbournePostcodes exists
        // proceed only if the Melbourne postcodes data has been successfully fetched
        if (melbournePostcodes) {
            // Object.values returns only the array from the .json
            // flat() falttens the nested arrays into a single array of postcodes
            // .includes() returns true or false if the postcode given from the user is inside the melbournePostcodes
            const isValid = Object.values(melbournePostcodes).flat().includes(postcode);
            setIsValidPostcode(isValid);
            console.log('Postcode:', postcode, 'isValid:', isValid);
        }
    };

    // the effect will run whenever either 'postcode' or 
    // 'melbournePostcodes' changes
    useEffect(() => {
        if (postcode.length > 0) {
            checkPostcodeValidity();
        }
    }, [postcode, melbournePostcodes]);
    // postcode state changes whenever the user types in the postcode 
    // include melbournePostcodes ensures the effect runs once the Melbourne postcodes data
    // is fetched successfully 

    return (
        <div>
            <Typography variant='h5' sx={{textAlign:'left', fontFamily: 'Verdana, sans-serif', margin: '1rem'}}>Postcode search</Typography>
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
                <Paper elevation={2} sx={{ padding: '2rem', mt: '2rem', display: 'flex', flexDirection: 'column'}}>
                    <TextField
                        value={postcode}
                        onChange={handlePostcodeChange}
                        placeholder="Enter postcode"
                    />
                    {postcode.length > 0 && (
                        isValidPostcode ? (
                            <Typography variant='body1' sx={{ color: '#43a047'}} >Delivery available in Melbourne.</Typography>
                        ) : (
                            <Typography variant='body1' sx={{ color: '#f44336'}}>Delivery unavailable in this area.</Typography>
                        )
                    )}
                    <Link to='/menupage'>
                        <Button variant='contained' sx={{ mt: '1rem'}} disabled={!isValidPostcode}>PROCEED</Button>
                    </Link>
                </Paper>
            </div>
        </div>
    )
    
};
export default DeliveryPage;