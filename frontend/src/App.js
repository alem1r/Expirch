import React, { useState } from 'react';
import logo from './logo.png'; 
//import './App.css';
import "./prova.css";
function App() {

  const [ title, setTitle ] = useState("");
  const [ email, setMail ] = useState("");
  const [ nameFile, setFile ] = useState();
 

  const newBook = () => {
    const uploadData = new FormData();
    uploadData.append('title', title);
    uploadData.append('nameFile', nameFile, nameFile.name);
    alert("Your file is being uploaded! You can click send email")
    fetch('https://2bd6-2a02-8084-9042-5c00-93ed-d109-19b7-48d4.eu.ngrok.io/products/', {
      method: 'POST',
      body: uploadData
    })
    .then( res => console.log(res))
    .catch(error => console.log(error))
  }


  const send = () => {

    const uploadData = new FormData();
    uploadData.append('email', email);
    uploadData.append('title', title);
    uploadData.append('nameFile', nameFile, nameFile.name);
    alert("Email sent!")
    fetch('https://2bd6-2a02-8084-9042-5c00-93ed-d109-19b7-48d4.eu.ngrok.io/test/', {
      method: 'POST',
      body: uploadData
    })
    
  }

  return (

  /*  
 <html>
  <body className="App">
    <div >
      <h3>EXPIRCH</h3>
      <label>
        Title
        <input type="text" value={title} onChange={(evt) => setTitle(evt.target.value)}/>
      </label>
      <label>
        EMAIL
        <input type="text" value={email} onChange={(evt) => setMail(evt.target.value)}/>
      </label>
      <br/>
      <label>
        nameFile
        <input type="file" onChange={(evt) => setFile(evt.target.files[0])}/>
      </label>
      <br/>
      <button onClick={() => newBook()}>UPLOAD</button>
      <br/>
      <button onClick={() => send()}>COMPUTE</button>
    </div>
    </body>
    </html>
*/

<html> 


<div class="login-box">
<img src={logo} alt="Logo" />
  <body>

  </body>

  <h2>Expirch</h2>
  
  <form>
    <div class="user-box">
    <input type="text" value={title} onChange={(evt) => setTitle(evt.target.value)}/>
      <label>Name of the food</label>
    </div>
    <div class="user-box">
    <input type="file" onChange={(evt) => setFile(evt.target.files[0])}/>
      <label>Photo</label>
    </div>
    <div class="user-box">
    <input type="text" id="em" required value={email} onChange={(evt) => setMail(evt.target.value)}/>
      <label>Email</label>
    </div>
    <div class="user-box">
    <button type="button" id="up" disabled={!title} onClick={() => newBook()}>Upload</button>
    </div>
    <div class="user-box">
    <button type="button" id="sem" disabled={!email} onClick={() => send()}>Send Email</button>
    </div>
  </form>


</div>

</html>

  );
}

export default App;