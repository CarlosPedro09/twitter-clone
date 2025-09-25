import React from "react";

interface TweetProps {
  author: string;
  content: string;
  created_at: string;
  onLike?: () => void;
  onFollow?: () => void;
}

const Tweet: React.FC<TweetProps> = ({ author, content, created_at, onLike, onFollow }) => {
  return (
    <div style={{ border: "1px solid #ccc", padding: 10, marginBottom: 5 }}>
      <strong>{author}</strong>
      <p>{content}</p>
      <small>{created_at}</small>
      <div>
        {onLike && <button onClick={onLike}>Curtir</button>}
        {onFollow && <button onClick={onFollow}>Seguir/Deixar de seguir</button>}
      </div>
    </div>
  );
};

export default Tweet;
