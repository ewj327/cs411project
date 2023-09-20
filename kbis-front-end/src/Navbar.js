import { Link, useMatch, useResolvedPath } from 'react-router-dom';

const Navbar = () => {
    return (
      <nav className="navbar">
        <div>
          <Link id="logo" to="/">
            <h1>KBIS</h1>
            <h2>Kidney Biopsy Image Segmentation</h2>
          </Link>
        </div>

        <ul className="links">
            <CustomLink to="/">Home</CustomLink>
            <CustomLink to="/demo">Demo</CustomLink>
            <CustomLink to="/about">About</CustomLink>
            <CustomLink to="/contact">Contact</CustomLink>
        </ul>
      </nav>  
    );
}

function CustomLink({ to, children, ...props}) {
  const resolvedPath = useResolvedPath(to)
  const isActive = useMatch({ path: resolvedPath.pathname, end: true})
  return(
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  )
}
 
export default Navbar;

// // style={{
//     textDecorationLine: 'underline',
//     color: '#9546C4',
// }}