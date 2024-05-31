# TotpUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**TotpUserFactorProfile**](TotpUserFactorProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.totp_user_factor import TotpUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of TotpUserFactor from a JSON string
totp_user_factor_instance = TotpUserFactor.from_json(json)
# print the JSON string representation of the object
print(TotpUserFactor.to_json())

# convert the object into a dict
totp_user_factor_dict = totp_user_factor_instance.to_dict()
# create an instance of TotpUserFactor from a dict
totp_user_factor_form_dict = totp_user_factor.from_dict(totp_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

