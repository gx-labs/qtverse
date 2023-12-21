import React, { useState } from "react";
import Sidebar from "../components/SideBar";
import MainContent from "../components/MainContent";
// import jsonData from "../data/data.json";

const App = () => {
  const [selectedData, setSelectedData] = useState([]);

  const handleSidebarItemClick = (data) => {
    setSelectedData(data);
  };

  return (
    <div style={{ display: "flex" }}>
      <Sidebar onSidebarItemClick={handleSidebarItemClick} />
      <MainContent selectedData={selectedData} />
    </div>
  );
};

export default App;
