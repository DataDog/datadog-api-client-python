# SecurityFilterAttributes

The object describing a security filter.

## Properties

| Name                   | Type                                                                                    | Description                                                                             | Notes      |
| ---------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------- |
| **exclusion_filters**  | [**[SecurityFilterExclusionFilterResponse]**](SecurityFilterExclusionFilterResponse.md) | The list of exclusion filters applied in this security filter.                          | [optional] |
| **filtered_data_type** | [**SecurityFilterFilteredDataType**](SecurityFilterFilteredDataType.md)                 |                                                                                         | [optional] |
| **is_builtin**         | **bool**                                                                                | Whether the security filter is the built-in filter.                                     | [optional] |
| **is_enabled**         | **bool**                                                                                | Whether the security filter is enabled.                                                 | [optional] |
| **name**               | **str**                                                                                 | The security filter name.                                                               | [optional] |
| **query**              | **str**                                                                                 | The security filter query. Logs accepted by this query will be accepted by this filter. | [optional] |
| **version**            | **int**                                                                                 | The version of the security filter.                                                     | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
