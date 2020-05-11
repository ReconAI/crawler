class ChoiceEnum(object):

    @classmethod
    def for_choice(cls):
        choices = []
        for k in dir(cls):
            if k.isupper():
                v = getattr(cls, k)
                choices.append((v, k))
        return choices

    @classmethod
    def for_choice_only_allowed(cls, allowed_list=None):
        if allowed_list is None:
            allowed_list = []
        choices = []
        for k in dir(cls):
            v = getattr(cls, k)
            if v in allowed_list:
                choices.append((v, k))
        return choices

    @classmethod
    def values(cls):
        return [v for k, v in cls.__dict__.items() if k.isupper()]

    @classmethod
    def get_name(cls, value):
        for k, v in cls.__dict__.items():
            if v == value and k.isupper():
                return k
        raise ValueError('%s is not defined' % value)
