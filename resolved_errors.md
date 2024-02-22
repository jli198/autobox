# MOVE RESOLVED ERRORS HERE SO WE KNOW WHAT WAS FIXED

from lambda_function.py:

```
{
  "errorMessage": "The config profile (default) could not be found",
  "errorType": "ProfileNotFound",
  "requestId": "e3ac69b4-f625-4696-9006-d4d10853b567",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 93, in lambda_handler\n    raise e\n",
    "  File \"/var/task/lambda_function.py\", line 80, in lambda_handler\n    textDetections = detect_text(bucket, key)\n",
    "  File \"/var/task/lambda_function.py\", line 41, in detect_text\n    session = boto3.Session(profile_name='default')\n",
    "  File \"/var/lang/lib/python3.12/site-packages/boto3/session.py\", line 90, in __init__\n    self._setup_loader()\n",
    "  File \"/var/lang/lib/python3.12/site-packages/boto3/session.py\", line 131, in _setup_loader\n    self._loader = self._session.get_component('data_loader')\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/session.py\", line 802, in get_component\n    return self._components.get_component(name)\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/session.py\", line 1140, in get_component\n    self._components[name] = factory()\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/session.py\", line 199, in <lambda>\n    lambda: create_loader(self.get_config_variable('data_path')),\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/session.py\", line 323, in get_config_variable\n    return self.get_component('config_store').get_config_variable(\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/configprovider.py\", line 459, in get_config_variable\n    return provider.provide()\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/configprovider.py\", line 665, in provide\n    value = provider.provide()\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/configprovider.py\", line 755, in provide\n    scoped_config = self._session.get_scoped_config()\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/session.py\", line 422, in get_scoped_config\n    raise ProfileNotFound(profile=profile_name)\n"
  ]
}
```


