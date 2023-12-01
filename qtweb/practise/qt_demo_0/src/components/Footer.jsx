import React from "react";
import styled from "styled-components";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faFacebook,
  faTwitter,
  faInstagram,
  faLinkedin,
} from "@fortawesome/free-brands-svg-icons";

const FooterContainer = styled.footer`
  text-align: center;
  padding: 5px;
  // position: fixed;
  bottom: 0;
  width: 100%;
  background-color: #f2f2f2; /* Light grey color */
`;
const Logo = styled.img`
  max-width: 100px; /* Adjust the size as needed */
`;

const SocialIconsContainer = styled.div`
  margin-top: 10px;
`;

const SocialIcon = styled(FontAwesomeIcon)`
  margin: 0 10px; /* Adjust spacing between icons */
  font-size: 30px; /* Adjust the size as needed */
`;

const Line = styled.hr`
  margin: 20px 0;
  border: 0;
  border-top: 1px solid #ccc;
`;

const CopyrightText = styled.p`
  font-size: 14px;
  color: #000;
  margin: 5px 0;
`;

const Footer = () => {
  return (
    <FooterContainer>
      <Logo src="./qt_logo_nobg.png" alt="Company Logo" />
      <SocialIconsContainer>
        <SocialIcon icon={faFacebook} />
        <SocialIcon icon={faTwitter} />
        <SocialIcon icon={faInstagram} />
        <SocialIcon icon={faLinkedin} />
      </SocialIconsContainer>
      <Line />
      <CopyrightText>&copy; 2023 Made with love by Jaswanth.</CopyrightText>
    </FooterContainer>
  );
};

export default Footer;
