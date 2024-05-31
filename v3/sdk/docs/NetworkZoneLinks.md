# NetworkZoneLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**deactivate** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.network_zone_links import NetworkZoneLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneLinks from a JSON string
network_zone_links_instance = NetworkZoneLinks.from_json(json)
# print the JSON string representation of the object
print(NetworkZoneLinks.to_json())

# convert the object into a dict
network_zone_links_dict = network_zone_links_instance.to_dict()
# create an instance of NetworkZoneLinks from a dict
network_zone_links_form_dict = network_zone_links.from_dict(network_zone_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

