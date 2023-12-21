
import styled from "styled-components";

const SideBarContainer = styled.div`
  width: 200px;
  background-color: #ccc;
  padding: 0px 2px;
  /* position: fixed; */
  overflow-y: auto;
  height: 100vh;
  
`;

const SideBarHeader = styled.h2`
  font-size: 25px;
  margin: 10px 0px;
  background-color: #ddd;
  text-align: center;
`;

const SideBarMainFolder = styled.div`
  font-size: 15px;
  cursor: pointer;
  margin: 5px 10px;
  border: 1px solid #000;
  background-color: #666;
  color: #fff;
  text-align: center;
  padding: 2px; /* Add padding to create space inside the main folder */
  user-select: none; /* Disable text selection for better interaction */

  &:hover {
    background-color: #555; /* Darken the background on hover */
  }
`;

const SideBarItem = styled.li`
  font-size: 15px;
  margin: 5px 15px;
  list-style: none;
  cursor: pointer;
  user-select: none;
  text-align: center;

  &:hover {
    background-color: #fff; /* Darken the background on hover */
  }
`;

const SideBar = () => {
  return (
    <SideBarContainer>
      <SideBarHeader>WIDGETS</SideBarHeader>

      <SideBarMainFolder>Widgets</SideBarMainFolder>

      <ul>
        <SideBarItem>Buttons</SideBarItem>
        <SideBarItem>Radio Buttons</SideBarItem>
        <SideBarItem>Check Box </SideBarItem>
        <SideBarItem>Combo Box </SideBarItem>
        <SideBarItem>Group Box </SideBarItem>
        <SideBarItem>Spin Box </SideBarItem>
        <SideBarItem>Tool Box</SideBarItem>
        <SideBarItem>Sliders </SideBarItem>
        <SideBarItem>Line Edit </SideBarItem>
        <SideBarItem>Calendar </SideBarItem>
        <SideBarItem>List View </SideBarItem>
        <SideBarItem>Table View</SideBarItem>
        <SideBarItem>Tree View </SideBarItem>
        <SideBarItem>Loading Bars</SideBarItem>
        <SideBarItem>Tab Widget</SideBarItem>
        <SideBarItem>List Widget</SideBarItem>
        <SideBarItem>Labels</SideBarItem>
        <SideBarItem>Widgets 2</SideBarItem>
        <SideBarItem>QDockWidget</SideBarItem>
        <SideBarItem>QSizeGrip</SideBarItem>
        <SideBarItem>QHeaderView</SideBarItem>
        <SideBarItem>QSplitter</SideBarItem>
        <SideBarItem>QToolButton</SideBarItem>
        <SideBarItem>QToolTip</SideBarItem>
        <SideBarItem>QMainWindow</SideBarItem>
        <SideBarItem>QMenu</SideBarItem>
        <SideBarItem>QWidget</SideBarItem>
      </ul>

      <SideBarMainFolder>Dialogs</SideBarMainFolder>

      <ul>
        <SideBarItem>Input Dialog </SideBarItem>
        <SideBarItem>Color Dialog</SideBarItem>
        <SideBarItem>File Dialog </SideBarItem>
        <SideBarItem>Font Dialog </SideBarItem>
      </ul>

      <SideBarMainFolder>Bars</SideBarMainFolder>

      <ul>
        <SideBarItem>Scroll Bars </SideBarItem>
        <SideBarItem>Menu Bar</SideBarItem>
        <SideBarItem>Tool Bar </SideBarItem>
        <SideBarItem>Status Bar</SideBarItem>
        <SideBarItem>Tab Bar </SideBarItem>
      </ul>

      <SideBarHeader>CUSTOM</SideBarHeader>

      <SideBarMainFolder>Custom</SideBarMainFolder>

      <ul>
        <SideBarItem>Custom </SideBarItem>
      </ul>
    </SideBarContainer>
  );
};

export default SideBar;