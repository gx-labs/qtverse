import React, { useState } from "react";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBookmark, faThumbsUp } from "@fortawesome/free-solid-svg-icons";
import MonacoEditor from "react-monaco-editor";
import data from "../data/maindata.json";

const Container = styled.div`
  display: flex;
  flex-wrap: wrap;
  max-height: calc(100vh - 60px);
  max-width: 100%;
  overflow-y: auto;
`;

const Box = styled.div`
  width: calc(33.33% - 20px);
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

const StyledFontAwesomeIcon = styled(FontAwesomeIcon)`
  font-size: 24px;
  cursor: pointer;
`;

const CodeContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  position: relative;
`;

const ButtonContainer = styled.div`
  display: flex;
  align-items: center;
`;

const LanguageButtonsContainer = styled.div`
  display: flex;
  margin-right: 10px;
`;

const Tab = styled.div`
  padding: 10px;
  margin-right: 10px;
  background-color: ${(props) => (props.active ? "#3498db" : "#ccc")};
  color: ${(props) => (props.active ? "#fff" : "#000")};
  cursor: pointer;
`;

const LanguageButton = styled(({ active, ...rest }) => <Tab {...rest} />)`
  padding: 10px;
  margin-right: 10px;
  background-color: ${(props) => (props.active ? "#3498db" : "#ccc")};
  color: ${(props) => (props.active ? "#fff" : "#000")};
  cursor: pointer;
`;

const GoBackButton = styled.button`
  padding: 10px;
  background-color: #3498db;
  color: #fff;
  border: none;
  cursor: pointer;
  margin-bottom: 5px;
`;

const Tooltip = styled.div`
  position: absolute;
  background-color: #3498db;
  color: #fff;
  padding: 5px;
  border-radius: 4px;
  font-size: 12px;
  opacity: ${(props) => (props.visible ? 1 : 0)};
  transition: opacity 0.3s ease;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
`;

const MainContent = () => {
  const [selectedItem, setSelectedItem] = useState(null);
  const [activeTab, setActiveTab] = useState(0);
  const [tooltipVisible, setTooltipVisible] = useState(false);

  const handleBoxClick = (item) => {
    // Check if the click happened on a button
    if (!event.target.classList.contains("button")) {
      setSelectedItem(item);
      setActiveTab(0);
    }
  };

  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  const handleGoBack = () => {
    setSelectedItem(null);
  };

  const handleButtonClick = (code) => {
    // Create a textarea element to facilitate copying to clipboard
    const textarea = document.createElement("textarea");
    textarea.value = code;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);

    // Show the tooltip
    setTooltipVisible(true);

    // Hide the tooltip after a short delay
    setTimeout(() => {
      setTooltipVisible(false);
    }, 1500);
  };

  return (
    <div>
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
                  {item.files.map((file, index) => (
                    <Button
                      key={index}
                      onClick={() => handleTabClick(index)}
                      className="button"
                    >
                      {file.type}
                    </Button>
                  ))}
                </ButtonsContainer>
              </Overlay>
            </Box>
          ))}
        </Container>
      )}

      {selectedItem && (
        <div>
          <ButtonContainer>
            <GoBackButton onClick={handleGoBack}>Go Back</GoBackButton>
            <LanguageButtonsContainer>
              {selectedItem.files.map((file, index) => (
                <LanguageButton
                  key={index}
                  active={index === activeTab}
                  onClick={() => handleTabClick(index)}
                >
                  {file.type}
                </LanguageButton>
              ))}
            </LanguageButtonsContainer>
          </ButtonContainer>
          <div style={{ display: "flex" }}>
            <div style={{ width: "50%" }}>
              <Image src={selectedItem.image} alt={selectedItem.name} />
            </div>
            <div style={{ width: "50%", padding: "10px" }}>
              <CodeContainer>
                <MonacoEditor
                  width="100%"
                  height="400"
                  language="javascript" // Assuming JavaScript as the default language
                  theme="vs-dark"
                  value={selectedItem.files[activeTab].code}
                  options={{
                    readOnly: false,
                    automaticLayout: true,
                  }}
                />
                <Tooltip visible={tooltipVisible}>Copied!</Tooltip>
                <Button
                  onClick={() =>
                    handleButtonClick(selectedItem.files[activeTab].code)
                  }
                >
                  Copy Code
                </Button>
              </CodeContainer>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MainContent;


// error with copycode button and not code being copied when hovered button image clicked