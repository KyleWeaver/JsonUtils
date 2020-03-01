

_json_primitives = {str, int, float, bool, type(None), type(u'')}


def is_json_primitve(obj):
    """Returns True iff obj is a json primitive: string, int, float, boolean, null, or
    unicode string."""

    try:
        if type(obj) in _json_primitives:
            return True

    # Unhashable types will throw exception, but are not primitives
    except TypeError:
        return False

    return False


def flatten(json_object):
    """Given a python type corresponding to a json object, return json_object with flattened keys
     as a dictionary. Supports JSON containing only dictionaries or primitives. Does not guarantee
     order is preserved (unless using python version >= 3.7)"""

    def dfs(obj, parent_keys):
        """Return list of tuples representing the mapping of flattened keys to values."""

        if is_json_primitve(obj):
            entry = ('.'.join(parent_keys), obj)
            return [entry]

        if type(obj) is dict:
            entries = []

            for (key, obj_val) in obj.items():
                new_parent_keys = parent_keys + [key]
                entries.extend(dfs(obj_val, new_parent_keys))

            return entries

        raise Exception('Unsupported type: ' + str(type(obj)))

    return dict(dfs(json_object, []))
