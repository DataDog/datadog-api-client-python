# HourlyUsageAttributionBody

The usage for one set of tags for one hour.

## Properties

| Name                  | Type                                                                      | Description                                                                                                                                                                                                  | Notes      |
| --------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **hour**              | **datetime**                                                              | The hour for the usage.                                                                                                                                                                                      | [optional] |
| **org_name**          | **str**                                                                   | The name of the organization.                                                                                                                                                                                | [optional] |
| **public_id**         | **str**                                                                   | The organization public ID.                                                                                                                                                                                  | [optional] |
| **tag_config_source** | **str**                                                                   | The source of the usage attribution tag configuration and the selected tags in the format of &#x60;&lt;source_org_name&gt;:::&lt;selected tag 1&gt;///&lt;selected tag 2&gt;///&lt;selected tag 3&gt;&#x60;. | [optional] |
| **tags**              | [**UsageAttributionTagNames**](UsageAttributionTagNames.md)               |                                                                                                                                                                                                              | [optional] |
| **total_usage_sum**   | **float**                                                                 | Total product usage for the given tags within the hour.                                                                                                                                                      | [optional] |
| **updated_at**        | **str**                                                                   | Shows the most recent hour in the current month for all organizations where usages are calculated.                                                                                                           | [optional] |
| **usage_type**        | [**HourlyUsageAttributionUsageType**](HourlyUsageAttributionUsageType.md) |                                                                                                                                                                                                              | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
