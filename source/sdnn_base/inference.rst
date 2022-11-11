================
Model inference
================

You can call the model interface API in application code to do inference via the compiled model. For how do model inference, please refer to ** examples **  repository code, which contains detailed user cases. Currently, two sets of interfaces are provided: ``standard TVM API`` and ``SDNN API``. Choose appropriate API set according to your application scenario.
If you just want to simply get performance or output of the compiled model given specific input, you can resort to to ``sdnn_test`` after uploading appropriate test tool to your board system.

Input and output layout
=========================

The input and output layout may change due to optimization, so you need refer to compile log for final layout format of compiled model.
At the end of optimization phase of compilation, you will see the layout infomation in the log as:

.. code-block:: bash

   INFO: Optimizing for bandwidth (96%): Clip_clip_1300__1_minClip_4_whd_dwh
   INFO: Optimizing for bandwidth (96%): Add_add_1330__3_whd
   INFO: Optimizing for bandwidth (97%): Conv_nn_conv2d_1350__8_whd
   INFO: Optimizing for bandwidth (97%): Clip_clip_1360__1_minClip_4_whd
   INFO: Optimizing for bandwidth (97%): Clip_clip_1390__1_minClip_4_whd
   INFO: Optimizing for bandwidth (98%): Conv_nn_conv2d_1430__7_whd
   INFO: Optimizing for bandwidth (98%): Clip_clip_1440__1_minClip_4_whd
   INFO: Optimizing for bandwidth (98%): Clip_clip_1470__1_minClip_4_whd
   INFO: Optimizing for bandwidth (99%): Conv_nn_conv2d_1510__7_whd
   INFO: Optimizing for bandwidth (99%): Clip_clip_1520__1_minClip_4_whd
   INFO: Optimizing for bandwidth (99%): Clip_clip_1550__1_minClip__4_whd
   INFO: Neural Network Inputs:
   INFO:   Input #0: slimai_0_i0_whd, layout: WHD, channel order: RGB, dimensions: [224, 224, 3]
   INFO: Neural Network Outputs:
   INFO:   Output #0: nn_softmax_30_dwh, layout: DWH, dimensions: [1, 1, 1001]



Neural Network Inputs
---------------------

This line will print out the input infomation of compiled model. You need to pay more attention to the layout attribute, the layout in the compilation log is in a reversed sequence from the conventional arrangement format, as in the example showed above, the layout WHD corrsponds to conventional layout notation CHW.

Neural Network Outputs
----------------------

The same as input, here DWH means HWC in conventional way.


examples
========

Examples are released for telling how to use ``API`` to deploy compiled model to different target devices.

Get source code
-----------------

Get the examples codebase URL from `Semidrive Customer support <https://www.semidrive.com/>`_

compile APP
------------

Before compiling a test case project in the examples, you need to enter the root directory of examples and execute the following instructions to set the environment variables:

.. code-block:: bash

   $ source envsetup.sh


Then enter directory ``examples/apps``, run build_app.sh to compile app for different deploy platform, following is an example for aarch64-linux app compilation:

.. code-block:: bash

   $ ./build_app.sh -p aarch64-linux -d app_api/sdnn_api/


sdnn_test
=============

``sdnn_test`` tool functions:

#. SlimAI device probe and test;
#. Model profiling;
#. Model precision evaluation(Currently classfication only)


Get tool
--------

Get sdnn_test for different platform:

.. tabs::

   .. tab:: Linux-x86_64

      `sdnn_test_x86 <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/x86_64-linux_sdnn_test.tgz>`_

   .. tab:: Linux-aarch64

      `sdnn_test_linux <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/aarch64-linux_sdnn_test.tgz>`_

   .. tab:: Android-aarch64

      `sdnn_test_android <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/aarch64-android_sdnn_test.tgz>`_

   .. tab:: QNX-aarch64

      `sdnn_test_qnx <https://gitee.com/zgh551/sdnn_doc/releases/download/2.2.3/aarch64-qnx_sdnn_test.tgz>`_


Help info
----------

Run ``sdnn_test`` with option ``--help`` or ``-h``, help information will list:

