# SecurityFilterUpdateAttributes

The security filters properties to be updated.

## Properties

| Name                   | Type                                                                    | Description                                                      | Notes      |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------- |
| **exclusion_filters**  | [**[SecurityFilterExclusionFilter]**](SecurityFilterExclusionFilter.md) | Exclusion filters to exclude some logs from the security filter. | [optional] |
| **filtered_data_type** | [**SecurityFilterFilteredDataType**](SecurityFilterFilteredDataType.md) |                                                                  | [optional] |
| **is_enabled**         | **bool**                                                                | Whether the security filter is enabled.                          | [optional] |
| **name**               | **str**                                                                 | The name of the security filter.                                 | [optional] |
| **query**              | **str**                                                                 | The query of the security filter.                                | [optional] |
| **version**            | **int**                                                                 | The version of the security filter to update.                    | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
