from decorator import cumulate_time


class TimeAnalyzer(type):
    def __new__(mcs, cls, bases, class_dict):
        for k, v in class_dict.items():
            if str(type(v)) == "<class 'function'>":
                class_dict[k] = cumulate_time(v)
        return type(cls, bases, class_dict)
