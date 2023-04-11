def concatenate(*args, **kwargs):
    message = ''.join(args)

    for old_str, new_str in kwargs.items():
        message = message.replace(old_str, new_str)

    return message