# coding=utf-8
import os,sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

data_path = os.path.join('Data','horse-colic.data')
type = ["surgery","Age","Hospital Number","rectal temperature","pulse",
        "respiratory rate","temperature of extremities","peripheral pulse",
        "mucous membranes","capillary refill time","pain","peristalsis",
        "abdominal distension","nasogastric tube","nasogastric reflux",
        "nasogastric reflux PH","rectal examination","abdomen","packed cell volume",
        "total protein","abdominocentesis appearance","abdomcentesis total protein",
        "outcome","surgical lesion","type of lesion 1","type of lesion 2",
        "type of lesion 3","cp_data"]
feature_num = 27
#载入文件
def load_data(feature_number = 1):
    file = open(data_path)
    stringArr = file.readlines()
    data = []
    for line in stringArr:
        line = line.strip('\n')
        line = line.strip(' ')
        item = line.split(' ')
        value = []
        for str in item:
            if str == '?':
                value.append(-1)
            else:
                value.append(float(str))
        data.append(value)
    data = np.array(data)
    return data

# 数据摘要
def data_abstract(data):
    numeric_attribute = [3,4,5,15,18,19,21]
    total = [i for i in range(0,feature_num)]
    nominal_properties = list(set(total).difference(set(numeric_attribute)))

    #标称属性,给出每个可能取值的频数
    nominal_res = []
    for i in nominal_properties:
        clean_data = data[np.where(data[:,i] != -1),i]
        nominal_res.append(dict(zip(*np.unique(clean_data, return_counts=True))))

    #数值属性, 最大、最小、均值、中位数、四分位数及缺失值的个数
    numeric_res = []
    index = 0

    fig = plt.figure(1)
    plt.title('Histogram')
    plt.subplots_adjust(hspace=0.5)

    plt.figure(2)
    plt.title('QQ-Plot')
    plt.subplots_adjust(hspace=0.5)

    plt.figure(3)
    plt.title('Box-Plot')
    plt.subplots_adjust(hspace=1,wspace=1)

    for i in numeric_attribute:
        index += 1
        result = []
        clean_data = data[np.where(data[:,i] != -1),i]
        result.append(np.max(clean_data))
        result.append(np.min(clean_data))
        result.append(np.mean(clean_data))
        result.append(np.median(clean_data))
        s = pd.Series(clean_data.flatten())
        result.append(s.quantile(0.25))
        numeric_res.append(result)

        plt.figure(1)
        plt.subplot(3,3,index)
        plt.hist(clean_data.flatten(),bins=20)
        plt.title(type[i])

        plt.figure(2)
        plt.subplot(3,3,index)
        plt.boxplot(clean_data.flatten())
        plt.title(type[i])

        plt.figure(3)
        plt.subplot(3,3,index)
        stats.probplot(clean_data.flatten(), dist="norm", plot=plt)
        plt.title(type[i])

    plt.show()
    return nominal_res,numeric_res

def fill_missing_data(data, numeric_attribute=[], mode=0):
    if mode == 0:#最大频数
        for attr in numeric_attribute:
            clean_data = data[np.where(data[:,attr] != -1),attr]
            freq = np.unique(clean_data, return_counts=True)
            max_freq = freq[0][np.where(freq[1] == np.max(freq[1]))]
            data[np.where(data[:,attr]==-1)]=max_freq

    elif mode == 1:#相关性
        n_attributes = data.shape[1]
        correlation = np.zeros((n_attributes,n_attributes))
        for i in range(0,n_attributes):
            correlation[i,i] = float("-inf")
            for j in range(i+1,n_attributes):
                #剔除两列属性中缺失的部分
                index_i = np.where(data[:,i]!=-1)
                index_j = np.where(data[:,j]!=-1)
                index_intersect = np.intersect1d(index_i,index_j)
                #计算相关性
                if index_intersect.size == 0:
                    correlation[i,j] = float("inf")
                else:
                    attr_i = data[index_intersect,i]
                    attr_j = data[index_intersect,j]
                    correlation[i,j]= np.corrcoef(attr_i.transpose(),attr_j.transpose())[0,1] # Euclidean
                correlation[j,i] = correlation[i,j]

        missing_index = np.array(np.where(data==-1)).reshape(2,-1).transpose()
        for idx in missing_index:
            # 降序排列
            corr = np.argsort(-correlation[idx[1]])
            max_corr = 0
            while(data[idx[0],corr[max_corr]] == -1):
                max_corr += 1
            data[idx[0],idx[1]] = data[idx[0],corr[max_corr]]

    elif mode == 2:#相似性
        n_samples = data.shape[0]
        distance = np.zeros((n_samples,n_samples))
        for i in range(0,n_samples):
            distance[i,i] = float("inf")
            for j in range(i+1,n_samples):
                #剔除两组数据中缺失的部分
                index_i = np.where(data[i,:]!=-1)
                index_j = np.where(data[j,:]!=-1)
                index_intersect = np.intersect1d(index_i,index_j)
                #计算欧氏距离
                if index_intersect.size == 0:
                    distance[i,j] = float("inf")
                else:
                    data_i = data[i,index_intersect]
                    data_j = data[j,index_intersect]
                    distance[i,j]= np.sqrt(np.sum(np.square(data_i - data_j)))  # Euclidean
                distance[j,i] = distance[i,j]

        missing_index = np.array(np.where(data==-1)).reshape(2,-1).transpose()
        for idx in missing_index:
            similarity = np.argsort(distance[idx[0]])
            min_sim = 0
            while(data[similarity[min_sim],idx[1]] == -1):
                min_sim += 1
            data[idx[0],idx[1]] = data[similarity[min_sim],idx[1]]

def data_visualization(data, attr):
    plt.figure(1)
    plt.title('Histogram')
    plt.subplots_adjust(hspace=0.5)

    plt.figure(2)
    plt.title('QQ-Plot')
    plt.subplots_adjust(hspace=0.5)

    plt.figure(3)
    plt.title('Box-Plot')
    plt.subplots_adjust(hspace=1,wspace=1)

    index = 0
    for attr in numeric_attribute:
        index += 1
        plt.figure(1)
        plt.subplot(3,3,index)
        plt.hist(data[:,attr].flatten(),bins=20)
        plt.title(type[attr])

        plt.figure(2)
        plt.subplot(3,3,index)
        plt.boxplot(data[:,attr].flatten())
        plt.title(type[attr])

        plt.figure(3)
        plt.subplot(3,3,index)
        stats.probplot(data[:,attr].flatten(), dist="norm", plot=plt)
        plt.title(type[attr])

    plt.show()

if __name__=='__main__':
    print 'loading data...'
    data = load_data(feature_num)
    numeric_attribute = [3,4,5,15,18,19,21]
    # print 'calculate data abstract'
    # data_abstract(data)
    # print 'visualization of clean data'

    print 'Fill missing data by maximum'
    fill_missing_data(data,numeric_attribute,mode=1)
    data_visualization(data,numeric_attribute)


