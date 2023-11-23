import React, { useState } from "react";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBookmark, faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import MonacoEditor from "react-monaco-editor";
import data from "../data/maindata.json";

// Dark Theme
const darkTheme = {
  backgroundColor: "#333",
  color: "#fff",
};

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  max-height: calc(100vh - 60px);
  overflow-y: auto;
  width: calc(33.33% - 10px);
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
  width: 100%;
  height: 100%;
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
  justify-content: space-between;
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

// Add aria-label attributes for icons
const BookmarkIcon = styled(FontAwesomeIcon).attrs({
  icon: faBookmark,
  "aria-label": "Bookmark",
  style: { fontSize: "24px", cursor: "pointer" },
})``;

const ThumbsUpIcon = styled(FontAwesomeIcon).attrs({
  icon: faThumbsUp,
  "aria-label": "Thumbs Up",
  style: { fontSize: "24px", cursor: "pointer" },
})``;

const CodeContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
`;

const MainContent = () => {
  const [selectedItem, setSelectedItem] = useState(null);

  const handleBoxClick = (item) => {
    setSelectedItem(item);
  };

  const handleButtonClick = (code) => {
    // You can implement the logic to copy the code to the clipboard here
    console.log(`Code ${code} copied to clipboard`);
  };

  return (
    <div style={selectedItem ? darkTheme : {}}>
      {/* Main Content View */}
      {!selectedItem && (
        <Container>
          {data.map((item) => (
            <Box key={item.id} onClick={() => handleBoxClick(item)}>
              <Image src={item.image} alt={item.name} />
              <Overlay className="overlay">
                <IconsContainer>
                  <BookmarkIcon />
                  <ThumbsUpIcon />
                </IconsContainer>
                <ButtonsContainer>
                  <Button onClick={() => handleButtonClick(item.code1)}>
                    {item.code1}
                  </Button>
                  <Button onClick={() => handleButtonClick(item.code2)}>
                    {item.code2}
                  </Button>
                  <Button onClick={() => handleButtonClick(item.code3)}>
                    {item.code3}
                  </Button>
                  <Button onClick={() => handleButtonClick(item.code4)}>
                    {item.code4}
                  </Button>
                </ButtonsContainer>
              </Overlay>
            </Box>
          ))}
        </Container>
      )}

      {/* Detailed View */}
      {selectedItem && (
        <div style={{ display: "flex" }}>
          <div style={{ width: "50%" }}>
            <button
              onClick={() => setSelectedItem(null)}
              style={{
                padding: "10px",
                backgroundColor: "#3498db",
                color: "#fff",
                border: "none",
                cursor: "pointer",
                marginBottom: "5px",
              }}
            >
              Go Back
            </button>
            <Image src={selectedItem.image} alt={selectedItem.name} />
          </div>
          <div style={{ width: "50%", padding: "10px" }}>
            <CodeContainer>
              <MonacoEditor
                width="100%"
                height="300"
                language="html"
                theme="vs-dark"
                value={selectedItem.code1}
                options={{
                  readOnly: false,
                  automaticLayout: true,
                }}
              />
            </CodeContainer>
          </div>
        </div>
      )}
    </div>
  );
};

export default MainContent;
