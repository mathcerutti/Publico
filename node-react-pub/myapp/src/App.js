import React, {useState,useEffect} from 'react';
import Axios from 'axios';
import './App.css';
import Card from './components/cards/Card'

function App() {

  const [values,setValues] = useState()
  const [listGames,setListGames] = useState()

  console.log(listGames)
  
  const handleChangeValues = (value)=>{
    setValues(prevValue=>({
      ...prevValue,
      [value.target.name]:value.target.value,
    }))
  }

  const handleClickButton =()=>{
    Axios.post("http://localhost:3001/register", {
      name: values.name,
      cost: values.cost,
      category: values.category
    }).then((response)=>{
      console.log(response)
      /*setListGames([
        ...listGames,
        {
          name: values.name,
          cost: values.cost,
          category: values.category
        }
      ]*/
    })
  }

  useEffect(()=>{
    Axios.get("http://localhost:3001/getCards").then((response)=>{
      setListGames(response.data)
    })
  },[])

  return (
    <div className="App-container">
      <div className='register-container'>
        <h1>Scrim Shop</h1>
        <input 
        className='register-input' 
        type='text' name='name' 
        placeholder='Nome' 
        onChange={handleChangeValues}
        />
        <input 
        className='register-input' 
        type='text' 
        name='cost' 
        placeholder='Preço'
        onChange={handleChangeValues}
        />
        <input 
        className='register-input' 
        type='text' 
        name='category' 
        placeholder='Categoria'
        onChange={handleChangeValues}
        />
        <button onClick={handleClickButton}>Cadastrar</button>
      </div>
        {typeof listGames!== "undefined" && listGames.map((values)=>{
          return <Card key={values.id}
                      listCard={listGames}
                      setListCard={setListGames}
                      id={values.idgames}
                      name={values.name}
                      cost={values.cost}
                      category={values.category}
                      >
                      </Card>
        })}
    </div>
  );
}

export default App;
