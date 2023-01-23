import React, { useState, useEffect } from 'react'

const Search = () => {
  const [data, getData] = useState([])
  const dataSender = async (input) => {
    const URL = 'http://localhost:3444/api/v1/graph/suggestion';
    const body = JSON.stringify({search: input})
    const requestHeaders = new Headers({
      "Content-Type": "application/json",
      "Content-Length": JSON.stringify(body).length
    })
    console.log(JSON.stringify({search: input}))
      fetch(URL, {
        method: "POST",
        mode: "cors",
        headers: requestHeaders,
        body: body
      }).then((res) =>
        res.json())
      .then((response) => {
          console.log(response.result);
          getData(response.result);
    })
  }
  return (
    <>
      <form className='suggestion'>
        <input type="text" onChange={(e) => { dataSender(e.target.value);}}/>
        {data.map((val, i) => (
          <div key={i}>
            <li>Вам может быть интересно: { val }</li>
          </div>
        ))}
      </form>
      
    </>
  )
}
export default Search;