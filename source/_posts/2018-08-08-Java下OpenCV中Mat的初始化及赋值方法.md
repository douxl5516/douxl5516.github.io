---
title: Java下OpenCV中Mat的初始化及赋值方法
date: 2018-08-08 22:54:20
description: Java中Mat如何初始化和赋值
tags: [OpenCV]
category: OpenCV
mathjax: true
---
利用函数构造特殊Mat

```Java
    A = Mat.eye(3,3, CvType.CV_64FC1);
    A = Mat.zero(3,3,CvType.CV_64FC1);
```

诸如MatOfDouble之类的矩阵，还支持将矩阵转换为List或者从List（array）转换成矩阵。所以可以直接这样创建矩阵：

```Java
    MatOfDouble A = new MatOfDouble(1,2,3,4,5,6,7,8,9);
```

或者

```Java
    MatOfDouble A = new MatOfDouble();
    A.fromArray(1,2,3,4,5,6,7,8,9);
```

这样得到的矩阵实际上是一个列向量，也就是$9*1$的矩阵。如果想得到一个$3*3$的矩阵，可以使用reshape。

```Java
    A.reshape(1,3);
```
注意这里第一个参数为通道数，第二个参数为行数


