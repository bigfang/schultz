HEADLESS_ONLY = True
HEADLESS_FRONTEND_URLS = {
    'account_confirm_email': '/account/verify-email/{key}',
    'account_reset_password': '/account/password/reset',
    'account_reset_password_from_key': '/account/password/reset/{key}',
    'account_signup': '/account/signup',
}

ACCOUNT_SIGNUP_FIELDS = ['username*', 'email*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_USERNAME_MIN_LENGTH = 6
