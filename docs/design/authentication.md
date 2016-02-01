# Authentication

## Overview

A mobile app using the authentication service should be able to:

* signup a new user with username, email and password, and optional email validation
* login an user with username and password, providing a token for authenticated calls, with optional token expiration
* logout an user
* reset password for an user, via email
* get and set user information on behalf of user
* allow setting custom information on the user

If an user is available, it can be used in combination with other services such as:

* push notifications: link the current user object to the current installation object. This would allow push notifications targeted at a specific user or filtered by some properties of the user profile
* analytics: actions of specific users could be tracked
* database: when writing objects to the database, the current user can be specified for fields pointing to an user, for example an `owner` field on some kind of model.


## Signup

* A new user object should be created for the current app, with provided username, email, and password. 
* Username will be optional, and will be set to email if not provided
* An email validation could be required, if set on application configuration or in specific signup call
* A notification could be sent to the user on successful signup
* Email templates for signup events should be editable directly on the platform


## Login

A login action has two side effects:

* initiates an user session for the app
* sends back a token to the client, for allowing requests on behalf of the logged user

### username and password

### session token

#### session token expiration
* session token will expire with a configurable timing
* each request on the user session will refresh the session for the user
* in case of expiring session tokens, a second token is sent to the client on login (refresh_token), along with the datetime of session token expiration
* in case of request to a session with an expired token, a special error code will be sent back to the client, allowing the client to exchange the old token with a new token (and a new refresh token)
* clients could also implement an auto-refresh strategy by calling periodically the refresh endpoint and keeping a token "always fresh" in the client.


### session expiration
* an application wide option will control session expiration in case of inactive users


## Logout

Logout operation destroys the user session, invalidating the current token.

In case of an user linked to an installation, the link will be dropped.


## Password recovery

* allow user to recover their password by email
* the email template should be configurable on the platform, being a "setting" of the app.








