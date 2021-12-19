# SLOCorrectionCreateRequestAttributes

The attribute object associated with the SLO correction to be created.

## Properties

| Name            | Type                                                  | Description                                                                                                                                                                             | Notes      |
| --------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **category**    | [**SLOCorrectionCategory**](SLOCorrectionCategory.md) |                                                                                                                                                                                         |
| **slo_id**      | **str**                                               | ID of the SLO that this correction will be applied to.                                                                                                                                  |
| **start**       | **int**                                               | Starting time of the correction in epoch seconds.                                                                                                                                       |
| **description** | **str**                                               | Description of the correction being made.                                                                                                                                               | [optional] |
| **duration**    | **int**                                               | Length of time (in seconds) for a specified &#x60;rrule&#x60; recurring SLO correction.                                                                                                 | [optional] |
| **end**         | **int**                                               | Ending time of the correction in epoch seconds.                                                                                                                                         | [optional] |
| **rrule**       | **str**                                               | The recurrence rules as defined in the iCalendar RFC 5545. The supported rules for SLO corrections are &#x60;FREQ&#x60;, &#x60;INTERVAL&#x60;, &#x60;COUNT&#x60; and &#x60;UNTIL&#x60;. | [optional] |
| **timezone**    | **str**                                               | The timezone to display in the UI for the correction times (defaults to \&quot;UTC\&quot;).                                                                                             | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
