from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication, PERMISSIONS)

if __name__ == '__main__':
  
    CLIENT_ID     = '############'
    CLIENT_SECRET = '#############'
    RETURN_URL = 'http://localhost:8000/callback/'
    
    authentication = LinkedInAuthentication(
                        CLIENT_ID,
                        CLIENT_SECRET,
                        RETURN_URL,
                        PERMISSIONS.enums.values()
                    )
    
    print(authentication.authorization_url)
    application = LinkedInApplication(authentication)