.. code-block:: bash
   :linenos:

   sdnn_test version: 1.0.2
   Usage: sdnn_test [params] image deploy_json

      -a, --accuracy (value:false)
              Whether evaluate the accuracy of model.
      -d, --debug (value:false)
              Whether enable debug information.
      -h, --help (value:true)
              Print help message.
      -n (value:10)
              The count of loop inference.
      -p, --performance (value:false)
              Whether evaluate the performancb of model.

      image
              the path of test image.
      deploy_json
              The path of deploy json file.

detailed explanation for options:

.. table:: application params
   :name: sdnn_test_params

   +---------------+------+--------+----------+--------------------------+
   | params        | Abbr |default | Required | descriptions             |
   +===============+======+========+==========+==========================+
   | image         |      |        | true     | image or image dir path  |
   +---------------+------+--------+----------+--------------------------+
   | deploy_json   |      |        | true     | compile created json file|
   +---------------+------+--------+----------+--------------------------+
   | --help        | -h   | true   | false    | print help info          |
   +---------------+------+--------+----------+--------------------------+
   | --debug       | -d   | false  | false    | enable debug info output |
   +---------------+------+--------+----------+--------------------------+
   | --performance | -p   | false  | false    | enable perf info output  |
   +---------------+------+--------+----------+--------------------------+
   | --accuracy    | -a   | false  | false    | enable accuracy output   |
   +---------------+------+--------+----------+--------------------------+
   |               | -n   | 10     | false    | inference iteration num  |
   +---------------+------+--------+----------+--------------------------+

Device Status Test
--------------------

Run ``sdnn_test`` will print device status **LOG** :

.. code-block:: bash
   :linenos:

   |-----------------------|
   |    SlimAI SelfCheck   |
   |-----------------------|
   |      Item    | Status |
   |--------------|--------|
   |  xrp driver  |  Pass  |
   |  xrp node    |  Pass  |
   |  elf load    |  Pass  |
   |-----------------------|

#. **xrp driver** : check communication library driver status for SlimAI
#. **xrp node** : check status of communication node on host side
#. **elf load** : check load status of SlimAI device executive file


Debug info
------------

Run ``sdnn_test`` with option ``--debug`` or ``-d`` will enable debug information output as:

.. code-block:: bash
   :linenos:

   ===> [./mobilenet_v2.so]
   |-----------------------|
   |    Node    | Layout   |
   |------------|----------|
   |   input    |  input:[1, 3, 224, 224]
   |   output   |  0:[1, 1000]
   |-----------------------|

   ===> DataSet Method: [ImageNet]
   ===> Metric Method: [TopK]
   |-----------------------|
   |    Software Version   |
   |-----------------------|
   |    Params   | Version |
   |-------------|---------|
   |SDNN Test    | V1.0.2  |
   |SDNN Runtime | V2.2.1  |
   |-----------------------|

Debug information includes model path, dataset methed and metric methed.

Software Version
^^^^^^^^^^^^^^^^^

This Table includes version of ``sdnn_test`` and version of tvm runtime library. you can check whether the runtime version matches the build tool version.

Node
^^^^^

This table includes layout information for input and output.


Performance
------------

Run ``sdnn_test`` with option ``--performance`` or ``-p`` will enable performance output as:

.. code-block:: bash
   :linenos:

   |---------------------|
   |    Inference Time   |
   |---------------------|
   |  Params  | Time[ms] |
   |----------|----------|
   |   mean   |   8.421
   |   std    |   0.000
   |---------------------|

   |--------------------------|
   |   Inference Frame Rate   |
   |--------------------------|
   | Params | Frame Rate[fps] |
   |--------|-----------------|
   |  FPS   |     118.76
   |--------|-----------------|

- **mean** : average time over ``n`` times inferences;
- **std** : inference time standard variance  over ``n`` times inferences;
- **FPS** : inference throughput in frame per second


Precision evaluation
----------------------

Run ``sdnn_test`` with option ``--accuracy`` or ``-a`` will enable precision evlation, LOG would be printed as:

.. code-block:: bash
   :linenos:

   |------------------------------|
   |            Top5              |
   |           0.00 %
   |------------------------------|
   | Index | Score |     Label    |
   |-------|-------|--------------|
   |  282  | 9.989 | tiger cat
   |  287  | 9.161 | lynx, catamount
   |  285  | 9.068 | Egyptian cat
   |  278  | 9.019 | kit fox, Vulpes macrotis
   |  281  | 8.856 | tabby, tabby cat
   |------------------------------|

