from numpy import convolve

kaiser_filter = [-0.01452123, -0.0155227 ,  0.01667252,  0.01800633, -0.01957209, -0.0214361 ,  0.02369253,  0.02647989, -0.03001054, -0.03462755, 0.04092347,  0.05001757, -0.06430831, -0.09003163,  0.15005272, 0.45015816,  0.45015816,  0.15005272, -0.09003163, -0.06430831, 0.05001757,  0.04092347, -0.03462755, -0.03001054,  0.02647989, 0.02369253, -0.0214361 , -0.01957209,  0.01800633,  0.01667252, -0.0155227 , -0.01452123]

def decimate_by_2(arr):
  return arr[::2]

def downsample_by_2(arr):
  conv = convolve(arr, kaiser_filter, mode = 'same')
  # sourse: https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
  conv = conv * 2
  return decimate_by_2(conv)

# I also wrote an OOP-based version below:
# class DownSampling():
#   def __init__(self):
#     self.filter = [-0.01452123, -0.0155227 ,  0.01667252,  0.01800633, -0.01957209, -0.0214361 ,  0.02369253,  0.02647989, -0.03001054, -0.03462755, 0.04092347,  0.05001757, -0.06430831, -0.09003163,  0.15005272, 0.45015816,  0.45015816,  0.15005272, -0.09003163, -0.06430831, 0.05001757,  0.04092347, -0.03462755, -0.03001054,  0.02647989, 0.02369253, -0.0214361 , -0.01957209,  0.01800633,  0.01667252, -0.0155227 , -0.01452123]

#   def decimate_by_2(self, arr):
#     return arr[::2]

#   def downsample_by_2(self, arr):
#     conv = convolve(arr, self.filter, mode = 'same')
#     conv = conv * 2
#     return self.decimate_by_2(conv)

# sampling = DownSampling()
# input1 = [1]*(len(sampling.filter))
# print(sampling.downsample_by_2(input1))


