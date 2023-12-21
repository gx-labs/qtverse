
import styled from "styled-components";


const NavbarContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
`;



const Logo = styled.div`
  font-size: 1.5rem;
  font-weight: bold;

`;


const NavLinks = styled.div`
  display: flex;
  align-items: center;

  @media (max-width: 768px) {
    display: none;
  }
`;

const NavLink = styled.a`
  margin: 0 1rem;
  color: #fff;
  text-decoration: none;
`;

const NavBar = () => {
  

  return (
    <>
      <NavbarContainer>
        
        <Logo>
          LOGO
        </Logo>
        <NavLinks>
          <NavLink href="#">Subscribe</NavLink>
          <NavLink href="#">Register</NavLink>
          <NavLink href="#">Login</NavLink>
        </NavLinks>
      </NavbarContainer>
     
    </>
  );
};

export default NavBar;
