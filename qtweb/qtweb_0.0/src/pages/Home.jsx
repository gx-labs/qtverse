import React from 'react'
import Sidebar from '../components/SideBar';
import MainContent from '../components/MainContent';


const Home = () => {
  return (

 
      <div style={{ display: "flex", flexGrow: 1 }}>
        <Sidebar />
        <MainContent />
      </div>
   
  );
}

export default Home