====================
Docker configuration
====================

Docker is SDNN development envirnoment, includes：

- basic development software
- related toolchain with Hardwared
- related toolchain with OS

Docker installation
===================

user need to install Docker environment on **PC**, please refer to：https://docs.docker.com/get-docker/

.. note::

   recommended OS: **Ubuntu 18.04.5 LTS**.

Import image
============

download the latest SDNN image from  Semidriver customer support https://support.semidrive.com/
we provide a variety of images，user can download the images as needed.

the following steps are for SlimAI depolyed on Linux:

#. basic environment: ``sdrv_tvm_base_1_0.zip``
#. accelerator: ``xnnc_2.4.zip`` and ``xtensa_2021_7.zip``
#. operation systerm: ``linux_env_yocto_2_5_3.zip``

.. note::

   up to know, we support **linux** , **android** and **qnx** operation systerm models depolyment environment.

Unzip the image
---------------

.. code-block:: bash
   :linenos:

   $ unzip sdrv_tvm_base_1_0.zip
   $ unzip xnnc_2_4.zip
   $ unzip xtensa_2021_7.zip
   $ unzip linux_env_yocto_2_5_3.zip


check the tar package which been generated in your current director:

.. code-block:: shell
   :linenos:

   $ ls *.tar
   linux_env_yocto_2_5_3.tar  sdrv_tvm_base_1_0.tar  xnnc_2_4.tar  xtensa_2021_7.tar

Load image
----------

exexcute ``docker load``  load  **tar** package:

.. code-block:: shell
   :linenos:

   $ docker load < xnnc_2_4.tar
   $ docker load < xtensa_2021_7.tar
   $ docker load < linux_env_yocto_2_5_3.tar
   $ docker load < sdrv_tvm_base_1_0.tar

check whether or not the image has been successfully loaded:

.. code-block:: shell
   :linenos:

   $ docker images

   REPOSITORY      TAG           IMAGE ID       CREATED        SIZE
   tvm_base        1.0           0b2ffdde775d   17 hours ago   12.7GB
   xnnc            2.4           8e9ee914c256   2 days ago     1.7GB
   linux_env       yocto_2.5.3   6726aca913ff   9 days ago     4.82GB
   xtensa          2021.7        e4c0657ac1e8   2 weeks ago    10.2GB

create container
================

there are two steps:

volume container
----------------

fist, create the volume container of toolchain：

.. code-block:: shell
   :linenos:

   $ docker create --name xtensa_2021_7 xtensa:2021.7 /bin/sh
   $ docker create --name xnnc_2_4 xnnc:2.4 /bin/sh
   $ docker create --name linux_env_yocto_2_5_3 linux_env:yocto_2.5.3 /bin/sh

.. note::

   - you can name the volume container andything you want.
   - when sharing volume container in parralel development，if the tool chain has been modified，all of developer would be impacted.so we suggust every user create their own volum container.

SDNN development container
--------------------------

When Creating SDNN container, you need to load volume container and mount local working directory:

.. code-block:: shell

   docker run -it --rm
          --name ${container name} \
          --volumes-from {volume container} \
          -v ${mount host directory}:${mapped directory} \
          -e ${config the container of enviroment variables}\
          ${ Repository name}：${lable name}  /bin/bash \

specific example is shown below：

.. code-block:: shell
   :linenos:

   $ docker run -it \
            --name tvm_$USER \
            -v ${PWD}:$HOME \
            --volumes-from xnnc_2_4 \
            --volumes-from xtensa_2021_7 \
            --volumes-from linux_env_yocto_2_5_3 \
            -e XTENSAD_LICENSE_FILE="27030@10.18.10.241" \
            -e XTENSA_SYSTEM="/opt/xtensa/XtDevTools/install/builds/RI-2021.7-linux/vision_dsp/config" \
            -e PATH="/sdrv/llvm-12.0.1-linux-gnu/bin:/sdrv/llvm-10.0.1/bin:/opt/xtensa/XtDevTools/install/tools/RI-2021.7-linux/XtensaTools/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
            -e XTENSA_CORE="vision_dsp" \
            -e XTENSA_CORE_TYPE="dsp" \
            tvm_base:1.0 /bin/bash

.. note::

   #. you can customize the container name, Repository name and lable name must consistent with the image loaded.
   #. **XTENSAD_LICENSE_FILE** ="27030@10.18.10.241" is vitial environment variables. only **XTENSAD_LICENSE_FILE** need to be modifid according user enviroment. others can use the default .  
   #. "27030@10.18.10.241" need to being replaced by user serve IP and port.
   #. refer to **chapter1**  license check. execute /check_license.sh to get License server status.


Enter container
===============

check the container created
---------------------------

.. code-block:: bash
   :linenos:

   $ docker ps -a
   7c5993971858   tvm_base:1.0            "/bin/bash"              3 weeks ago    Up 3 weeks                          tvm_base_linux_1_0_user
   009902f3ed26   qnx_env:710             "/bin/sh"                5 weeks ago    Created                             qnx_env_710
   e3a098b395a5   android_env:ndk_r23b    "/bin/sh"                5 weeks ago    Created                             android_env_ndk_r23b
   f37197b75f18   linux_env:yocto_2.5.3   "/bin/sh"                5 weeks ago    Created                             linux_env_yocto_2_5_3
   8aff9d99ef74   xnnc:2.4                "/bin/sh"                5 weeks ago    Created                             xnnc_2_4
   f2270c3a9439   xtensa:2021.7           "/bin/sh"                5 weeks ago    Created                             xtensa_2021_7

start container
---------------


.. code-block:: bash

   $ docker start ${container name}

enter container
---------------

.. code-block:: shell

   $ docker exec -it ${container name} bash

.. note::

   for other command, please refer to：https://docs.docker.com/engine/reference/commandline/cli/

QNX Docker configruation
========================

since QNX development need license，SDNN couldn't provide Docker image，follow these steps to create a QNX docker：

QNX Docker image and container
------------------------------

  please refer to  ``path/to/tvm/docker/qnx_create_readme.txt`` to create image. the step to creat a container is similar with Linxu.

Config QNX license
------------------

Being difference form Linux, QNX need to register licnese or else “license check failed” will print in log.

.. code-block:: bash

   $ qnxsoftwarecenter/qnxsoftwarecenter_clt
   -url https://qnx.com/swcenter -syncLicenseKeys -myqnx.user=<MYQNX_USER>
   -myqnx.password=<MYQNX_PASSWORD> -addLicenseKey <build_server_license_key>
   -listLicenseKeys

``qnxsoftwarecenter`` file directory and MYQNX_USER，MYQNX_PASSWORD，build_server_license_key, plese contact with QNX FAE to get support.
