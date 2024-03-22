import { useState, useEffect} from 'react'
import axios from 'axios'

function App() {
  const [buku, setBuku] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/buku/');
      const data = response.data;
      setBuku(data);
    };

    fetchData();
  }, []);

  return (
    <>
      <div>
      {buku.map((buku, index) => (
        <div key={index}>
          <h2>{buku.judul_buku}</h2>
          <p>{buku.pengarang}</p>
          <p>{buku.jenis_buku}</p>
          <img src={buku.cover} alt="Gambar" style={{ width: '200px', height: 'auto' }} />
        </div>
      ))}
      </div>
    </>
  )
}

export default App
