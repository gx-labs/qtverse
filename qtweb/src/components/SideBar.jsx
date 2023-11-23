import React, { useState } from "react";
import styled from "styled-components";

const SidebarContainer = styled.div`
  width: 250px;
  background-color: #ccc;
  padding: 0px 2px;
  position: sticky;
  top: 60px;
  bottom: 0;
  overflow-y: auto;
  height: 100vh;
`;

const SidebarHeader = styled.h2`
  font-size: 25px;
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
  padding: 5px; /* Add padding to create space inside the main folder */
  user-select: none; /* Disable text selection for better interaction */

  &:hover {
    background-color: #555; /* Darken the background on hover */
  }
`;

const SidebarItem = styled.li`
  font-size: 15px;
  margin: 5px 15px;
  list-style: none;
  cursor: pointer;
  user-select: none;

  &:hover {
    background-color: #fff; /* Darken the background on hover */
  }
`;

const Sidebar = () => {
  const [expandedFolders, setExpandedFolders] = useState([]);

  const toggleFolder = (folder) => {
    setExpandedFolders((prevFolders) => {
      if (prevFolders.includes(folder)) {
        // If folder is already in the list, remove it
        return prevFolders.filter((f) => f !== folder);
      } else {
        // If folder is not in the list, add it
        return [...prevFolders, folder];
      }
    });
  };

  return (
    <SidebarContainer>
      <SidebarHeader>WIDGETS</SidebarHeader>

      <SidebarMainFolder onClick={() => toggleFolder("Widgets")}>
        Widgets
      </SidebarMainFolder>
      {expandedFolders.includes("Widgets") && (
        <ul>
          <SidebarItem>Buttons</SidebarItem>
          <SidebarItem>Radio Buttons</SidebarItem>
          <SidebarItem>Check Box </SidebarItem>
          <SidebarItem>Combo Box </SidebarItem>
          <SidebarItem>Group Box </SidebarItem>
          <SidebarItem>Spin Box </SidebarItem>
          <SidebarItem>Tool Box</SidebarItem>
          <SidebarItem>Sliders </SidebarItem>
          <SidebarItem>Line Edit </SidebarItem>
          <SidebarItem>Calendar </SidebarItem>
          <SidebarItem>List View </SidebarItem>
          <SidebarItem>Table View</SidebarItem>
          <SidebarItem>Tree View </SidebarItem>
          <SidebarItem>Loading Bars</SidebarItem>
          <SidebarItem>Tab Widget</SidebarItem>
          <SidebarItem>List Widget</SidebarItem>
          <SidebarItem>Labels</SidebarItem>
          <SidebarItem>Widgets 2</SidebarItem>
          <SidebarItem>QDockWidget</SidebarItem>
          <SidebarItem>QSizeGrip</SidebarItem>
          <SidebarItem>QHeaderView</SidebarItem>
          <SidebarItem>QSplitter</SidebarItem>
          <SidebarItem>QToolButton</SidebarItem>
          <SidebarItem>QToolTip</SidebarItem>
          <SidebarItem>QMainWindow</SidebarItem>
          <SidebarItem>QMenu</SidebarItem>
          <SidebarItem>QWidget</SidebarItem>
        </ul>
      )}

      <SidebarMainFolder onClick={() => toggleFolder("Dialog")}>
        Dialogs
      </SidebarMainFolder>
      {expandedFolders.includes("Dialog") && (
        <ul>
          <SidebarItem>Input Dialog </SidebarItem>
          <SidebarItem>Color Dialog</SidebarItem>
          <SidebarItem>File Dialog </SidebarItem>
          <SidebarItem>Font Dialog </SidebarItem>
        </ul>
      )}

      <SidebarMainFolder onClick={() => toggleFolder("Bars")}>
        Bars
      </SidebarMainFolder>
      {expandedFolders.includes("Bars") && (
        <ul>
          <SidebarItem>Scroll Bars </SidebarItem>
          <SidebarItem>Menu Bar</SidebarItem>
          <SidebarItem>Tool Bar </SidebarItem>
          <SidebarItem>Status Bar</SidebarItem>
          <SidebarItem>Tab Bar </SidebarItem>
        </ul>
      )}

      <SidebarHeader>CUSTOM</SidebarHeader>

      <SidebarMainFolder onClick={() => toggleFolder("Custom")}>
        Custom
      </SidebarMainFolder>
      {expandedFolders.includes("Custom") && (
        <ul>
          <SidebarItem>Custom </SidebarItem>
        </ul>
      )}
    </SidebarContainer>
  );
};

export default Sidebar;
