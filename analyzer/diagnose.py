from analyzer.globals import TIME_RECORDER


def explain_performance_by_name():
    print(f"Total Time: {sum(TIME_RECORDER.values())}")
    for t, n in sorted([(t, n) for n, t in TIME_RECORDER.items()], reverse=True):
        print(f"{t:10.2f}ms    {n}")


def explain_performance_by_class():
    print("Divided by Class: ")
    classes = {}
    for n, t in TIME_RECORDER.items():
        if '.' in n:
            class_name, method_name = n.split('.')
            if class_name in classes:
                classes[class_name][method_name] = t
            else:
                classes[class_name] = {method_name: t}
        # todo: normal functions
    for cls_method_dict in classes.values():
        cls_method_dict['total'] = sum(cls_method_dict.values())
    for cls in sorted(classes.keys(), key=lambda i: classes[i]['total'], reverse=True):
        print(f"{cls}    {classes[cls].pop('total')}ms")
        for t, n in sorted([(t, n) for n, t in classes[cls].items()], reverse=True):
            print(f"    {t:10.2f}ms    {n}")
