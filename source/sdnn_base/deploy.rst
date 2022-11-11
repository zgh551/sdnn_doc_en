====================================
Deploy environment configuration
====================================

Get required runtime lib files form `Semidrive Customer support<https://www.semidrive.com/>`_ , or click and download them from links listed below:

.. tabs::

   .. tab:: Linux

      1. `linux_runtime installation package <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/aarch64-linux.tgz>`_
      2. `linux_opencv installer <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/opencv_deploy_linux.run>`_

   .. tab:: Android

      1. `development environment configuration script <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/android_envsetup.sh>`_
      2. `android_libcpp installer  <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/libcpp_shared_android.run>`_
      3. `android_runtime installation package <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/aarch64-android.tgz>`_
      4. `android_opencv installer  <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/opencv_deploy_android.run>`_

   .. tab:: QNX

      1. `qnx_runtime installation package <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/aarch64-qnx.tgz>`_


   .. important::

      #. The runtime lib version must align with sdnn_build version, or it may cause uncertainties.
      #. Please update the runtime lib in the deploy environment after each upgrade of the sdnn build tool in compile environment.


Deploy on Linux board
======================

Remount
---------

Because some libraries need to be installed to the system directory, you need to remount system to get read and write permissions to the root directory by following command:

.. code-block:: bash

   $ mount -o remount,rw /

Runtime lib installation
-----------------------------

First confirm whether current deploy environment contains the runtime library files. Generally runtime library resides in:

- ``/usr/lib``
- ``/usr/local/lib``
- ``/usr/sdrv/tvm``


Runtime lib already installed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If runtime library is already installed, but its version does not match with your upgraded sdnn_build tool, then you need to upgrade your runtime library to the matching new version. So you need to download the new libtvm_runtime.so and overwrite the old libtvm_runtime.so.

Runtime lib not installed
^^^^^^^^^^^^^^^^^^^^^^^^^^

Auto installation
""""""""""""""""""""""""""
Download **tvm_runtime_linux-deploy.run** to your pc, and upload it to any directory in the board linux system, run command:

.. code-block:: bash

   $ sh ./tvm_runtime_linux-deploy.run

then **libtvm_runtime.so** file would be installed to ``/usr/sdrv/tvm``


Manual installation
"""""""""""""""""""""""

Download libtvm-runtime.so file, then upload it to the directory you defined, finally add this directory to system dynamic library searching configuration file as follow:

1. **check ldconfig file**

Check whether ``ld.so.conf`` file exists in directory ``/etc``, if file does not exist, please create and add following to it:

.. code-block:: bash

   include /etc/ld.so.conf.d/*.conf

Check whether directory ``/etc/ld.so.conf.d`` exists, create it if the directory dose not exist. Create xxx.conf in this directory, and add runtime absolute path to this configure file.
finally update system dynamic library searching configuration by following command:

.. code-block:: bash

   $ ldconfig

OpenCV libraries installation
------------------------------

Test case code depends on OpenCV. So if OpenCV libraries are not installed in your deploy linux environment, copy auto installer from directory ``examples/vendor/OpenCV`` of test case code to your deploy environment, and run following command:

.. code-block:: bash

   $ sh ./opencv_deploy_linux.run

**OpenCV** libraries will be installed in directory ``/usr/sdrv/opencv``.

Deploy on Android board
========================

Adb environment setup
----------------------

Root device
^^^^^^^^^^^^^

.. code-block:: bash

   $ adb root

Remount
^^^^^^^^^

.. code-block:: bash

   $ adb remount

Open shell
^^^^^^^^^^^^

.. code-block:: bash

   $ adb shell

Environment variables setup
--------------------------------

Copy **android_envsetup.sh** from directory ``examples/vendor/Android`` of test case code to your deploy environment, run following command:

.. code-block:: bash

   $ source android_envsetup.sh

C++ libraries installation
---------------------------

Check whether **libc++_shared.so**  exists in directory ``/vendor/lib64``, if not, copy **libc++_shared_android.run** from directory ``examples/vendor/Android`` of test case code to your deploy environment, run following command:

.. code-block:: bash

   $ sh libc++_shared_android.run

Runtime lib installation
--------------------------

First confirm whether current deploy environment contains the runtime library files. Generally runtime library resides in:

- ``/vendor/lib``
- ``/vendor/lib64``
- ``/vendor/sdrv/tvm``

Runtime lib already installed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If runtime library is already installed, but its version does not match with your upgraded sdnn_build tool, then you need to upgrade your runtime library to the matching new version. So you need to download the new libtvm_runtime.so and overwrite the old libtvm_runtime.so.

Runtime lib not installed
^^^^^^^^^^^^^^^^^^^^^^^^^^

Auto installation
"""""""""""""""""""""

Download **tvm_runtime_android-deploy.run** to your pc, and upload it to any directory in the board Android system, run command:

.. code-block:: bash

   $ sh ./tvm_runtime_linux-deploy.run

then **libtvm_runtime.so** file would be installed to ``/vendor/sdrv/tvm``.

Manual installation
"""""""""""""""""""""""

Download libtvm-runtime.so file, then upload it to the directory ``/vendor/lib64/`` in your board Android system. If you want to install it to other directory, please configure environment variables **LD_LIBRARY_PATH** as:

.. code-block:: bash

   $ export LD_LIBRARY_PATH=path/to/your_lib_path

OpenCV libraries installation
------------------------------

Test case code depends on OpenCV. So if OpenCV libraries are not installed in your deploy Android environment, copy auto installer from directory ``examples/vendor/OpenCV`` of test case code to your deploy environment, and run following command:

.. code-block:: bash

   $ sh ./opencv_deploy_android.run

**OpenCV** libraries will be installed in directory ``/vendor/sdrv/opencv``.





Deploy on QNX board
=====================

Runtime lib installation
--------------------------

Just download and copy **libtvm_runtime.so** to directory ``/proc/boot/`` in your QNX system.


