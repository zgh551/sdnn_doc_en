=====================
Lincense configration
=====================

Apply for license
=================

Before starting your work, you need to install license. please contact our FAE to get the license in detials. please provide the following information:

- **software envirment**：Linux Ubuntu version
- **user name**：both Chines and English
- **MAC address**：Server(host) MAC adrress
- **HostName**：host name

.. note::

   #. MAC address is the local host adrress, not Docker container address.
   #. HostName:  use  ``cat /etc/hostname`` to get host name.
   #. strongly recommand useing  **ubuntu** system.

Install license
===============

documentation
-------------

after geting your License file，plese refer to **install instruction linux.pdf**, the directory structure is follwing:

.. code-block:: bash
   :linenos:

   ├── check_license.sh
   ├── install instruction linux.pdf
   ├── license.readme
   ├── licserv_linux_x64_v11_15
   │             └── x64_lsb
   │                 ├── lmgrd
   │                 ├── lmutil
   │                 ├── xtensad
   │                 └── xtensa_lic_test-linux-64
   ├── start_license.sh
   ├── xtensa.lic
   └── xtensa.log

execute installation
--------------------

execute command:

.. code-block:: bash

   $ ./start_license.sh

after this execution，will generate  **xtensa.log** file.

check license
=============

execute ``check_license.sh`` script to get the status  of  **license** .

.. code-block:: shell
   :linenos:

   $ ./check_license.sh

sucessful installation
----------------------

the following output indicates sucessful installation of license:

.. code-block:: bash

   Feature                Version    #license    Vendor    Expires
   ------------------------------------------------------------------
   Xt_ISS_BASE_E2B6056E   14.0          1        xtensad  21-jul-2022
   Xt_XCC_FUSA_E2B6056E   14.0          1        xtensad  21-jul-2022
   Xt_XPLORER_SE          14.0          1        xtensad  21-jul-2022

failed installation
-------------------

If the following information is returned, it means that the license installation failed. Please check the ``xtensa.log`` file, which contains detailed error messages.

.. code-block:: bash

   Feature                Version    #license    Vendor    Expires
   ------------------------------------------------------------------

.. note::

   1. reconfirm  **MAC address** and **HOST Name** if it is consistent;
   2. confirm if the host port is occupied;

port occupancy problem
^^^^^^^^^^^^^^^^^^^^^^

If the ``xtensa.log`` file displays the following information, it means that the port of the license service has been occupied and cannot be opened.

.. code-block:: bash

   Failed to open the TCP port number in the license

At this time, you can query the process occupying the port by using the following command:

.. code-block:: bash

   $ netstat -natp | grep [port]


``kill`` relate process  **ID** , re-execute ``start_license.sh`` script.
