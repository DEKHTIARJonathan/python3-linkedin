__author__ = 'Samuel Marks <samuelmarks@gmail.com>'
__maintainer__ = "Marshall Humble <humblejm@gmail.com>"
__version__ = '0.2.0'

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from socketserver import ThreadingTCPServer
from http.server import SimpleHTTPRequestHandler

from webbrowser import open_new_tab
from json import dumps


from linkedin.linkedin import LinkedInAuthentication, LinkedInApplication

PORT = 8080

# ============ Client Application Credentials ============ #
# Can be found here: https://www.linkedin.com/developer/apps

CLIENT_ID = '<your Client ID>'
CLIENT_SECRET = '<Your Client secret>'


class LinkedInWrapper(object):

    def __init__(self, id, secret, port):
        self.id = id
        self.secret = secret

        self.callback_url = 'http://localhost:{0}/code/'.format(port)

        print("CLIENT ID: %s" % self.id)
        print("CLIENT SECRET: %s" % self.secret)
        print("Callback URL: %s" % self.callback_url)

        self.authentication = LinkedInAuthentication(
            self.id,
            self.secret,
            self.callback_url,
            permissions=['r_basicprofile',
                         'r_emailaddress',
                         'rw_company_admin',
                         'w_share']
        )

        # Note: edit permissions according to what you defined in the linkedin
        # developer console.

        self.application = LinkedInApplication(self.authentication)

        print("Please double check that the callback URL has been correctly "
              "added in the developer console ("
              "https://www.linkedin.com/developer/apps/), then open "
              "http://localhost:8080 in your browser\n\n")


lkin_api = LinkedInWrapper(CLIENT_ID, CLIENT_SECRET, PORT)

run_already = False

params_to_d = lambda params: {
    l[0]: l[1] for l in [j.split('=')
                         for j in urlparse(params).query.split('&')]
}


class CustomHandler(SimpleHTTPRequestHandler):
    def json_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsedurl = urlparse(self.path)
        authed = lkin_api.authentication.token is not None

        if parsedurl.path in ['/code/', '/code']:
            self.json_headers()

            lkin_api.authentication.authorization_code = \
                params_to_d(self.path).get('code')
            self.wfile.write(dumps({
                'access_token': lkin_api.authentication.get_access_token(),
                'routes': list([d for d in dir(lkin_api.application)
                                if not d.startswith('_')])
                }).encode('utf8'))
        elif parsedurl.path == '/routes':
            self.json_headers()

            self.wfile.write(dumps({
                'routes': list([d for d in dir(lkin_api.application)
                                if not d.startswith('_')])
                }).encode('utf8'))
        elif not authed:
            self.json_headers()

            if not globals()['run_already']:
                open_new_tab(lkin_api.authentication.authorization_url)
            globals()['run_already'] = True
            self.wfile.write(dumps({
                'path': self.path,
                'authed': type(lkin_api.authentication.token) is None
                }).encode('utf8'))
        elif authed \
                and len(parsedurl.path) \
                and parsedurl.path[1:] in dir(lkin_api.application):
            self.json_headers()
            self.wfile.write(dumps(
                getattr(lkin_api.application, parsedurl.path[1:])()
                ).encode('utf8'))
        else:
            self.json_headers(501)
            self.wfile.write(dumps({'error': 'NotImplemented'}).encode('utf8'))


if __name__ == '__main__':
    httpd = ThreadingTCPServer(('localhost', PORT), CustomHandler)

    print(('Server started on port:{}'.format(PORT)))
    httpd.serve_forever()
