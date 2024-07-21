import React from 'react'
import '../styles/styles.css'

export default function Home() {

    const handleSubmitOptions = (event) => {
        event.preventDefault()

    
    }


  return (
    <div className='wrapper_page'>
        <div className='page'>
            <div className='wrapper_Title'>
                <h1>Bruteforcer</h1>
            </div>
            <div className='wrapper_description'>
                <p>You can brute force websites with this site. Use it <span>ETHICALLY</span></p>
            </div>
            <div className='wrapper_form_fruteforce'>
                <div className='wrapper-url'>
                    <label for="url_user">URL to test: </label>
                    <input id='url_user' className='input-url'></input>
                </div>
                <div className='wrapper_add_component'>
                    <form action='' className='form_to_add_options' onSubmit={handleSubmitOptions}>
                    <label for='select-options'>Choose options: </label>
                    <select name='options' id='select-options'>
                        <option value="">---Please choose an option---</option>
                        <option value="button">Button</option>
                        <option value="input">Input</option>
                        <option value="input-wordlist">Input-Wordlist</option>
                        <option value="link">Link</option>
                        <option value="boucle">Boucle</option>
                    </select>
                    <button className='button_to_add'>Add</button>
                    </form>
                </div>
            </div>
            <div className='wrapper_schema'>
            
            </div>        
        </div>
    </div>
  )
}
