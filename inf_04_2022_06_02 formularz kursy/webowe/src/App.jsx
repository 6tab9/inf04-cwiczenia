import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import React from 'react'
import './App.css'

function App() {
  let kursyLista = ["Programowanie w C#","Angular dla początkujących", "Kurs Django"]
  let credentials = React.createRef()
  let kursNumber = React.createRef()
  function handleForm(e){
    e.preventDefault()
    console.log(credentials.current.value)
    if (kursyLista.length >= kursNumber.current.value){
      console.log(kursyLista[kursNumber.current.value-1])
    }
    else{
      console.log("Nieprawidłowy numer kursu")
    }
  }
  return (
    <>
      <h2>Liczba kursów: {kursyLista.length}</h2>
      <ol>
        {
          kursyLista.map(el=>{
            return <li>{el}</li>
          })
        }
      </ol>
      <form className='form d-flex flex-column justify-content-center gap-10'>
        <label htmlFor="credentials">Imię i nazwisko</label>
        <input type="text" name='credentials' ref={credentials}/>
        <label htmlFor="chosenKurs">Numer Kursu</label>
        <input type="number" name="chosenKurs" id="chosenKurs" ref={kursNumber}/>
        <button onClick={handleForm} className='btn btn-primary m-10'>Zapisz Do kursu</button>
      </form>
    </>
  )
}

export default App