Currently only **TopK** is supported for classfication model. If you need to evaluate precision of other type model, you have to use **BinData** currently, which save model output as **bin** file, then write your precision evaluation code in python or any languege you prefer to finish the precision evaluation.


deploy.json format
-------------------

``sdnn_build`` will produce  ``model library(so)`` and ``deploy config file(.deploy.json)`` simutanously. You can use option ``--save`` to define output path. Json file looks as follow:

.. code-block:: json

   {
     "model": {
    "name": "mobilenet_v2",
    "accelerator": "cpu",
    "path": "./mobilenet_v2.so",
    "domain": "classfication",
    "inputs": [
      {
        "name": "input",
        "layout": "NCHW",
        "channel_order": "RGB",
        "mean": [
          0.485,
          0.456,
          0.406
        ],
        "std": [
          0.229,
          0.224,
          0.225
        ]
      }
    ]
     },
     "dataset": {
    "name": "ImageNet"
     },
     "metric": {
    "method": "TopK",
    "params": [
      5
    ],
    "annotation": "label.txt"
     }
   }

.. note::

   Verify that the automatically created parameters of the deploy.json are set **correctly** before you using it.


model section
^^^^^^^^^^^^^

name
""""

Model alias, it is automatically generated by compiler, you can modify it as your preference.

accelerator
"""""""""""

Inference execute device type, it is automatically generated by compiler and change with ``path`` value due to different accelerator compiling configuration. If you want to modify this parameter, you need to modify  ``path`` value together to ensure that the correct so file which matches the newly set accelerator type will be loaded.

path
""""

Model path, it is automatically generated by compiler  and change with ``accelerator`` value due to different accelerator compiling configuration. if the path of compiled model **so file** is not in the same directory where **deploy.json file** stays in, set this value as the relative path to the json file.

domain
""""""

Model domain, it is used to define default preprocess and postprocess when **dataset** and **metric** attribute values are not set.

inputs
""""""

Input nodes attribute list,  it specifies the parameters of each input node in an array manner, single or multiple inputs are formed as a list.

1. **name**

   Input node name, it is  automatically generated by compiler.

2. **layout**

   Input node layout, it is automatically generated by compiler referring to the compile configuration

3. **channel_order**

   Input node channel order, it is automatically generated by compiler referring to the compile configuration

4. **mean**

   Mean value of each channel of input node, it is automatically generated by compiler referring to the compile configuration

5. **std**

   Standard variance of each channel of input node, it is automatically generated by compiler referring to the compile configuration

.. note::

   **mean** and **std** will be skipped when ``slimai`` as accelerator, due to normalization process they defined has been integrated into model computations.

dataset section
^^^^^^^^^^^^^^^^

Dataset type used in model inference, it defines preprocess type.

name
""""

Training dataset type name. Currently only **ImageNet** dataset preprocess is supported.

metric section
^^^^^^^^^^^^^^^

Metric used in precision evaluation, Default value ``BinData``.

method
""""""

Currently **BinData** and **TopK**  are supported: TopK for classfication precision evaluation, BinData for others.

params
""""""

Parameters list used for metric.

annotation
""""""""""

Annotation file path.

sdnn_test usage
----------------

``sdnn_test`` can  be used to evaluate model performance.


Model test
^^^^^^^^^^^^

Test in x86
"""""""""""""

You can evalueate your model in docker immediately after the compiled model is generated by x86_64 format sdnn_test. Currently sdnn_test support cpu and slimai-simulator device on x86 computer, so you need to use option ``-emu`` to compile simulator model and a .sim.so model file will be generated to feed x86 version sdnn_test.

Test on chip
""""""""""""

Download appropriate version sdnn_test according to your board system, linux,Android or QNX. Copy model file(.so) and deploy config file(.deploy.json) into your board system, and make sure you have installed and setup environment for the runtime and OpenCV libraries, Then you can run sdnn_test on chip now.

Demo
^^^^

.. code-block:: bash

   ./sdnn_test cat.png mobilenet_v2.deploy.json -d -p