import React, { useContext, useEffect } from 'react'
import { Link  } from "react-router-dom";
import { ServerAPI_GET } from '../../libs/ServerAPI';
import { LoginContext, setLoginContext } from '../../contexts/LoginContext';
import { getClassName } from '../../libs/GetCSS';
import cs from './NavBar.module.css'
import profileLogo from './profile.png'

const AuthButton = () => {
	const loginContext = useContext(LoginContext)

	useEffect(() => {
		ServerAPI_GET({ 
			url:"/islogin",
			onDataReceived : (data) => {
				setLoginContext({isAuth : data.isAuth})
				console.log(data)
			} 
		})
	}, [])

	return (
		<div>
			{
			loginContext.isAuth === undefined ? (
				<div>Loading... </div>
			) : (
				loginContext.isAuth ? (
					<div>
						<Link to="/profile">  
							<img src={profileLogo} alt="logo" className={cs.logo}/>
						</Link>
					</div>
				) : (
					<div>
						<Link to="/login"> <input type="button" className={getClassName(["btn-sm btn-dark", cs.AuthButton])} value="Login" /> </Link>
					</div>
				)
			)
			}
		</div>
	)
}

export default AuthButton
