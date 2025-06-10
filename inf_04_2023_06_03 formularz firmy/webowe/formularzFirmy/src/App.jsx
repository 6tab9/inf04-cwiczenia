import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import React from 'react'
import './App.css'
function App() {

    var movieTitle = React.createRef()
    var movieType = React.createRef()
    const movieAlert = (e) => {
        e.preventDefault()
        alert(JSON.stringify({
            title:movieTitle.current.value,
            kategoria:movieType.current.value
        }))
    }
    return (
        <>
            <form onSubmit={movieAlert}>
                <label htmlFor="title" className="w-75">Tytuł filmu</label>
                <input ref={movieTitle} type="text" name="title" id="title"  className="w-75"/>
                <label htmlFor="type" className="w-75">Rodzaj</label>
                <select ref={movieType} name="type" id="type" className="w-75">
                    <option default></option>
                    <option value="1">Komedia</option>
                    <option value="2">Obyczajowy</option>
                    <option value="3">Sensacyjny</option>
                    <option value="4">Horror</option>
                </select><br/>
                <button className="btn btn-primary" >Dodaj</button>
            </form>
        </>
    )
}

export default App
