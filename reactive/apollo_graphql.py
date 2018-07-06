import subprocess

from charms.reactive import (
        when,
        when_not,
        set_flag,
        clear_flag
        )
from charmhelpers.core.hookenv import (
        status_set,
        open_port,
        close_port
        )
from charms.layer.nodejs import npm

@when('nodejs.available')
@when_not('apollo-graphql.installed')
def install_apollo_graphql():
    status_set('maintenance', 'installing graphql-demo')
    npm('install', '-g', 'github', 'n-pochet/graphql-demo')
    set_flag('apollo-graphql.installed')
    clear_flag('apollo-graphql.started')
    status_set('active', 'graphql-demo installed')

@when('apollo-graphql.installed')
@when_not('apollo-graphql.started')
def start_apollo_graphql():
    subprocess.Popen('graphql-demo')
    set_flag('apollo-graphql.started')

@when('apollo-graphql.started')
def expose_port():
    open_port(3000)

@when_not('apollo-graphql.started')
def unexpose_port():
    close_port(3000)

@when('apollo-graphql.started', 'website.available')
def configure_website(website):
    website.configure(port=3000)
