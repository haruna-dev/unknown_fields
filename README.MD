# unknown_fields
## Wrapper for dataclasses.dataclass init method to handle unknown arguments

### Usage:
```
from dataclasses import dataclass
from unknown_fields import unknown_fields, Action


@unknown_fields(action=Action.Ignore)
@dataclass
class MyWrappedDataclass:
    a: int
    b: str
    c: float = 0.

if __name__ == "__main__":
    import sys
    this_wont_raise_an_error = MyWrappedDataclass(1, "2", 3., CustomClassOrWhatever(), 123, None, *sys.argv)
    #    > MyWrappedDataclass(a:int = 1, b: str = "2", c:float = 3.0,)
    this_wont_raise_an_error_either = MyWrappedDataclass(1, "2", 3., CustomClassOrWhatever(), c=123.0, does_not_exist=None)
    #    > MyWrappedDataclass(a:int = 1, b: str = "2", c:float = 123.0,)
```

### Possible actions:
  - Ignore:
    Simply ignore unknown arguments passed to the init function
  - WarnThenIgnore:
    Ignore unknown arguments but create UserWarnings
  - Catch:
    Stores unknown arguments in a class unknown_arguments attribute as `([unknown_args], {unknown_keyword_args})`
  - Custom function (`callable`):
    Provide your own function to manage the arguments.

### Custom actions:

To use a custom action define a function and use it for the `action` parameter.
```
def customAction(cls, fields: List[str], args: List[Any], kwargs: Dict[str, Any]):
    """
    cls: The class the action is performed on (instance)
    fields: A list containing the ordered list of __init__ arguments for cls (without self)
    args: Arguments the __init__ function was called with
    kwargs: Dictionary with the keyword arguments the __init__ function was called with.
    
    MUST return:
    [arguments to pass to the original __init__ function], {keyword arguments to pass to the original __init__ function}
    These return arguments will be passed to the cls.__init__ so any unknown fields must be filtered already or the default dataclass exception will be raised
    """
    filtered_args, filtered_kwargs = do_someting(args, kwargs)
    return filtered_args, filtered_kwargs
```

### Install:
> pip install unknown-fields

### Note:
This library is in a **very** early alpha state. Bugs are to be expected.

## License

MIT

