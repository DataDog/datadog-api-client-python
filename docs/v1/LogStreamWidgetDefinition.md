# LogStreamWidgetDefinition

The Log Stream displays a log flow matching the defined query. Only available on FREE layout dashboards.

## Properties

| Name                    | Type                                                                  | Description                                                                          | Notes      |
| ----------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------- |
| **type**                | [**LogStreamWidgetDefinitionType**](LogStreamWidgetDefinitionType.md) |                                                                                      |
| **columns**             | **[str]**                                                             | Which columns to display on the widget.                                              | [optional] |
| **indexes**             | **[str]**                                                             | An array of index names to query in the stream. Use [] to query all indexes at once. | [optional] |
| **logset**              | **str**                                                               | ID of the log set to use.                                                            | [optional] |
| **message_display**     | [**WidgetMessageDisplay**](WidgetMessageDisplay.md)                   |                                                                                      | [optional] |
| **query**               | **str**                                                               | Query to filter the log stream with.                                                 | [optional] |
| **show_date_column**    | **bool**                                                              | Whether to show the date column or not                                               | [optional] |
| **show_message_column** | **bool**                                                              | Whether to show the message column or not                                            | [optional] |
| **sort**                | [**WidgetFieldSort**](WidgetFieldSort.md)                             |                                                                                      | [optional] |
| **time**                | [**WidgetTime**](WidgetTime.md)                                       |                                                                                      | [optional] |
| **title**               | **str**                                                               | Title of the widget.                                                                 | [optional] |
| **title_align**         | [**WidgetTextAlign**](WidgetTextAlign.md)                             |                                                                                      | [optional] |
| **title_size**          | **str**                                                               | Size of the title.                                                                   | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
