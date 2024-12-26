def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    info['attributes'] = dir(obj)

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    info['module'] = obj.__class__.__module__

    info['doc'] = obj.__doc__

    return info


number_info = introspection_info(42)
print(number_info)
