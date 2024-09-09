DeepEye - APIs
===========================
**This project aims to recommend good visualizations from a relational dataset.**
This repository shares the APIs of DeepEye's visualization recommendation module. A live demo of DeepEye: http://deepeye.tech

Description
===========================
### Visualization Ranking: 
the task is, given two visualization nodes, to decide which one is better. Hence we need to rank multiple visualization nodes. We support three ranking approaches:
1. **Learning-to-rank**: We use a learning-to-rank model. Roughly speaking, it is a supervised learning task that takes the input space X as lists of feature vectors, and Y as the output space consisting of grades (or ranks). The goal is to learn a function F (·) from the training examples, such that given two input vectors x1 and x2, it can determine which one is better, F (x1 ) or F (x2 ). We used the LambdaMART algorithm. [More Details](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf)
2. **Partial Order-based approach**: the basic idea is that we define some partial orders which are used to decide which visualization node is better. Then we build a graph based on the partial orders, where each vertex is a visualization node and the directed edge between two nodes is decided by the partial order. At last, we can use the graph to compute a score for each visualization node based on topology sorting, i.e., the smaller the topology order is, the larger the score is. [More Details](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf)
3. **Diversified Ranking**: We aim to select diversified top-k visualization nodes since there may be many similar visualizations showing redundant information. For example, v1 > v2 and v2 > v3 do not necessarily mean that v1 + v2 > v1 + v3, since v1 and v2 might be very “similar". Our basic idea is to construct a graph in which nodes are visualizations, and the weight of the edge between two nodes denotes the distance between them. Then we use the graph, our defined relevance, and diversity measurement to calculate diversified top-k visualizations.

Platforms
===========================
DeepEye - APIs has been tested on **OS X**, **CentOS**, **Linux**, and **Windows 10**.



Usage
===========================
### Dependencies 
- [x] Python 3.6+
- [x] [pyecharts v1.3.1](https://github.com/pyecharts/pyecharts)
- [x] [numpy](https://github.com/numpy/numpy)
- [x] pandas

### How to use

If you want to get the latest source code, please clone it from the Github repo using the following command.

```
https://github.com/Thanksyy/DeepEye-APIs.git
cd DeepEye-APIs
python3 test.py
```


Publications
===========================
- Yuyu Luo, Xueqi Qin, Nan Tang, Guoliang Li. [DeepEye: Towards Automatic Data Visualization](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf). **ICDE 2018**
- Yuyu Luo, Xuedi Qin, Nan Tang Guoliang Li, Xinran Wang. [DeepEye: Creating Good Data Visualizations by Keyword Search](http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/sigmod18-deepeye.pdf). **SIGMOD 2018 Demo**

# Contact
If you have any questions, feel free to contact Yuyu Luo (yuyuluo [AT] hkust-gz.edu.cn).
