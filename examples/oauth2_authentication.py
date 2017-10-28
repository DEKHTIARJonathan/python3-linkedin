from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)

if __name__ == '__main__':

    CLIENT_ID = '<Your Client ID>'
    CLIENT_SECRET = '<Your Client secret>'
    RETURN_URL = 'http://localhost:8080/code/'

    authentication = LinkedInAuthentication(
                        CLIENT_ID,
                        CLIENT_SECRET,
                        RETURN_URL,
                        permissions=['r_basicprofile',
                                     'r_emailaddress',
                                     'rw_company_admin',
                                     'w_share']
                    )

    # Note: edit permissions according to what you defined in the linkedin
    # developer console.

    # Optionally one can send custom "state" value that will be returned from
    # OAuth server It can be used to track your user state or something else
    # (it's up to you) Be aware that this value is sent to OAuth server AS IS -
    # make sure to encode or hash it
    # authorization.state = 'your_encoded_message'

    print(authentication.authorization_url)
    application = LinkedInApplication(authentication)
