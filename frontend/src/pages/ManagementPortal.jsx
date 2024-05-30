import React, { useState } from 'react'
import { Typography, Paper, Table, TableHead, TableBody, TableRow, TableCell } from '@mui/material'

const ManagementPortal = () => {
    const [orderDetails, setOrderDetails] = useState({
        orderID: '',
        name: '',
        orderDescription: '',
        tableNo: '',
        orderStatus: '',
        orderType: '',
        timeOrdered: ''
    })
  return (
    <div style={{margin:'1rem'}}>
        <Typography variant='h5' textAlign='left' sx={{ fontFamily: 'Verdana, sans-serif' }}>Restaurant Management Portal</Typography>
        <Typography variant='body2' textAlign='left' sx={{ fontFamily: 'Verdana, sans-serif', marginBottom: '1rem' }}>In use for restaurant staffs</Typography>
        <Table>
            <TableHead>
                <TableCell>Order ID</TableCell>
                <TableCell>Name</TableCell>
                <TableCell>Order Description</TableCell>
                <TableCell>Table No.</TableCell>
                <TableCell>Order Status</TableCell>
                <TableCell>Order Type</TableCell> 
                <TableCell>Time Ordered</TableCell>                
            </TableHead>
        </Table>
    </div>
  )
}

export default ManagementPortal