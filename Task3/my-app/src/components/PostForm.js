import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addNewPost } from '../redux/postsSlice';

const PostForm = () => {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title && body) {
      const newPost = { title, body };
      dispatch(addNewPost(newPost));
      setTitle('');
      setBody('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add a New Post</h2>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Body"
        value={body}
        onChange={(e) => setBody(e.target.value)}
      />
      <button type="submit">Add Post</button>
    </form>
  );
};

export default PostForm;
