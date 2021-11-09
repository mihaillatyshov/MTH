import React from 'react'
import { getClassName } from '../../libs/GetCSS'
import cs from './NavBar.module.css'
import mainLogo from './logo.png'
import { Link } from 'react-router-dom'
import AuthButton from './AuthButton'

const NavBar = () => {
	return (
		<div className={getClassName(["container", cs.navBar])}>
			<div className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 ">
				<div className="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-light text-decoration-none">
					<Link to="/"> 
						<img src={mainLogo} alt="logo" className={cs.logo}/>
					</Link>
				</div>
				<div className="nav col-12 col-md-auto mb-2 justify-content-center text-light mb-md-0">
					<Link to="/graph"> 
						<input type="button" className="btn-sm btn-dark" value="Graph" />
					</Link>
				</div>
				<div className="text-light col-md-3 text-end">
					<AuthButton />
				</div>
			</div>
		</div>
	)
}

export default NavBar
