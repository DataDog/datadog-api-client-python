# Widget

Information about widget. **Note**: The `layout` property is required for widgets in dashboards with `free` `layout_type`. For the **new dashboard layout**, the `layout` property depends on the `reflow_type` of the dashboard. - If `reflow_type` is `fixed`, `layout` is required. - If `reflow_type` is `auto`, `layout` should not be set.

## Properties

| Name           | Type                                        | Description       | Notes      |
| -------------- | ------------------------------------------- | ----------------- | ---------- |
| **definition** | [**WidgetDefinition**](WidgetDefinition.md) |                   |
| **id**         | **int**                                     | ID of the widget. | [optional] |
| **layout**     | [**WidgetLayout**](WidgetLayout.md)         |                   | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
