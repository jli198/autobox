# ADD ANY KNOWN ERROS IN THIS FILE AND REMOVE WHEN RESOLVED

from lambda_function.py:

```
{
  "errorMessage": "An error occurred (InvalidS3ObjectException) when calling the DetectText operation: Unable to get object metadata from S3. Check object key, region and/or access permissions.",
  "errorType": "InvalidS3ObjectException",
  "requestId": "93eefe53-d42e-45b9-9906-6ed5207f4eeb",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 98, in lambda_handler\n    raise e\n",
    "  File \"/var/task/lambda_function.py\", line 85, in lambda_handler\n    textDetections = detect_text(bucket, key)\n",
    "  File \"/var/task/lambda_function.py\", line 49, in detect_text\n    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/client.py\", line 535, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/client.py\", line 980, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"
  ]
}
```

