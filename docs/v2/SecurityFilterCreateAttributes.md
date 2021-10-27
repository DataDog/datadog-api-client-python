# SecurityFilterCreateAttributes

Object containing the attributes of the security filter to be created.

## Properties

| Name                   | Type                                                                    | Description                                                      | Notes |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------- | ----- |
| **exclusion_filters**  | [**[SecurityFilterExclusionFilter]**](SecurityFilterExclusionFilter.md) | Exclusion filters to exclude some logs from the security filter. |
| **filtered_data_type** | [**SecurityFilterFilteredDataType**](SecurityFilterFilteredDataType.md) |                                                                  |
| **is_enabled**         | **bool**                                                                | Whether the security filter is enabled.                          |
| **name**               | **str**                                                                 | The name of the security filter.                                 |
| **query**              | **str**                                                                 | The query of the security filter.                                |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
