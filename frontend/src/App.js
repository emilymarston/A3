import './App.css';
import NavBar from './components/header/NavBar'
import Homepage from './pages/Homepage'
import Footer from './components/footer/Footer'
import PickUp from './pages/PickUp'
import MenuPage from './pages/MenuPage'
import CustomerLogin from './pages/LoginMember'
import CustomerForm from './pages/CustomerForm'
import DeliveryPage from './pages/DeliveryPage'
import Reservation from './pages/Reservation'
import StaffLogin from './pages/StaffLogin';
import ManagementPortal from './pages/ManagementPortal';
import { Route, Routes } from 'react-router-dom'

function App() {
  return (
    <div className="App">
      
      <NavBar />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/pickup" element={<PickUp />} />
        <Route path="/menupage" element={<MenuPage />} />
        <Route path="/customerlogin" element={<CustomerLogin />} />
        <Route path="/customerform" element={<CustomerForm />} />
        <Route path="/deliverypage" element={<DeliveryPage />} />
        <Route path="/reservation" element={<Reservation />} />
        <Route path="/stafflogin" element={<StaffLogin />} />
        <Route path="/managementportal" element={<ManagementPortal />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
