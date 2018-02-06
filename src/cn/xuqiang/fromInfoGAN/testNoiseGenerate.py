import numpy as np
from pprint import pprint

def make_one_hot(indices, size):
    as_one_hot = np.zeros((indices.shape[0], size))
    as_one_hot[np.arange(0, indices.shape[0]), indices] = 1.0
    return as_one_hot





# 返回一个size=64行style_size=62+num_continuous=2 = 64列的二维数组
def create_continuous_noise(num_continuous, style_size, size):
    continuous = np.random.uniform(-1.0, 1.0, size=(size, num_continuous))
    style = np.random.standard_normal(size=(size, style_size))
    return np.hstack([continuous, style])

#返回的noise为categorical_cardinality行，size=64列的二维数组
def create_categorical_noise(categorical_cardinality, size):
    noise = []
    for cardinality in categorical_cardinality:
        noise.append(
            np.random.randint(0, cardinality, size=size)
        )
    return noise


def encode_infogan_noise(categorical_cardinality, categorical_samples, continuous_samples):
    noise = []
    for cardinality, sample in zip(categorical_cardinality, categorical_samples):
        noise.append(make_one_hot(sample, size=cardinality))
    noise.append(continuous_samples)
    return np.hstack(noise)

# 其中style_size为62，categorical_cardinality为[10]，num_continuous为2
def create_infogan_noise_sample(categorical_cardinality, num_continuous, style_size):
    batch_size=64
    def sample(batch_size):
        return encode_infogan_noise(
            categorical_cardinality,
            create_categorical_noise(categorical_cardinality, size=batch_size),
            create_continuous_noise(num_continuous, style_size, size=batch_size)
        )
    return sample(64)


def create_gan_noise_sample(style_size):
    def sample(batch_size):
        return np.random.standard_normal(size=(batch_size, style_size))
    return sample

import tensorflow as tf
if __name__ == "__main__":
    # z_size=74
    # 其中style_size为62，categorical_cardinality为[10]，num_continuous为2
    # z_size = style_size + sum(categorical_cardinality) + num_continuous
    sample_noise = create_infogan_noise_sample(
        [10],
        2,
        62
    )

    zc_vectors = tf.placeholder(
        tf.float32,
        [None, 74],
        name="zc_vectors"
    )
    categorical_c_vectors = []
    categorical_cardinality = 10
    categorical_cardinality = tf.convert_to_tensor(categorical_cardinality)
    num_continuous = 2
    offset = 0
    # for cardinality in categorical_cardinality:
    #     # 实质就是如果是使用InfoGAN则将前10列取出，行保留所有==这个就是类别latend code
    #     categorical_c_vectors.append(
    #         zc_vectors[:, offset:offset + cardinality]
    #     )
    categorical_c_vectors.append(
                zc_vectors[:, offset:offset + 10]
            )
        # categorical_c_vectors = tf.convert_to_tensor(categorical_c_vectors)
    offset += 10
    # 将随机噪声中的11-12列取出，行保留所有===这个就是符合均匀分布[-1,1]的连续的latend code
    continuous_c_vector = zc_vectors[:, offset:offset + num_continuous]

    # num_categorical = sum([true_categorical.get_shape()[1].value for true_categorical in categorical_c_vectors])
    num_continuous = continuous_c_vector.get_shape()[1].value

    # continuous_c_vector = tf.convert_to_tensor(continuous_c_vector)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # yy = sess.run(num_categorical, feed_dict={zc_vectors: sample_noise})
        kk = sess.run(num_continuous,feed_dict={zc_vectors:sample_noise})


        # print(yy)
        print("===================")
        print(kk)




    # print(categorical_c_vectors)
    # for i in categorical_c_vectors:
    #     print("==========")
    #     print(i.get_shape())
    #     print("==========")


    #
    # # num_categorical = sum([true_categorical.get_shape()[1].value for true_categorical in categorical_c_vectors])
    #
    # num_continuous = continuous_c_vector.get_shape()[1].value
    #
    # # print(num_categorical)
    # print(num_continuous)
