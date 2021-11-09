import React, { useState } from 'react'
import { Link, useHistory  } from "react-router-dom";
import { ServerAPI_POST } from '../../libs/ServerAPI';
import cs from './Auth.module.css'

const RegisterPage = () => {
	const history = useHistory();
	const [email, 		setEmail] 		= useState("");
	const [nickname, 	setNickname] 	= useState("");
	const [name, 		setName] 		= useState("");
	const [password1, 	setPassword1] 	= useState("");
	const [password2, 	setPassword2] 	= useState("");
	const [message, 	setMessage] 	= useState(undefined)

	const handleSubmit = (e) => {
		e.preventDefault()

		ServerAPI_POST({
			url : "/register",
			sendObj : {
				email : email,
				nickname : nickname,
				name : name,
				password1 : password1,
				password2 : password2
			},
			handleStatus : (result) =>
			{
				setMessage(result.data.message)
				//console.log("Data", data)
			},
			onDataReceived : () => {
				history.push("/")
			}
		})
	}

	return (
		<div className={cs.form} >
			{ message && <h3> {message} </h3> }
			<form onSubmit={handleSubmit} className="g-3">
				<div className="mb-3">
					<label htmlFor="email" 		className="form-label"> Email address </label>
					<input type="email" 		className="form-control" id="email" 	required 	value={email} 		onChange={(e) => { setEmail(e.target.value) }} />
				</div>
				<div className="mb-3">
					<label htmlFor="nickname" 	className="form-label"> Nickname </label>
					<input type="text" 			className="form-control" id="nickname" 				value={nickname} 	onChange={(e) => { setNickname(e.target.value) }} />
				</div>
				<div className="mb-3">
					<label htmlFor="name"	 	className="form-label"> Name </label>
					<input type="text" 			className="form-control" id="name" 					value={name} 	onChange={(e) => { setName(e.target.value) }} />
				</div>
				<div className="mb-3">
					<label htmlFor="password1" 	className="form-label"> Password </label>
					<input type="password" 		className="form-control" id="password1" required 	value={password1} 	onChange={(e) => { setPassword1(e.target.value) }} />
				</div>
				<div className="mb-3">
					<label htmlFor="password2" 	className="form-label"> Password </label>
					<input type="password" 		className="form-control" id="password2" required 	value={password2} 	onChange={(e) => { setPassword2(e.target.value) }} />
				</div>
				<div className="mb-3">
					<Link to="/register">Don't have an account? Register! </Link>
				</div>
				<input type="submit" className="btn btn-primary" value="Register" />
			</form>
		</div>
	)
}

export default RegisterPage
