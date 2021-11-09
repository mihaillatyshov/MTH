import React from 'react'

const context = 
{
	isAuth : undefined
}

let callback = () => {}

export const LoginContext = React.createContext(context)

export const setLoginContext = (newContext) => {
	callback(newContext)
}

export const setLoginContextChange = (newCallback) => {
	callback = newCallback
}
