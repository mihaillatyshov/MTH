import React, { useState, useContext } from 'react'
import NavBar from './components/NavBar/NavBar'
import Nodes from './components/Nodes/Nodes'
import { BrowserRouter, Switch, Route } from "react-router-dom";
import ProfilePage from './components/Profile/ProfilePage';
import StartPage from './components/StartPage/StartPage';
import PageNotFound from './components/PageNotFound';
import { LoginContext, setLoginContextChange } from './contexts/LoginContext';
import LoginPage from './components/Authentication/LoginPage';
import RegisterPage from './components/Authentication/RegisterPage';

function App() {
	const [loginContext, setLoginContext] = useState(useContext(LoginContext))

	setLoginContextChange((newContext) => {
		setLoginContext(newContext)
	})

	return (
		<BrowserRouter>
			<LoginContext.Provider value={loginContext} >
				<div className="App">
					<NavBar />
					<div className="container">
						<Switch>
							<Route path="/" exact 		render={() => <StartPage 	/>} />
							<Route path="/profile" 		render={() => <ProfilePage 	/>} />
							<Route path="/login" 		render={() => <LoginPage 	/>} />
							<Route path="/register" 	render={() => <RegisterPage />} />
							<Route path="/graph/:id?" 	render={() => <Nodes 		/>} />
							<Route 						render={() => <PageNotFound />} />
						</Switch>
					</div>
				</div>
			</LoginContext.Provider>
		</BrowserRouter>
	);
}

export default App;
