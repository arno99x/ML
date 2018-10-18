import numpy as np

def train_test_split(X,y,test_ratio=0.2,seed=None):
    """将数据X和y按照test_ratio分割成X_train y_train 与 X_test y_test"""
    ## step1 : 取0-len(X)范围的随机数
    shuffle_index = np.random.permutation(len(X))
    ## step2 : 设置测试数据集为20%
    test_ratio = 0.2
    test_size = int(len(X) * test_ratio)
    ## step3 : 取后20%个元素做为测试数据集的index ; 前80%个元素做为训练数据集
    test_index = shuffle_index[:test_size]
    train_index = shuffle_index[test_size:]
    ## step4 : 获取训练数据集
    X_train = X[train_index]
    y_train = y[train_index]
    ## step5 : 获取测试数据集
    X_test = X[test_index]
    y_test = y[test_index]

    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)

    return X_train,y_train,X_test,y_test