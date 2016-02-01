# Core features

## Pollicino infrastructure
User model 

## Applications configuration
All the features are based on the `Application` entity. 

For now, we'll consider all features "scoped" or "isolated" into a separate environment for each application, so we will not able, 
for instance, to mix data between different applications

The application instance will keep track of:

* security tokens to be used to authenticate client apps (app token and client secrets)
* configuration for different services:
  * secrets and tokens for push notification
  * current default workflow for user signup
  * ...
  * ...
* other info and metadata such as app id and pages on stores

