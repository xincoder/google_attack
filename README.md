## Hongyang & Xin

### This repository is used to record the best defense result of our team, trained by TRADESv2 on ResNet-50.
(TRADESv1 [[paper]](https://arxiv.org/pdf/1901.08573.pdf) [[code]](https://github.com/yaodongyu/TRADES))

#### Bird or Bicycle dataset
All percentages above correspond to the model's accuracy at 80% coverage.

| Defense               | Submitted by  | Clean data | Common corruptions | Spatial grid attack | SPSA attack | Boundary attack |  Submission Date |
| --------------------- | ------------- | ------------| ------------ |--------------- |-------- | ------- | --------------- |
| [Pytorch ResNet50 <br>(trained on bird-or-bicycle extras)](https://github.com/xincoder/google_attack) |Hongyang Zhang (CMU) & Xin Li (Lehigh Univ.)|100.0%|100.0%|99.5%|100.0%|95.0%|Jan 17th, 2019 (EST)|
| [Keras ResNet <br>(trained on ImageNet)](https://github.com/google/unrestricted-adversarial-examples/tree/master/examples/undefended_keras_resnet)   |  Google Brain   |    100.0%    |    99.2%    |  92.2%    |     1.6%    |     4.0%     |  Sept 29th, 2018 |
| [Pytorch ResNet <br>(trained on bird-or-bicycle extras)](https://github.com/google/unrestricted-adversarial-examples/tree/master/examples/undefended_pytorch_resnet)  |  Google Brain | 98.8% | 74.6% | 49.5% | 2.5% | 8.0% | Oct 1st, 2018 |


___

### To test the performance of our model:
- Step 1: Download our evaluation code:
  ``` bash
  git clone https://github.com/xincoder/google_attack.git
  ```

- Step 2: Download our pre-trained weight:
  https://drive.google.com/file/d/1l7uZW73gMzwvBDR5WWOXVPY1vWX3WEk4/view?usp=sharing and put it into the folder "google_attack"
  
- Step 3: Run the code:
  ``` bash
  python eval_hongyangxin.py
  ```
