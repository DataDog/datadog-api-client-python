# SecurityMonitoringRuleCaseCreate

Case when signal is generated.

## Properties

| Name              | Type                                                                    | Description                                                                                                      | Notes      |
| ----------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------- | ---------- |
| **status**        | [**SecurityMonitoringRuleSeverity**](SecurityMonitoringRuleSeverity.md) |                                                                                                                  |
| **condition**     | **str**                                                                 | A rule case contains logical operations (&#x60;&gt;&#x60;,&#x60;&gt;&#x3D;&#x60;, &#x60;&amp;&amp;&#x60;, &#x60; |            | &#x60;) to determine if a signal should be generated based on the event counts in the previously defined queries. | [optional] |
| **name**          | **str**                                                                 | Name of the case.                                                                                                | [optional] |
| **notifications** | **[str]**                                                               | Notification targets for each rule case.                                                                         | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
