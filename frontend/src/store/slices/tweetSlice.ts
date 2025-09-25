import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface Tweet {
  id: number;
  content: string;
  author: string;
  created_at: string;
}

interface TweetState {
  tweets: Tweet[];
}

const initialState: TweetState = { tweets: [] };

const tweetSlice = createSlice({
  name: "tweet",
  initialState,
  reducers: {
    setTweets: (state, action: PayloadAction<Tweet[]>) => {
      state.tweets = action.payload;
    },
    addTweet: (state, action: PayloadAction<Tweet>) => {
      state.tweets.unshift(action.payload);
    },
  },
});

export const { setTweets, addTweet } = tweetSlice.actions;
export default tweetSlice.reducer;
