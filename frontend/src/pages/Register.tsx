import React, { useState } from "react";
import { registerUser } from "../services/api";

const Register: React.FC = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await registerUser(username, password, email);
      setMessage("Cadastro realizado com sucesso! Faça login.");
      setUsername(""); setEmail(""); setPassword("");
    } catch (err: any) {
      setMessage("Erro ao cadastrar: " + err.response?.data?.detail || err.message);
    }
  };

  return (
    <div>
      <h1>Registrar</h1>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <input placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
        <input placeholder="Email" type="email" value={email} onChange={e => setEmail(e.target.value)} required />
        <input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} required />
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
};

export default Register;
