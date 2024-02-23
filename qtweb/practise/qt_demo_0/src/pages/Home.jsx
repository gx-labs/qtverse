import React from "react";
import styled from "styled-components";
import SideBar from "../components/SideBar";
import ViewerContent from "../components/ViewerContent";

const Container = styled.div`
  display: flex;
  height: 100vh; /* Adjust as needed */
`;

const SideBarWrapper = styled.div`
  width: 200px;
`;

const ContentWrapper = styled.div`
  flex: 1;
  overflow-y: auto;
`;

const Home = () => {
  return (
    <Container>
      <SideBarWrapper>
        <SideBar />
      </SideBarWrapper>
      <ContentWrapper>
        <ViewerContent />
      </ContentWrapper>
    </Container>
  );
};

export default Home;
