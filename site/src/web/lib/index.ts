import {LoginAPI, LogoutAPI} from './auth'
export * from './base'

export const Login = new LoginAPI()
export const Logout = new LogoutAPI()
