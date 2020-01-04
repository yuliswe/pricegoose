import { id, DEEP, URLs, SHALLOW, ObjectAPI } from './base'
import { Basket } from './basket'

export class SessionBasketAPI extends ObjectAPI<Basket<SHALLOW>, Basket<DEEP>>
{
    public readonly URL: string = URLs.SESSION_BASKET
}
