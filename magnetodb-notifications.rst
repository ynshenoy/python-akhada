..
  This work is licensed under a Creative Commons Attribution 3.0 Unported
  License.

  http://creativecommons.org/licenses/by/3.0/legalcode

  =======================
  MagnetoDB Notifications
  =======================

  https://blueprints.launchpad.net/magnetodb/+spec/magnetodb-notifications

  Notifications in MagnetoDB are already implemented. For example, when a
  table is created a notification called table.create.start is emmited and 
  when the table creation is finished a notification called table.create.end
  is emmited. 

  Problem description
  ===================

  The notifications sent by MagnetoDB needs to be fetched from message bus
  and then transformed into samples and then stored in the database. To
  achieve this a notification handler is needed.

  Proposed change
  ===============

  A new notification plugin for MagnetoDB to transform the notifications
  into samples using existing ``NotificationBase`` implementation as a model.

  Alternatives
  ------------

  Handling notifications is the preferred way for gathering data in ceilometer.

  Data model impact
  -----------------
  None.

  REST API impact
  ---------------
  There will be additional valid values in the query parameters but no changes
  to API endpoints.

  Security impact
  ---------------

  None.

  Pipeline impact
  ---------------

  None.

  Othe end user impact
  --------------------

  None.

  Performance/Scalability impacts
  -------------------------------

  No new impacts. As MagnetoDB is a highly available nosql datastore, there are
  a lot of notifications going to be generated.

  Other deployer impact
  ---------------------

  None.

  Developer impact
  ----------------

  None.

  Implementation
  ==============

  Assignee(s)
  -----------
  Primary assignee:
    ajayaa

  Other contributors:

  Work Items
  ----------

  * Establish expected data.

  * Create tests of transformation of notifications to samples.

  * Create notification plugin to consume notifications.

  * Create tests of notifications across fake bus.

  * Create sample query tests.

  Future lifecycle
  ================

  In the future new types of notifications are expected from the MagnetoDB.
  These will need to be handled either by additional notification
  plugins or (hopefully) generic notification handling. The Ceilometer team
  will
  be responsible for collaborating with the MagnetoDB team to ensure these are
  handled smoothly.

  Dependencies
  ============

  None.

  Testing
  =======

  Unittests.

  Documentation Impact
  ====================

  The added metrics will need to be documented in the `measurements section`_.

  .. _measurements section:
     http://docs.openstack.org/developer/ceilometer/measurements.html
