
import json
import sys
import unittest

# Enable imports without requiring users to set PYTHONPATH
sys.path.append('..')

from src import json_utils


class JsonUtilsTests(unittest.TestCase):

    def _compare_json(self, json_text, json_text_expected, transform=lambda x:x):

        json_obj1 = json.loads(json_text)
        json_obj_expected = json.loads(json_text_expected)

        # Use json.dumps to sort dictionary keys and format uniformly so we can compare more easily
        output = json.dumps(transform(json_obj1), sort_keys=True)
        expected = json.dumps(json_obj_expected)

        self.assertEqual(output, expected)


    def test_flattener(self):

        json_empty = '{}'
        flat_empty = '{}'

        json_small_flat = '{"a": 1}'
        flat_small_flat = '{"a": 1}'

        json_small = '{"a": {"b": 1.2 }}'
        flat_small = '{"a.b": 1.2 }'

        json_medium = '{"a": 1,"b": true,"c": {"d": 3,"e": "test"}}'
        flat_medium = '{"a": 1,"b": true,"c.d": 3,"c.e": "test"}'

        json_deep = '{"a": {"b": {"c": null}}}'
        flat_deep = '{"a.b.c": null}'

        json_list = '{"a": [1, 2, 3]}'

        transform = json_utils.flatten

        self._compare_json(json_empty, flat_empty, transform)
        self._compare_json(json_small_flat, flat_small_flat, transform)
        self._compare_json(json_small, flat_small, transform)
        self._compare_json(json_medium, flat_medium, transform)
        self._compare_json(json_deep, flat_deep, transform)

        # Check throw exception for unsupported types
        with self.assertRaises(Exception):
            json_list_obj = json.loads(json_list)
            json_utils.flatten(json_list_obj)


if __name__ == '__main__':
    unittest.main()
