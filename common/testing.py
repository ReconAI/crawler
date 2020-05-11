import json

from rest_framework.test import APITestCase, APIClient


class CommonTestCaseMixin(object):
    user = None

    def content_to_dict(self, content):
        return json.loads(content)


class CommonTestCase(APITestCase, CommonTestCaseMixin):
    client_class = APIClient

    def is_equal_dict_structure(self, standart, candidate):

        if isinstance(candidate, dict) and isinstance(standart, dict):
            if set(standart.keys()) != set(candidate.keys()):
                raise Exception('Response structure is not correct.\nStandart keys = %s.\nCandidate keys = %s' % (
                    sorted(standart.keys()), sorted(candidate.keys())))
            for key, value in candidate.items():
                self.is_equal_dict_structure(standart[key], value)
        elif isinstance(candidate, list):
            for index, value in enumerate(candidate):
                try:
                    self.is_equal_dict_structure(standart[index], value)
                except IndexError:
                    pass

    def isDictsAlmostEquals(self, logic_result, test_result):
        """
        "test_result" should be equal or be part of "logic_result"
        """
        if not isinstance(logic_result, dict):
            raise Exception('logic_result is not a dict')

        if not isinstance(test_result, dict):
            raise Exception('Test result is not a dict')

        if set(test_result.keys()) - set(logic_result.keys()):  # works like: {1,2,3} - {1,2,3,4} == {}
            raise Exception(
                'Some keys in test_result were not found in logic_result. Logic_result keys = %s. test_result keys = %s' % (
                    logic_result.keys(), test_result.keys()))

        primitives = (str, int, float)

        def _isAlmostEquals(logic_result, test_result):
            if isinstance(test_result, dict):
                for key, value in test_result.items():
                    if isinstance(value, primitives):
                        if not logic_result[key] == test_result[key]:
                            raise Exception('logic_result["%s"] = %s, test_result["%s"] = %s' % (
                                key, logic_result[key], key, test_result[key]))
                    else:
                        _isAlmostEquals(logic_result[key], test_result[key])
            elif isinstance(test_result, list):
                for key, value in enumerate(test_result):
                    if isinstance(value, primitives):
                        if not logic_result[key] == test_result[key]:
                            raise Exception('logic_result["%s"]=%s, test_result["%s"]=%s' % (
                                key, logic_result[key], key, test_result[key]))
                    else:
                        _isAlmostEquals(logic_result[key], test_result[key])

        _isAlmostEquals(logic_result, test_result)
        return True
