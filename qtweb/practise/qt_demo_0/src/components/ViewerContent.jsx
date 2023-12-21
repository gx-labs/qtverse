import React, { useState } from "react";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBookmark, faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import MonacoEditor from "react-monaco-editor";
import data from "../data/data.json";

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 0px; 
`;

const Box = styled.div`
  flex: 1 0 calc(25% - 20px); /* Four items per row, accounting for margins */
  margin: 10px;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.3s ease;

  &:hover {
    transform: scale(1.05);
  }
`;

const Image = styled.img`
  max-width: 100%;
  height: auto;
  object-fit: cover;
`;

const Overlay = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  padding: 10px;
  opacity: 0;
  transition: opacity 0.3s ease;

  ${Box}:hover & {
    opacity: 1;
  }
`;

const IconsContainer = styled.div`
  display: flex;
  justify-content: space-between;
`;

const ButtonsContainer = styled.div`
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
`;

const Button = styled.button`
  padding: 10px 15px;
  background-color: #3498db;
  color: #fff;
  border: none;
  cursor: pointer;
`;

const StyledFontAwesomeIcon = styled(FontAwesomeIcon)`
  font-size: 24px;
  cursor: pointer;
`;

const CodeContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
`;

const GoBackButton = styled.button`
  padding: 10px;
  background-color: #3498db;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-bottom: 5px;
`;

const ViewerContentWrapper = styled.div`
  background-color: #0d1117;
  color: #c9d1d9;
  height: 100vh;
`;

const DetailedViewContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
`;

const ContentContainer = styled.div`
  display: flex;
  justify-content: space-between;
  width: 100%;
`;

const DetailedImage = styled.img`
  max-width: 45%;
  height: auto;
  object-fit: cover;
  margin-right: 20px;
`;

const CodeEditorContainer = styled.div`
  width: 50%;
`;



const ViewerContent = () => {
  const [selectedItem, setSelectedItem] = useState(null);

  const handleBoxClick = (item) => {
    setSelectedItem(item);
  };

  const handleButtonClick = (code) => {
    console.log(`Code ${code} copied to clipboard`);
    // Implement your logic to copy the code to the clipboard here
  };

  const handleGoBack = () => {
    setSelectedItem(null);
  };

  return (
    <ViewerContentWrapper>
      {/* Main Content View */}
      {!selectedItem && (
        <Container>
          {data.map((item) => (
            <Box key={item.id} onClick={() => handleBoxClick(item)}>
              <Image src={item.image} alt={item.name} />
              <Overlay>
                <IconsContainer>
                  <StyledFontAwesomeIcon
                    icon={faBookmark}
                    aria-label="Add to bookmarks"
                  />
                  <StyledFontAwesomeIcon icon={faThumbsUp} aria-label="Like" />
                </IconsContainer>
                <ButtonsContainer>
                  {[item.code1, item.code2, item.code3, item.code4].map(
                    (code, index) => (
                      <Button
                        key={index}
                        onClick={() => handleButtonClick(code)}
                      >
                        {code}
                      </Button>
                    )
                  )}
                </ButtonsContainer>
              </Overlay>
            </Box>
          ))}
        </Container>
      )}

      {/* Detailed View */}
      {selectedItem && (
        <DetailedViewContainer>
          <GoBackButton onClick={handleGoBack}>Go Back</GoBackButton>
          <DetailedImage src={selectedItem.image} alt={selectedItem.name} />
          <CodeEditorContainer>
            <MonacoEditor
              width="100%"
              height="400"
              language="html"
              theme="vs-dark"
              value={selectedItem.code1}
              options={{
                readOnly: false,
                automaticLayout: true,
              }}
            />
          </CodeEditorContainer>
        </DetailedViewContainer>
      )}
    </ViewerContentWrapper>
  );
};

export default ViewerContent;
