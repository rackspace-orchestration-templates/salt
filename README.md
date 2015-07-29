[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/salt/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/salt)
Description
===========

This is a template for deploying [SaltStack](http://www.saltstack.com/). It
will deploy a salt master and a number of minions that communicate over a
private network.

Requirements
============
* A Heat provider.
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the
[python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
  <TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
  stack-create Salt-Stack -f salt.yaml -P number_of_minions=5
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as
the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these
values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `image`: Operating system to install (Default: Ubuntu 12.04 LTS (Precise
  Pangolin))
* `master_flavor`: Cloud server size to use for the Salt Master (Default: 2 GB
  Performance)  
* `minion_flavor`: Cloud server size to use for all minions (Default: 1 GB
  Performance)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value fo a specific output.

* `private_key`: SSH private that can be used to login as root to the server.
* `salt_master_ip`: Public IP address of the Salt Master
* `minion_public_ips`: Array of all minion public IPs

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
If you are new to [Salt Stack](http://www.saltstack.com/), check out their
[online documentation](http://docs.saltstack.com/) for information on how to
get started. This deployment handles the setup and configuration of the Salt
Master as well as the minions. When you connect to your salt master via SSH,
you can immediately begin issuing commands to your minions. The SSH Private Key
provided will work on all nodes of your deployment.

Getting Started
---------------
Connect to the salt master via SSH using the Private key provided in the
outputs.  Once logged in, list and accept the Salt keys using the `salt-key`
command.  Here are examples of how to list and accept those keys:

```bash
root@salt-master:~# salt-key
Accepted Keys:
Unaccepted Keys:
salt-minion0
salt-minion1
Rejected Keys:

root@salt-master:~# salt-key -A
The following keys are going to be accepted:
Unaccepted Keys:
salt-minion0
salt-minion1
Proceed? [n/Y] Y
Key for minion salt-minion0 accepted.
Key for minion salt-minion1 accepted.

root@salt-master:~#
```

Once the keys are accepted, you can begin managing your minions.  To run a
command on on all minions, use `cmd.run`.  Here's an example where we want to
find the IPv4 address of the eth2 interace of the minions:

```bash
root@salt-master:~# salt '*' cmd.run 'ifconfig eth2 | grep "inet addr"'
salt-minion1:
              inet addr:192.168.224.2  Bcast:192.168.239.255  Mask:255.255.240.0
salt-minion0:
              inet addr:192.168.224.3  Bcast:192.168.239.255  Mask:255.255.240.0
root@salt-master:~#
```

Scaling Out
-----------
For scaling your deployment, we recommend using [Salt
Cloud](http://docs.saltstack.com/en/latest/topics/cloud/config.html). The
`salt-cloud` package has been installed as a part of this deployment. An
example for configuring Salt Cloud with Rackspace can be found
[here](http://docs.saltstack.com/en/latest/topics/cloud/config.html#rackspace).

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
