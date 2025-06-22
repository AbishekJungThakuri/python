import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState('');
  const [releaseYear, setReleaseYear] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [newTitle, setNewTitle] = useState('');

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/books/");
        setBooks(response.data);
      } catch (err) {
        console.log(err);
        setError('Failed to fetch books.');
      }
    };
    fetchBooks();
  }, []);

  const addBook = async () => {
    if (!title || !releaseYear) {
      alert('Please fill in all fields.');
      return;
    }
    setLoading(true);
    setError('');

    const bookData = {
      title,
      release_year: parseInt(releaseYear),
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/books/create', bookData);
      setBooks((prevBooks) => [...prevBooks, response.data]);
      setTitle('');
      setReleaseYear('');
    } catch (err) {
      console.log(err);
      setError('Failed to add book.');
    } finally {
      setLoading(false);
    }
  };



  const updateTitle = async (pk, release_year) => {
    const bookData = {
      title: newTitle,
      release_year: parseInt(release_year),
    };
  
    try {
      const response = await axios.put(`http://127.0.0.1:8000/api/books/${pk}`, bookData);
      setBooks((prevBooks) =>
        prevBooks.map((book) => (book.id === pk ? response.data : book))
      );
      setNewTitle('');
    } catch (err) {
      console.log(err);
      setError('Failed to edit title.');
    } finally {
      setLoading(false);
    }
  };
  
  const handleDelete = async (pk) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/books/${pk}`);
      setBooks((prev) => prev.filter((book) => book.id !== pk));
    } catch (err) {
      console.log(err);
      setError('Failed to delete');
    }
  };
  


  return (
    <>
      <h1>Django And React</h1>
      <div>
        <input
          type="text"
          placeholder="Book Title..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="number"
          placeholder="Release Year..."
          value={releaseYear}
          onChange={(e) => setReleaseYear(e.target.value)}
        />
        <button onClick={addBook} disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </div>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div>
        {books.map((book) => (
          <div key={book.id}>
            <p>Title:{book.title}</p>
            <p>Release Year:{book.release_year}</p>
            <input type="text" placeholder='New Title...' value={newTitle} onChange={(e)=>setNewTitle(e.target.value)} />
            <button onClick={()=>updateTitle(book.id, book.release_year)}>Change Title</button>
            <button onClick={()=>handleDelete(book.id)} >Delete</button>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
