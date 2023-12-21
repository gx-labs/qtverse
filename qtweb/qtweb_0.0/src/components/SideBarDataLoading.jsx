import React, { useState } from "react";
import styled from "styled-components";
import jsonData from "../data/data.json"; // Adjust the import path based on your project structure

const SidebarContainer = styled.div`
  width: 250px;
  background-color: #ccc;
  padding: 10px;
  position: sticky;
  top: 0;
  overflow-y: auto;
  height: 100vh;
`;

const SidebarHeader = styled.h2`
  font-size: 18px;
  margin: 10px 0px;
  background-color: #ddd;
`;

const SidebarMainFolder = styled.div`
  font-size: 15px;
  cursor: pointer;
  margin: 5px 10px;
  border: 1px solid #000;
  background-color: #666;
  color: #fff;
  text-align: center;
  padding: 5px;
  user-select: none;

  &:hover {
    background-color: #555;
  }
`;

const SidebarItem = styled.li`
  font-size: 15px;
  margin: 5px 15px;
  list-style: none;
  cursor: pointer;
  user-select: none;

  &:hover {
    background-color: #fff;
  }
`;

const Sidebar = () => {
  const [filteredData, setFilteredData] = useState([]);

  const handleCategoryClick = (category) => {
    const filteredCategoryData = jsonData.filter(
      (item) => item.category === category
    );
    setFilteredData(filteredCategoryData);
    console.log("Filtered Category Data:", filteredCategoryData);
  };

  const handleGroupClick = (group) => {
    const filteredGroupData = jsonData.filter((item) => item.group === group);
    setFilteredData(filteredGroupData);
    console.log("Filtered Group Data:", filteredGroupData);
  };

  return (
    <SidebarContainer>
      <SidebarHeader>WIDGETS</SidebarHeader>

      <SidebarMainFolder onClick={() => handleCategoryClick("Widgets")}>
        Widgets
      </SidebarMainFolder>

      <ul>
        <SidebarItem onClick={() => handleGroupClick("Buttons")}>
          Buttons
        </SidebarItem>
        <SidebarItem onClick={() => handleGroupClick("Radio Buttons")}>
          Radio Buttons
        </SidebarItem>
      </ul>

      <SidebarMainFolder onClick={() => handleCategoryClick("Dialogs")}>
        Dialogs
      </SidebarMainFolder>

      <ul>
        <SidebarItem onClick={() => handleGroupClick("Input Dialogs")}>
          Input Dialogs
        </SidebarItem>
        <SidebarItem onClick={() => handleGroupClick("Color Dialogs")}>
          Color Dialogs
        </SidebarItem>
      </ul>

      <SidebarMainFolder onClick={() => handleCategoryClick("Bars")}>
        Bars
      </SidebarMainFolder>

      <ul>
        <SidebarItem onClick={() => handleGroupClick("Scroll Bars")}>
          Scroll Bars
        </SidebarItem>
        <SidebarItem onClick={() => handleGroupClick("Menu Bars")}>
          Menu Bars
        </SidebarItem>
      </ul>

      <SidebarHeader>CUSTOM</SidebarHeader>

      <SidebarMainFolder onClick={() => handleCategoryClick("Custom")}>
        Custom
      </SidebarMainFolder>

      <ul>
        <SidebarItem onClick={() => handleGroupClick("Custom")}>
          Custom
        </SidebarItem>
      </ul>
    </SidebarContainer>
  );
};

export default Sidebar;
