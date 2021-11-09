import React, { useEffect, useState } from 'react'
import { ServerAPI_GET } from '../../libs/ServerAPI'
import profileLogo from './profile150.png'

const Profile = () => {
	const [profileInfo, setProfileInfo] = useState(undefined)

	useEffect(() => {
		ServerAPI_GET({ 
			url:"/profileinfo",
			onDataReceived : (data) => {
				setProfileInfo(data)
				console.log(data)
			} 
		})
	}, [])

	return (
		<div className="col">
			{
				profileInfo === undefined ? (
					<div>Loading... </div>
				) : (
					<div className="container">
						<div className="row">
							<div className="col-md-auto">
								<img src={profileLogo} alt="logo"/>
							</div>
							<div className="col">
								<div><h3> {profileInfo.nickname} ({profileInfo.name}) </h3></div>
								<div><h5> {profileInfo.email} </h5></div>
							</div>
						</div>
					</div>
				)
			}
		</div>
	)
}

export default Profile
