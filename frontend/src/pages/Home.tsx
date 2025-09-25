import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { RootState } from "../store";
import { fetchTweets, postTweet, toggleFollow } from "../services/api";

interface Tweet {
  id: number;
  user: { id: number; username: string; avatar?: string };
  content: string;
  created_at: string;
  likes: { id: number; user: { username: string } }[];
  comments: { id: number; user: { username: string }; content: string }[];
}

const Home: React.FC = () => {
  const token = useSelector((state: RootState) => state.user.token);
  const [tweets, setTweets] = useState<Tweet[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [newContent, setNewContent] = useState("");

  useEffect(() => {
    if (!token) return;

    const loadTweets = async () => {
      setLoading(true);
      try {
        const data = await fetchTweets(token);
        setTweets(data);
      } catch (err: any) {
        setError("Erro ao carregar tweets: " + (err.response?.data?.detail || err.message));
      } finally {
        setLoading(false);
      }
    };

    loadTweets();
  }, [token]);

  const handlePostTweet = async () => {
    if (!newContent.trim()) return;
    try {
      const tweet = await postTweet(newContent, token!);
      setTweets([tweet, ...tweets]);
      setNewContent("");
    } catch (err: any) {
      setError("Erro ao postar tweet: " + (err.response?.data?.detail || err.message));
    }
  };

  const handleToggleFollow = async (userId: number) => {
    try {
      await toggleFollow(userId, token!);
      // opcional: atualizar feed ou estado do follow
    } catch (err: any) {
      setError("Erro ao seguir/deixar de seguir: " + (err.response?.data?.detail || err.message));
    }
  };

  if (!token) return <p>Faça login para ver seu feed.</p>;
  if (loading) return <p>Carregando tweets...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div>
      <h1>Feed</h1>

      <div style={{ marginBottom: "20px" }}>
        <textarea
          placeholder="O que está acontecendo?"
          value={newContent}
          onChange={(e) => setNewContent(e.target.value)}
          rows={3}
          style={{ width: "100%", padding: "10px" }}
        />
        <button onClick={handlePostTweet} style={{ marginTop: "5px" }}>
          Tweet
        </button>
      </div>

      {tweets.length === 0 ? (
        <p>Nenhum tweet encontrado.</p>
      ) : (
        <ul style={{ listStyle: "none", padding: 0 }}>
          {tweets.map((tweet) => (
            <li key={tweet.id} style={{ border: "1px solid #ccc", padding: 10, marginBottom: 10 }}>
              <strong>{tweet.user.username}</strong>
              <p>{tweet.content}</p>
              <small>{tweet.created_at}</small>
              <div style={{ marginTop: 5 }}>
                <span>❤️ {tweet.likes.length} </span>
                <span>💬 {tweet.comments.length}</span>
                <button
                  style={{ marginLeft: 10 }}
                  onClick={() => handleToggleFollow(tweet.user.id)}
                >
                  Seguir/Deixar de seguir
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Home;
