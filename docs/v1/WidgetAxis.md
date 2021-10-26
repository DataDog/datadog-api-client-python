# WidgetAxis

Axis controls for the widget.

## Properties

| Name             | Type     | Description                                                                                                                                                              | Notes                                                                   |
| ---------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| **include_zero** | **bool** | True includes zero.                                                                                                                                                      | [optional]                                                              |
| **label**        | **str**  | The label of the axis to display on the graph.                                                                                                                           | [optional]                                                              |
| **max**          | **str**  | Specifies the maximum value to show on the y-axis. It takes a number, or auto for default behavior.                                                                      | [optional] if omitted the server will use the default value of "auto"   |
| **min**          | **str**  | Specifies minimum value to show on the y-axis. It takes a number, or auto for default behavior.                                                                          | [optional] if omitted the server will use the default value of "auto"   |
| **scale**        | **str**  | Specifies the scale type. Possible values are &#x60;linear&#x60;, &#x60;log&#x60;, &#x60;sqrt&#x60;, &#x60;pow##&#x60; (e.g. &#x60;pow2&#x60;, &#x60;pow0.5&#x60; etc.). | [optional] if omitted the server will use the default value of "linear" |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
