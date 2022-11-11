.. sdnn documentation master file, created by
   sphinx-quickstart on Tue Aug 30 08:09:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SDNN User Guide
===============

SDNN is an end-to-end AI compiler framework based on the open source compiler framework TVM. SEMIDRIVE has adapted the TVM compiler framework. The main features are as follows:

- Base on TVM 0.8.0 Release
- Support OS: ``Android`` , ``Linux`` , ``QNX`` development and deployment
- Support for multiple backends: ``CPU`` , ``GPU`` , ``SlimAI``
- Support C++/PYTHON interface development and deployment
- Support heterogeneous and homogeneous multi-model deployment
- Support for multi-process and multi-threaded applications

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: SDNN Base
   :name: sdnn_base

   sdnn_base/license
   sdnn_base/docker
   sdnn_base/sdnn_build
   sdnn_base/deploy
   sdnn_base/inference

.. toctree::
   :maxdepth: 2
   :caption: appendix

   appendix/operator_support
