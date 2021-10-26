# AlertValueWidgetDefinition

Alert values are query values showing the current value of the metric in any monitor defined on your system.

## Properties

| Name            | Type                                                                    | Description                                                        | Notes      |
| --------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **alert_id**    | **str**                                                                 | ID of the alert to use in the widget.                              |
| **type**        | [**AlertValueWidgetDefinitionType**](AlertValueWidgetDefinitionType.md) |                                                                    |
| **precision**   | **int**                                                                 | Number of decimal to show. If not defined, will use the raw value. | [optional] |
| **text_align**  | [**WidgetTextAlign**](WidgetTextAlign.md)                               |                                                                    | [optional] |
| **title**       | **str**                                                                 | Title of the widget.                                               | [optional] |
| **title_align** | [**WidgetTextAlign**](WidgetTextAlign.md)                               |                                                                    | [optional] |
| **title_size**  | **str**                                                                 | Size of value in the widget.                                       | [optional] |
| **unit**        | **str**                                                                 | Unit to display with the value.                                    | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
