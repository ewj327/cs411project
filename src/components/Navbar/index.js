import React from "react";
import { Nav, NavLink, NavMenu } 
    from "./NavbarElements";
  
const Navbar = () => {
  return (
    <>
      <Nav bg="dark" variant="dark">
        <NavMenu>
          <h1>Welcome!</h1>
          <NavLink to="/search" activeStyle>
            Search
          </NavLink>
          <NavLink to="/profile" activeStyle>
            Profile
          </NavLink>
          <NavLink to="/wishlist" activeStyle>
            Wishlist
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};
  
export default Navbar;