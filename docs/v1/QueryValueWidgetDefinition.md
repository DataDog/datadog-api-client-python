# QueryValueWidgetDefinition

Query values display the current value of a given metric, APM, or log query.

## Properties

| Name             | Type                                                                    | Description                                                                | Notes      |
| ---------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------- |
| **requests**     | [**[QueryValueWidgetRequest]**](QueryValueWidgetRequest.md)             | Widget definition.                                                         |
| **type**         | [**QueryValueWidgetDefinitionType**](QueryValueWidgetDefinitionType.md) |                                                                            |
| **autoscale**    | **bool**                                                                | Whether to use auto-scaling or not.                                        | [optional] |
| **custom_links** | [**[WidgetCustomLink]**](WidgetCustomLink.md)                           | List of custom links.                                                      | [optional] |
| **custom_unit**  | **str**                                                                 | Display a unit of your choice on the widget.                               | [optional] |
| **precision**    | **int**                                                                 | Number of decimals to show. If not defined, the widget uses the raw value. | [optional] |
| **text_align**   | [**WidgetTextAlign**](WidgetTextAlign.md)                               |                                                                            | [optional] |
| **time**         | [**WidgetTime**](WidgetTime.md)                                         |                                                                            | [optional] |
| **title**        | **str**                                                                 | Title of your widget.                                                      | [optional] |
| **title_align**  | [**WidgetTextAlign**](WidgetTextAlign.md)                               |                                                                            | [optional] |
| **title_size**   | **str**                                                                 | Size of the title.                                                         | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
