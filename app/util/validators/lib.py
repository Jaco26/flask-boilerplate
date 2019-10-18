import uuid
from voluptuous import *

def json_from(source, template_dict):
  accum = {}
  for key in template_dict:
    predicate = template_dict[key]
    if type(key) is tuple:
      if len(key) == 2:
        field_name = key[0]
        default_value = key[1]
        accum.update({ Required(field_name, default=default_value): predicate })
      else:
        raise 'Tuple keys must contain two elements'
    elif type(key) is str:
      accum.update({ Required(key, default=None): predicate })

  schema_func = Schema(accum, extra=REMOVE_EXTRA)
  return schema_func(dict(source))


class Custom:
  UUID = lambda val: val and str(uuid.UUID(val))