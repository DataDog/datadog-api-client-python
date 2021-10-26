# UsageAttributionBody

Usage Summary by tag for a given organization.

## Properties

| Name                  | Type                                                        | Description                                                                                                                                                                                         | Notes      |
| --------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **month**             | **datetime**                                                | Datetime in ISO-8601 format, UTC, precise to month: [YYYY-MM].                                                                                                                                      | [optional] |
| **org_name**          | **str**                                                     | The name of the organization.                                                                                                                                                                       | [optional] |
| **public_id**         | **str**                                                     | The organization public ID.                                                                                                                                                                         | [optional] |
| **tag_config_source** | **str**                                                     | The source of the usage attribution tag configuration and the selected tags in the format &#x60;&lt;source_org_name&gt;:&lt;selected tag 1&gt;-&lt;selected tag 2&gt;-&lt;selected tag 3&gt;&#x60;. | [optional] |
| **tags**              | [**UsageAttributionTagNames**](UsageAttributionTagNames.md) |                                                                                                                                                                                                     | [optional] |
| **updated_at**        | **str**                                                     | Shows the the most recent hour in the current months for all organizations for which all usages were calculated.                                                                                    | [optional] |
| **values**            | [**UsageAttributionValues**](UsageAttributionValues.md)     |                                                                                                                                                                                                     | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
