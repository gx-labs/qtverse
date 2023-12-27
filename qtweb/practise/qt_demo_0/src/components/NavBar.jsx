import React from "react";
import styled from "styled-components";
import { NavLink } from "react-router-dom";

const NavbarContainer = styled.div`
  background-color: #21232c;
  color: #fff;
  padding: 0 4.8rem;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  @media (max-width: 768px) {
    padding: 0 2rem;
  }
`;

const Logo = styled.div`
  height: auto;
  max-width: 30%;

  img {
    max-width: 100%;
    height: auto;
  }
`;

const ButtonsContainer = styled.div`
  display: flex;
  align-items: center;
`;

const Button = styled.button`
  margin-left: 1rem;
  padding: 8px 16px;
  background-color: #04aa6d;
  color: #fff;
  border: none;
  cursor: pointer;
  border-radius: 12px;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #048c5a;
  }
`;

const NavBar = () => {
  return (
    <NavbarContainer>
      <NavLink to="/">
        <Logo>
          <img src="/qt_logo_nobg_white.png" alt="Company Logo" />
        </Logo>
      </NavLink>
      <ButtonsContainer>
        <NavLink to="/prosubscription">
          <Button>PRO</Button>
        </NavLink>
        <NavLink to="/login&register">
          <Button>Login/Logout</Button>
        </NavLink>
        
      </ButtonsContainer>
    </NavbarContainer>
  );
};

export default NavBar;
