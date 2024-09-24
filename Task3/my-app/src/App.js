import React from 'react';
import PostsList from './components/PostsList';
import PostForm from './components/PostForm';
import './App.css';
function App() {
  return (
    <div className="App">
      <h1>Post list</h1>
      <PostForm />
      <PostsList />
    </div>
  );
}

export default App;
