# Design overview

## Why

Many mobile apps share the same server side requirements. 

This is a single server implementation providing:
* common ready to use services (think of builtins)
* configurable layer of services for common use cases (think of reusable apps)
* extensibility via python code (think of custom modules)

## What

We want to provide server side support for mobile apps, which includes:

* [Authentication](docs/design/authentication.md)
* [Push notifications] (docs/design/push_notifications.md)
* [Cloud database] (docs/design/cloud_database.md)
* [Analytics] (docs/design/analytics.md)

This will be provided by a django based web application.

The platform should have the following features:

* Support for multiple client applications
* Have a web based user interface
* Expose a REST API
* Be extensible with python code
* Be easily deployable to common infrastructures

## Future

* Static assets
* Async tasks
* Proxy
