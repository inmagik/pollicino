# Push notifications

Push notifications are a common feature of mobile applications. Normally, these are provided by calling external services (run by mobile OS maintainers such as Google and Apple) using some sort of authenticated API.

Push mechanisms are implemented in different ways for different platforms, possibily requiring different implementations for:

* workflows
* configurations
* messages payload structure

All push notification mechanisms involve sending some message to a list of devices identified by a unique id.

## Features

* A common configuration point for push notifications, including authentication tokens and certificates for the different platforms
* A common interface to send debug and production notifications to a set of users or to all users of a mobile applications
* A common workflow and registry for registered devices, including platform profiling and optional linking to application users (see also design docs about authentication)


## Implementation ideas
