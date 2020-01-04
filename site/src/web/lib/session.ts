import { id, DEEP, URLs, SHALLOW, ObjectAPI } from './base'
import { User } from './user'

export interface Session<D> {
    id: id
    user: User
}

export class SessionAPI extends ObjectAPI<Session<SHALLOW>, Session<DEEP>>
{
    public readonly URL: string = URLs.SESSION
}
