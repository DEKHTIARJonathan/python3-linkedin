from linkedin import linkedin

CLIENT_ID = '<your Client ID>'
CLIENT_SECRET = '<Your Client secret>'

RETURN_URL = 'http://localhost:8080/code/'

authentication = linkedin.LinkedInAuthentication(
                    CLIENT_ID,
                    CLIENT_SECRET,
                    RETURN_URL,
                    linkedin.PERMISSIONS.enums.values()
                )

# Note: edit permissions according to what you defined in the linkedin
# developer console.

authentication.authorization_code = '#########################################'
result = authentication.get_access_token()

print("Access Token:", result.access_token)
print("Expires in (seconds):", result.expires_in)
