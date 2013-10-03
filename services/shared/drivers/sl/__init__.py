from SoftLayer import Client

from services.common.babelfish import before_hooks
from services.shared.drivers.sl.auth import get_auth


def get_client(req, resp, kwargs):
    client = Client()
    client.auth = None
    req.env['tenant_id'] = None

    if req.headers.get('x-auth-token'):
        auth, token, err = get_auth(req, resp)
        if err:
            return err
        client.auth = auth

        account = client['Account'].getObject()
        req.env['tenant_id'] = str(account['id'])

    req.env['sl_client'] = client

before_hooks.append(get_client)