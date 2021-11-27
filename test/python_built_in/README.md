LIMIT = 1000000

When start calculation, all other apps are quited except pycharm. 

- Best performance on MacBook Air (Monterey 12.0.1):
```commandline
Limit = 1000000
Total Time: 668.8199043273926
    153.83ms    Filter.method_2
    153.35ms    Filter.method_3
    110.48ms    Sum.method_0
     84.23ms    Filter.method_0
     60.53ms    Filter.method_1
     55.45ms    Sum.method_1
     50.95ms    Sum.method_2
Divided by Class: 
Filter    451.9388675689697ms
        153.83ms    method_2
        153.35ms    method_3
         84.23ms    method_0
         60.53ms    method_1
Sum    216.88103675842285ms
        110.48ms    method_0
         55.45ms    method_1
         50.95ms    method_2
```