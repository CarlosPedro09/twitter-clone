import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} Twitter. Todos os direitos reservados Carlos Pedro.</p>
    </footer>
  );
};

export default Footer;
