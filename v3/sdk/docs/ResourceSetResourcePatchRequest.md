# ResourceSetResourcePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_resource_patch_request import ResourceSetResourcePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourcePatchRequest from a JSON string
resource_set_resource_patch_request_instance = ResourceSetResourcePatchRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourcePatchRequest.to_json())

# convert the object into a dict
resource_set_resource_patch_request_dict = resource_set_resource_patch_request_instance.to_dict()
# create an instance of ResourceSetResourcePatchRequest from a dict
resource_set_resource_patch_request_form_dict = resource_set_resource_patch_request.from_dict(resource_set_resource_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

