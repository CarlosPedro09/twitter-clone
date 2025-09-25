import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="header">
      <h1>Twitter Clone</h1>
      <nav>
        <Link to="/home">Home</Link>
        <Link to="/profile">Profile</Link>
        <Link to="/">Login</Link>
      </nav>
    </header>
  );
};

export default Header;
