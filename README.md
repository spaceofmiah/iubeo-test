# iubeo-test
Friendlier way to write your config.

This repo is just to replicate issues encountered when using `iubeo` library ([track resolved issue](https://github.com/isik-kaplan/iubeo/issues/3))

Traceback
---

```
Traceback (most recent call last):
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\iubeo\utils.py", line 15, in wrapper
    return f(value)
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\iubeo\casters.py", line 23, in boolean
    raise ValueError('Value "{}" can not be parsed into a boolean.'.format(value))
ValueError: Value "None" can not be parsed into a boolean.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\django\core\management\__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\django\core\management\__init__.py", line 345, in execute
    settings.INSTALLED_APPS
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\django\conf\__init__.py", line 82, in __getattr__
    self._setup(name)
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\django\conf\__init__.py", line 69, in _setup
    self._wrapped = Settings(settings_module)
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\django\conf\__init__.py", line 170, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "C:\Users\miah\AppData\Local\Programs\Python\Python38-32\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\miah\code\django\test-iubeo\core\settings.py", line 20, in <module>
    DEBUG = CONFIG.DEBUG
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\iubeo\config.py", line 18, in __getattr__
    return raise_config_error_instead(cast)(os.environ.get(var))
  File "C:\Users\miah\code\django\test-iubeo\env\lib\site-packages\iubeo\utils.py", line 17, in wrapper
    raise ConfigError("Error while parsing value with {}".format(f.__name__)) from e
iubeo.exceptions.ConfigError: Error while parsing value with boolean
```
