import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchPosts } from '../redux/postsSlice';

const PostsList = () => {
  const dispatch = useDispatch();
  const { posts, loading, error } = useSelector((state) => state.posts);

  useEffect(() => {
    dispatch(fetchPosts());
}, [dispatch]);

if (loading) return <div>Loading...</div>;
if (error) return <div>Error: {error}</div>;

return (
  <div>
      <h2>Posts</h2>
      <ul>
          {posts.map((post) => (
              <li key={post.id}>
                  <div className="post-title">{post.title}</div>
                  <div className="post-body">{post.body}</div> {/* Ensure this line is present */}
              </li>
          ))}
      </ul>
  </div>
);
};

export default PostsList;