class DataSet:
    def __init__(self, data_file, num_inputs, num_outputs):
        self.data_file = data_file
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

    def get_training_inputs(self):
        return self.read_data(self.data_file[:-4] + "_inputs.data")

    def get_training_outputs(self):
        return self.read_data(self.data_file[:-4] + "_outputs.data")

    def get_test_inputs(self):
        return self.read_data(self.data_file[:-4] + "_test_inputs.data")

    def get_test_outputs(self):
        return self.read_data(self.data_file[:-4] + "_test_outputs.data")

    def get_mini_batch(self, batch_size):
        # Implement your own mini-batch generation logic here
        pass

    def read_data(self, file_name):
        # Implement your own logic to read the data from file
        pass
