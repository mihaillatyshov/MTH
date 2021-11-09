import React from 'react'
import { Link, useHistory  } from "react-router-dom";
import { setLoginContext } from '../../contexts/LoginContext'
import { ServerAPI_POST } from '../../libs/ServerAPI'
import { getClassName } from '../../libs/GetCSS';
import cs from "./Profile.module.css"

const ProfileNav = () => {
	const history = useHistory();
	
	const handeleLogout = () => {
		ServerAPI_POST({ 
			url:"/logout",
			onDataReceived : () => {
				setLoginContext({isAuth : false})
				history.push("/")
			}
		})
	}

	return (
		<div className={getClassName(["col-3", cs.profileNav])}>
			<div>
				<Link to="/profile"> Профиль </Link>
			</div>
			<div>
				<Link to="/profile/graphs"> Сохраненные темы </Link>
			</div>
			<div>
				<input type="button" className="btn btn-dark" value="Logout" onClick={handeleLogout} />
			</div>
		</div>
	)
}

export default ProfileNav
