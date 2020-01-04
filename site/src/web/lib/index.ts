import { ProductAPI } from './product'
import { CategoryAPI } from './category'
import { SessionAPI } from './session'
import { SessionBasketProductAPI } from './session_basket_product'
import { URLs } from './base'
import { LoginAPI, LogoutAPI } from './auth'
import { ProductImageAPI } from './product_image'
import { BasketProductAPI } from './basket_product'
import { ProductCategoryAPI } from './category_product'

export {
    URLs,
}

export const Product = new ProductAPI()
export const Category = new CategoryAPI()
export const ProductCategory = new ProductCategoryAPI()
export const Image = new ProductImageAPI()
export const Login = new LoginAPI()
export const Logout = new LogoutAPI()
export const BasketProduct = new BasketProductAPI()
export const Session = new SessionAPI()
export const SessionBasketProduct = new SessionBasketProductAPI()
