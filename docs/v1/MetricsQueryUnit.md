# MetricsQueryUnit

Object containing the metric unit family, scale factor, name, and short name.

## Properties

| Name             | Type      | Description                                                                       | Notes                 |
| ---------------- | --------- | --------------------------------------------------------------------------------- | --------------------- |
| **family**       | **str**   | Unit family, allows for conversion between units of the same family, for scaling. | [optional] [readonly] |
| **name**         | **str**   | Unit name                                                                         | [optional] [readonly] |
| **plural**       | **str**   | Plural form of the unit name.                                                     | [optional] [readonly] |
| **scale_factor** | **float** | Factor for scaling between units of the same family.                              | [optional] [readonly] |
| **short_name**   | **str**   | Abbreviation of the unit.                                                         | [optional] [readonly] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
