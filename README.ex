# Overview

This charm is used to demonstrate a very simple GraphQL application with Apollo and Express.


# Usage

Step by step instructions on using the charm:

* Clone the repository
* Build the charm:
```
charm build . --series xenial
```
* Deploy the charm:
```
juju deploy --series xenial .xenial/apollo-graphql
```

You can then browse to http://ip-address:3000/graphiql to play with the interface 
or use http://ip-address:3000/graphql as a GraphQL endpoint.

## Scale out Usage
No specific mechanism is used for scale-out

## Known Limitations and Issues

A lot of parameters are hard-coded (e.g.: IP address, port...)
