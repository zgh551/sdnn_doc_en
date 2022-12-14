================
Operator support
================

The list of ONNX operators supported by XNNC is as follows:


+------------------------+---------------------+--------------+
| Operator               | Inputs              | Outputs      |
+========================+=====================+==============+
| Abs                    | float               |              |
+------------------------+---------------------+--------------+
| Add                    | int32, int64, float |              |
+------------------------+---------------------+--------------+
| ArgMax                 | float               | int32, int64 |
+------------------------+---------------------+--------------+
| AveragePool            | float               |              |
+------------------------+---------------------+--------------+
| Batch Normalize        | float               |              |
+------------------------+---------------------+--------------+
| Instance               | float               |              |
+------------------------+---------------------+--------------+
| Normalization          |                     |              |
+------------------------+---------------------+--------------+
| Ceil                   | float               |              |
+------------------------+---------------------+--------------+
| Clip                   | float               |              |
+------------------------+---------------------+--------------+
| Concat                 | float               |              |
+------------------------+---------------------+--------------+
| Constant               |                     |              |
+------------------------+---------------------+--------------+
| ConstantOfShape        | int32, int64, float |              |
+------------------------+---------------------+--------------+
| Conv                   | float               |              |
+------------------------+---------------------+--------------+
| Cast                   |                     |              |
+------------------------+---------------------+--------------+
| ConvTranspose          | float               |              |
+------------------------+---------------------+--------------+
| Cos                    | float               |              |
+------------------------+---------------------+--------------+
| Clip (V10, V11)        | float               |              |
+------------------------+---------------------+--------------+
| DepthToSpace (V10,V11) |                     |              |
+------------------------+---------------------+--------------+
| Div                    | float               |              |
+------------------------+---------------------+--------------+
| Dropout                |                     |              |
+------------------------+---------------------+--------------+
| Elu                    | float               |              |
+------------------------+---------------------+--------------+
| Exp                    | float               |              |
+------------------------+---------------------+--------------+
| Expand                 |                     |              |
+------------------------+---------------------+--------------+
| Flatten                |                     |              |
+------------------------+---------------------+--------------+
| Floor                  | float               |              |
+------------------------+---------------------+--------------+
| Gather                 | int32, int64, float |              |
+------------------------+---------------------+--------------+
| Gemm                   | float               |              |
+------------------------+---------------------+--------------+
| GlobalAveragePool      | float               |              |
+------------------------+---------------------+--------------+
| Greater                | float               |              |
+------------------------+---------------------+--------------+
| GRU                    | float               | Float        |
+------------------------+---------------------+--------------+
| Identity               |                     |              |
+------------------------+---------------------+--------------+
| LRN                    | float               |              |
+------------------------+---------------------+--------------+
| LeakyRelu              | slope: [0, 1]       |              |
+------------------------+---------------------+--------------+
| Less                   | int32, ibool        |              |
+------------------------+---------------------+--------------+
| Log                    | float               |              |
+------------------------+---------------------+--------------+
| LSTM                   | float               | float        |
+------------------------+---------------------+--------------+
| MatMul                 | float               |              |
+------------------------+---------------------+--------------+
| Max                    | float               |              |
+------------------------+---------------------+--------------+
| MaxPool                | float               |              |
+------------------------+---------------------+--------------+
| Min                    | float               |              |
+------------------------+---------------------+--------------+
| Mul                    | int32, int64, float |              |
+------------------------+---------------------+--------------+
| Neg                    | float               |              |
+------------------------+---------------------+--------------+
| NonZero                |                     |              |
+------------------------+---------------------+--------------+
| PRelu                  | float               |              |
+------------------------+---------------------+--------------+
| Pad                    |                     |              |
+------------------------+---------------------+--------------+
| Pow                    | float               |              |
+------------------------+---------------------+--------------+
| Reciprocal             | float               |              |
+------------------------+---------------------+--------------+
| ReduceMean             | float               |              |
+------------------------+---------------------+--------------+
| ReduceSum              | float               |              |
+------------------------+---------------------+--------------+
| ReduceSum Square       | float               |              |
+------------------------+---------------------+--------------+
| ReduceMin              | float               |              |
+------------------------+---------------------+--------------+
| ReduceMax              | float               |              |
+------------------------+---------------------+--------------+
| Relu                   | float               |              |
+------------------------+---------------------+--------------+
| Reshape                |                     |              |
+------------------------+---------------------+--------------+
| Resize                 | float               |              |
+------------------------+---------------------+--------------+
| Resize V11             | float               |              |
+------------------------+---------------------+--------------+
| Round                  | float               |              |
+------------------------+---------------------+--------------+
| ScatterND (V11)        | float               |              |
+------------------------+---------------------+--------------+
| Shape                  |                     |              |
+------------------------+---------------------+--------------+
| Sin                    | float               |              |
+------------------------+---------------------+--------------+
| Slice                  |                     |              |
+------------------------+---------------------+--------------+
| Sigmoid                | float               |              |
+------------------------+---------------------+--------------+
| Softmax                | float               |              |
+------------------------+---------------------+--------------+
| Softplus               | float               |              |
+------------------------+---------------------+--------------+
| SpaceToDepth           | float               |              |
+------------------------+---------------------+--------------+
| Split                  | float, int32, int64 |              |
+------------------------+---------------------+--------------+
| Squeeze                |                     |              |
+------------------------+---------------------+--------------+
| Sqrt                   | float               |              |
+------------------------+---------------------+--------------+
| Sub                    | float               |              |
+------------------------+---------------------+--------------+
| Sum                    | float               |              |
+------------------------+---------------------+--------------+
| Tanh                   | float               |              |
+------------------------+---------------------+--------------+
| Tile                   | float               |              |
+------------------------+---------------------+--------------+
| TopK                   | float               |              |
+------------------------+---------------------+--------------+
| Transpose              |                     |              |
+------------------------+---------------------+--------------+
| Upsample               | float               |              |
+------------------------+---------------------+--------------+
| Unsqueeze              |                     |              |
+------------------------+---------------------+--------------+
| Where                  |                     |              |
+------------------------+---------------------+--------------+




List of tflite operators supported by SlimAI



+-----------------------+------------------+
| Tflite operator       | slimAi supported |
+=======================+==================+
| Add                   | Yes              |
+-----------------------+------------------+
| Mul                   | Yes              |
+-----------------------+------------------+
| SpaceToBatchNd        | Yes              |
+-----------------------+------------------+
| BatchToSpaceNd        | Yes              |
+-----------------------+------------------+
| HardSwish             | Yes              |
+-----------------------+------------------+
| Pad                   | Yes              |
+-----------------------+------------------+
| Conv2D                | Yes              |
+-----------------------+------------------+
| Relu                  | Yes              |
+-----------------------+------------------+
| DepthwiseConv2D       | Yes              |
+-----------------------+------------------+
| Concatenation         | Yes              |
+-----------------------+------------------+
| ResizeBilinear        | Yes              |
+-----------------------+------------------+
| ResizeNearestNeighbor | Yes              |
+-----------------------+------------------+
| AveragePool2D         | Yes              |
+-----------------------+------------------+
| Reshape               | Yes              |
+-----------------------+------------------+
| MaxPool2D             | Yes              |
+-----------------------+------------------+
| FullyConnected        | Yes              |
+-----------------------+------------------+
| Softmax               | Yes              |
+-----------------------+------------------+
| Quantize              | Yes              |
+-----------------------+------------------+
| Logistic              | Yes              |
+-----------------------+------------------+
| Mean                  | Yes              |
+-----------------------+------------------+
| ReduceMax             | Yes              |
+-----------------------+------------------+
