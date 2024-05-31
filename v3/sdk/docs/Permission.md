# Permission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **object** | Conditions for further restricting a permission | [optional] 
**created** | **datetime** | Timestamp when the role was created | [optional] [readonly] 
**label** | **str** | The permission type | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the role was last updated | [optional] [readonly] 
**links** | [**PermissionLinks**](PermissionLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print(Permission.to_json())

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_form_dict = permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

