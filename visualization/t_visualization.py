import tensorflow as tf

to_save_values = True
to_restore_values = True

if __name__ == '__main__':

    #
    # #testing model load and save
    # a1 = tf.constant([1, 0, 1])
    # a2 = tf.constant([2, 0, 1])
    #
    # a3 = a2*a1
    #
    # v1 = tf.get_variable("v1", shape=[3], initializer=tf.zeros_initializer)
    # v2 = tf.get_variable("v2", shape=[5], initializer=tf.zeros_initializer)
    #


    # Create some variables.
    weights = tf.Variable(tf.random_normal([784, 200], stddev=0.35),
                          name="weights")
    biases = tf.Variable(tf.zeros([200]), name="biases")

    saver = tf.train.Saver()


    if to_save_values:
        #op1 = v1 + v2
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            print("v1 : %s" % weights.eval())
            # saver.save(sess, "tmp/model")

    if to_restore_values:
        with tf.Session() as sess:
            saver.restore(sess, "tmp/model")
            print('Model Restored')
            print("v1 : %s" % weights.eval())
            # print("v2 : %s" % v2.eval())








