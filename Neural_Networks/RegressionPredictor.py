from BasePredictor import BasePredictor
import numpy as np
import tensorflow as tf

def RegressionPredictor(self, BasePredictor):
    def __init__(internal_state_size, company , verbose, update_rate):
        self.state_size=internal_state_size
        self.company=company
        feature_columns = [tf.feature_column.numeric_column(key="x")]
        self.regressor=tf.estimators.LinearRegressor(feature_columns=feature_columns)
        self.count=0
    def input_fn(self, x, y):
        return tf.estimator.inputs.numpy_input_fn( x={"x": np.array(x)}, y=np.array(y),num_epochs=None,shuffle=True)
    def update(self,state):
        super.update(state)

        if self.count()%update_rate==0:
            self.regressor.train(input_fn=self.input_fn, steps=STEPS)
        self.count+=1
