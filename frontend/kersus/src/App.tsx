import { useState } from 'react';
import { z } from 'zod';
import axios from 'axios';

const categoryForm = z.object({
  user: z.number().int().positive(),
  name: z.string().min(1).max(255),
  description: z.string().min(1).max(255),
})

export default function App(){
  const [user, setUser] = useState(1);
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (event: { preventDefault: () => void; }) => {
    event.preventDefault();
    
    const url = 'http://localhost:8000/api/category/'
    const headers = {
      'Content-Type': 'application/json',
    }
    
    try {
      const data = {
        user,
        name,
        description,
      };

      const validatedData = categoryForm.parse(data);
      console.log(validatedData);

      await axios.post(url, validatedData, { headers });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">
        Name:
        <input type="text" value={name} onChange={(event) => setName(event.target.value)} />
      </label>
      <br />
      <label htmlFor="description">
        Description
        <input type="text" value={description} onChange={(event) => setDescription(event.target.value)} />
      </label>
      <br />
      <button type="submit">Submit</button>
      </form>
  )
}