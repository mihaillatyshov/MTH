import React, { useState, useEffect } from 'react'
import { ServerAPI_POST } from '../../libs/ServerAPI';
import './Search.css'

const Search = () => {
  const [data, getData] = useState([])
  const dataSender = (input, e) => {
    const body = JSON.stringify({search: input})
    const requestHeaders = new Headers({
      "Content-Type": "application/json",
      "Content-Length": JSON.stringify(body).length
    })
    console.log(JSON.stringify({search: input}))
    ServerAPI_POST({
			url : "/api/v1/graph/suggestion",
      sendObj: {
        search: input
      },
			onDataReceived : (res) => {
        console.log(res.result);
        getData(res.result);
      }
		})
  }
  return (
      <form className='suggestion'>
        <input type="text" onChange={(e) => { dataSender(e.target.value);}}/>
        <div className='results'>
        {data.map((val, i) => (
          <div  key={i}>
            <li>Вам может быть интересно: { val }</li>
          </div>
        ))}
        </div>
      </form>
  )
}
export default Search;