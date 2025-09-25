import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  headers: { "Content-Type": "application/json" },
});

// Login
export const loginUser = async (username: string, password: string) => {
  const response = await api.post("users/login/", { username, password });
  return response.data;
};

// Registro
export const registerUser = async (username: string, password: string, email: string) => {
  const response = await api.post("users/register/", { username, password, email });
  return response.data;
};

// Buscar tweets (apenas usuários seguidos)
export const fetchTweets = async (token: string) => {
  const response = await api.get("tweets/", {
    headers: { Authorization: `Token ${token}` },
  });
  return response.data;
};

// Postar tweet
export const postTweet = async (content: string, token: string) => {
  const response = await api.post(
    "tweets/",
    { content },
    { headers: { Authorization: `Token ${token}` } }
  );
  return response.data;
};

// Atualizar perfil
export const updateProfile = async (data: any, token: string) => {
  const response = await api.patch("users/me/", data, {
    headers: { Authorization: `Token ${token}` },
  });
  return response.data;
};

// Seguir / deixar de seguir
export const toggleFollow = async (userId: number, token: string) => {
  const response = await api.post(
    `users/${userId}/follow/`,
    {},
    { headers: { Authorization: `Token ${token}` } }
  );
  return response.data;
};

// Curtir tweet
export const likeTweet = async (tweetId: number, token: string) => {
  const response = await api.post(
    `tweets/${tweetId}/like/`,
    {},
    { headers: { Authorization: `Token ${token}` } }
  );
  return response.data;
};

// Comentar tweet
export const commentTweet = async (tweetId: number, content: string, token: string) => {
  const response = await api.post(
    `tweets/${tweetId}/comment/`,
    { content },
    { headers: { Authorization: `Token ${token}` } }
  );
  return response.data;
};
