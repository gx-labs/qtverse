
import styled from "styled-components";

const Container = styled.div`
  display: grid;
  grid-template-columns: 200px 1fr; /* Sidebar width and the rest of the page */
  grid-template-rows: auto 1fr auto; /* Navbar, content, and footer heights */
  grid-template-areas:
    "navbar navbar"
    "sidebar content"
    "footer footer";
  height: 100vh;
`;

const SideBarContainer = styled.div`
  grid-area: sidebar;
  background-color: #21232c;
  overflow-y: scroll;
`;

const SideBarHeader = styled.h2`
  font-size: 25px;
  margin: 10px 0px;
  background-color: #04aa6d;
  color: #fff;
  text-align: center;
`;

const SideBarMainFolder = styled.div`
  font-size: 15px;
  cursor: pointer;
  margin: 5px 10px;
  border: 1px solid #000;
  background-color: #04aa6d;
  color: #fff;
  text-align: center;
  padding: 2px; /* Add padding to create space inside the main folder */
  user-select: none;

  &:hover {
    background-color: #555;
  }
`;

const SideBarItem = styled.li`
  font-size: 15px;
  margin: 5px 15px;
  list-style: none;
  cursor: pointer;
  user-select: none;
  text-align: center;
  color: #fff;

  &:hover {
    background-color: #ffffff34;
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