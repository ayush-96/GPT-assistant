import random


contexts = ["Respond to the following but as follow up question"]


def get_context():
    return contexts[random.randrange(0, len(contexts))]


def get_context_index(str):
    return contexts.index(str)
