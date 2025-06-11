import { use, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
    const imageTable = [{id: 0, alt: "Mak", filename: "obraz1.jpg", category:1, downloads: 35},
    {id: 1, alt:"Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43},
    {id: 2, alt:"Dalmatyńczyk", filename: "obraz3.jpg", category:2, downloads: 2},
    {id: 3, alt:"Świnka morska", filename: "obraz4.jpg", category:2, downloads: 53},
    {id: 4, alt:"Rotwailer", filename: "obraz5.jpg", category:2, downloads: 43},
    {id: 5, alt:"Audi", filename: "obraz6.jpg", category:3, downloads: 11},
    {id: 6, alt:"kotki", filename: "obraz7.jpg", category:2, downloads: 22},
    {id: 7, alt:"Róża", filename: "obraz8.jpg", category:1, downloads: 33},
    {id: 8, alt:"Świnka morska", filename: "obraz9.jpg", category:2, downloads: 123},
    {id: 9, alt:"Foksterier", filename: "obraz10.jpg", category:2, downloads: 22},
    {id: 10, alt:"Szczeniak", filename: "obraz11.jpg", category:2, downloads: 12},
    {id: 11, alt:"Garbus", filename: "obraz12.jpg", category:3, downloads: 321}]
    const [flowers, setFlowers] = useState(true)
    const [animals, setAnimals] = useState(true)
    const [car, setCar] = useState(true)
  return (
    <>
      <h1>Galeria zdjęć</h1>
        <div className="d-flex flex-row">
            <div className="form-check form-switch">
            <input id="flowerInput" type="checkbox" className="form-check-input" checked={flowers}  onChange={()=>
                {
                    flowers? setFlowers(false) : setFlowers(true)
                }}
            />
            <label htmlFor="flowerInput" className="form-check-label">Kwiaty</label></div>
        <div className="form-check form-switch">
            <input id="animalInput"  type="checkbox" className="form-check-input" checked={animals} onChange={()=>
            {
                animals? setAnimals(false) : setAnimals(true)
            }}
            />
            <label htmlFor="animalInput" className="form-check-label">Zwierzęta</label>
        </div>
        <div className="form-check form-switch">
            <input id="carInput" type="checkbox" className="form-check-input" checked={car} onChange={()=>
                {
                    car? setCar(false) : setCar(true)
                }}/>
            <label htmlFor="carInput" className="form-check-label">Samochody</label>
        </div>
        </div>

        <div className="d-flex flex-row flex-wrap">
            {imageTable.map(element=>{
                if ((element.category == 1 && flowers)||(element.category == 2 && animals)||(element.category == 3 && car)){
                    const [downloads, setDownloads] = useState(element.downloads)
                    return <div>
                        <img src={"/src/assets/"+element.filename} alt={element.alt} className="rounded-3"/>
                        <h4>Pobrania: {downloads}</h4>
                        <button onClick={()=> {
                            setDownloads(downloads + 1)
                            element.downloads = downloads +1
                            console.log(imageTable[element.id])
                        }} className="btn btn-success">Pobierz</button>
                    </div>
                }
            })}
        </div>
    </>
  )
}

export default App
