# SLOCorrectionUpdateRequestAttributes

The attribute object associated with the SLO correction to be updated.

## Properties

| Name            | Type                                                  | Description                                                                                 | Notes      |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------- |
| **category**    | [**SLOCorrectionCategory**](SLOCorrectionCategory.md) |                                                                                             | [optional] |
| **description** | **str**                                               | Description of the correction being made.                                                   | [optional] |
| **duration**    | **int**                                               | Length of time (in seconds) for a specified &#x60;rrule&#x60; recurring SLO correction.     | [optional] |
| **end**         | **int**                                               | Ending time of the correction in epoch seconds.                                             | [optional] |
| **rrule**       | **str**                                               | Recurrence rules as defined in the iCalendar RFC 5545.                                      | [optional] |
| **start**       | **int**                                               | Starting time of the correction in epoch seconds.                                           | [optional] |
| **timezone**    | **str**                                               | The timezone to display in the UI for the correction times (defaults to \&quot;UTC\&quot;). | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
