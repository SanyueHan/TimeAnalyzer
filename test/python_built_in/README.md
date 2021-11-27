LIMIT = 1000000

When start calculation, all other apps are quited except pycharm. 

- Best performance on MacBook Air (Monterey 12.0.1):
```commandline
Limit = 1000000
Total Time: 675.2510070800781
    155.06ms    Filter.method_2
    154.44ms    Filter.method_3
    110.53ms    Sum.method_0
     92.96ms    Filter.method_0
     60.23ms    Filter.method_1
     54.15ms    Sum.method_1
     47.88ms    Sum.method_2
Divided by Class: 
Filter    462.6889228820801ms
        155.06ms    method_2
        154.44ms    method_3
         92.96ms    method_0
         60.23ms    method_1
Sum    212.56208419799805ms
        110.53ms    method_0
         54.15ms    method_1
         47.88ms    method_2
```