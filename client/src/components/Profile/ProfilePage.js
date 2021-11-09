import React from 'react'
import Profile from './Profile';
import ProfileNav from './ProfileNav';

const ProfilePage = () => {



	return (
		<div className="container">
			<div className="row">
				<ProfileNav />
				<Profile />
			</div>
		</div>
	)
}

export default ProfilePage
