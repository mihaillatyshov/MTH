import React, { useState, useEffect } from 'react'
import { ServerAPI_POST } from '../../libs/ServerAPI';
import './Search.css'

const Search = () => {
  const [data, getData] = useState([])
  const dataSender = (e) => {
    console.log(e.target.value)
    ServerAPI_POST({
			url : "/api/v1/graph/suggestion",
      sendObj: {
        search: e.target.value
      },
			onDataReceived : (res) => {
        getData(res.result);
      }
		})
  }
  return (
    <form className='suggestion'>
      <input type="text" onChange={dataSender}/>
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