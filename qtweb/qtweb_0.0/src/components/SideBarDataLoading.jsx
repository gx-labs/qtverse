import React, { useState } from "react";
import styled from "styled-components";
import data from "../data/finaldestination.json";

const SidebarContainer = styled.div`
  width: 650px;
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
  const [selectedItem, setSelectedItem] = useState(null);

  const handleSelectItem = (itemName) => {
    // Find the selected item in the JSON data
    let selectedItem = null;

    for (const category of data.categories) {
      for (const group of category.groups) {
        for (const type of group.types) {
          selectedItem = type.items.find((item) => item.name === itemName);
          if (selectedItem) break;
        }
        if (selectedItem) break;
      }
      if (selectedItem) break;
    }

    // Log the relevant information
    if (selectedItem) {
      console.log("Selected Category:", selectedItem.groupname);
      console.log("Selected Type:", selectedItem.type);
      console.log("Selected Item:", selectedItem.name);
      console.log("Selected Item ID:", selectedItem.id);
      console.log("Selected Item Image:", selectedItem.image);
      console.log("Selected Item Files:", selectedItem.files);
    } else {
      console.error("Selected item not found");
    }
  };

  return (
    <SidebarContainer>
      <SidebarHeader>WIDGETS</SidebarHeader>

      <SidebarMainFolder
        onClick={() => handleSelectItem("Widgets", null, null)}
      >
        Widgets
      </SidebarMainFolder>

      <ul>
        <SidebarItem
          onClick={() => handleSelectItem("Buttons", "Buttons", "Widgets")}
        >
          Buttons
        </SidebarItem>
        <SidebarItem
          onClick={() =>
            handleSelectItem("Radio Buttons", "Radio Buttons", "Widgets")
          }
        >
          Radio Buttons
        </SidebarItem>
      </ul>

      <SidebarMainFolder
        onClick={() => handleSelectItem("Dialogs", null, null)}
      >
        Dialogs
      </SidebarMainFolder>

      <ul>
        <SidebarItem
          onClick={() =>
            handleSelectItem("Input Dialog", "Input Dialog", "Dialogs")
          }
        >
          Input Dialog
        </SidebarItem>
        <SidebarItem
          onClick={() =>
            handleSelectItem("Color Dialog", "Color Dialog", "Dialogs")
          }
        >
          Color Dialog
        </SidebarItem>
      </ul>

      <SidebarMainFolder onClick={() => handleSelectItem("Bars", null, null)}>
        Bars
      </SidebarMainFolder>

      <ul>
        <SidebarItem
          onClick={() => handleSelectItem("Scroll Bars", "Scroll Bars", "Bars")}
        >
          Scroll Bars
        </SidebarItem>
        <SidebarItem
          onClick={() => handleSelectItem("Menu Bar", "Menu Bar", "Bars")}
        >
          Menu Bar
        </SidebarItem>
      </ul>

      <SidebarHeader>CUSTOM</SidebarHeader>

      <SidebarMainFolder onClick={() => handleSelectItem("Custom", null, null)}>
        Custom
      </SidebarMainFolder>

      <ul>
        <SidebarItem
          onClick={() => handleSelectItem("Custom", "Custom", "Custom")}
        >
          Custom
        </SidebarItem>
      </ul>
    </SidebarContainer>
  );
};

export default Sidebar;
