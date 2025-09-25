import React, { useState } from "react";
import { useSelector } from "react-redux";
import { RootState } from "../store";
import { updateProfile } from "../services/api";

const Profile: React.FC = () => {
  const token = useSelector((state: RootState) => state.user.token);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleUpdate = async () => {
    try {
      const data: any = {};
      if (username) data.username = username;
      if (password) data.password = password;
      await updateProfile(data, token!);
      setMessage("Perfil atualizado com sucesso!");
    } catch (err: any) {
      setMessage("Erro ao atualizar: " + err.response?.data?.detail || err.message);
    }
  };

  if (!token) return <p>Faça login para atualizar seu perfil.</p>;

  return (
    <div>
      <h1>Perfil</h1>
      {message && <p>{message}</p>}
      <input placeholder="Novo username" value={username} onChange={e => setUsername(e.target.value)} />
      <input placeholder="Nova senha" type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button onClick={handleUpdate}>Atualizar Perfil</button>
    </div>
  );
};

export default Profile;
