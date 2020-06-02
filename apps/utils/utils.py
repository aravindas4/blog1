import uuid


def get_uuid():
    return str(uuid.uuid4()).upper()[:8]


def reverse_of_simple_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}


def get_choice_name_value_dictionary(choices):
    return {item.name: item.value for item in choices}
