..
 This work is licensed under a Creative Commons Attribution 3.0 Unported
 License.

 http://creativecommons.org/licenses/by/3.0/legalcode

======================
Distributed DB Backend
======================

`bp distributed-db-backend <https://blueprints.launchpad.net/keystone/+spec/distributed-database-backend>`_

We propose the addition of an optional driver for keystone backends, one that is based on a NoSQL database.

Problem Description
===================

Currently MySQL, the default backend for keystone, is a single point of failure in the system which impacts availability of the keystone service. 

Proposed Change
===============

We propose to add a new driver which uses a NoSQL backend. The backend is MagnetoDB, which provides a DynamoDB API, and is implemented on top of Cassandra.

Alternatives
------------

Use Cassandra directly instead of using MagnetoDB as a backend. The advantage
MagnetoDB provides is it has a pluggable backend. So it gives an opportunity
to use different NoSQL backends like HBase, Riak with the same apis.

Security Impact
---------------

None.

Notifications Impact
--------------------

None.

Other End User Impact
---------------------

None.

Performance Impact
------------------

None.

Other Deployer Impact
---------------------

This is going to be another driver. Deployers are free not to use it and
use default MySQL driver. But if it is used then MagnetoDB service has to
be deployed to make this driver work. MagnetoDB in turn uses Cassandra to
store data. So Cassandra has to be deployed as well. Proposed configuration 
changes are as follows:

* Add a new paramter magnetodb_api_endpoint in database section.

This driver is going to reside in backend directory of each keystone backend.
So the driver should be changed for each backend if the new driver is used.

Developer Impact
----------------

None.

Implementation
==============

Assignee(s)
-----------

Primary assignee:
  <ajayaa>

Other contributors:

* <rushiagr>
* <yogeshwars>
* <vivekd>

Work Items
----------

Schema design and code for following backends:

* Token
* Identity
* Credential
* Catalog
* Trust
* Policy
* Assignment

Dependencies
============

* As mentioned above MagnetoDB and the library it depends on will be needed.
  Similarly Cassandra needs to be installed as well.

* `MagneotDB global secondary index
  <https://review.openstack.org/#/c/143945/>`_


Documentation Impact
====================

The new driver needs to documented.

References
==========

* `Blueprint
  <https://blueprints.launchpad.net/keystone/+spec/distributed-database-backend>`_

* `MagnetoDB
  <https://github.com/stackforge/magnetodb>`_

* `MagnetoDB documentation
  <http://magnetodb.readthedocs.org/en/latest/>`_
