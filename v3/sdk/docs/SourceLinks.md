# SourceLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**var_schema** | [**SourceLinksAllOfSchema**](SourceLinksAllOfSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.source_links import SourceLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SourceLinks from a JSON string
source_links_instance = SourceLinks.from_json(json)
# print the JSON string representation of the object
print(SourceLinks.to_json())

# convert the object into a dict
source_links_dict = source_links_instance.to_dict()
# create an instance of SourceLinks from a dict
source_links_form_dict = source_links.from_dict(source_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

