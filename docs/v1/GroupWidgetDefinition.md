# GroupWidgetDefinition

The groups widget allows you to keep similar graphs together on your timeboard. Each group has a custom header, can hold one to many graphs, and is collapsible.

## Properties

| Name                 | Type                                                          | Description                                        | Notes                                                               |
| -------------------- | ------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| **layout_type**      | [**WidgetLayoutType**](WidgetLayoutType.md)                   |                                                    |
| **type**             | [**GroupWidgetDefinitionType**](GroupWidgetDefinitionType.md) |                                                    |
| **widgets**          | [**[Widget]**](Widget.md)                                     | List of widget groups.                             |
| **background_color** | **str**                                                       | Background color of the group title.               | [optional]                                                          |
| **banner_img**       | **str**                                                       | URL of image to display as a banner for the group. | [optional]                                                          |
| **show_title**       | **bool**                                                      | Whether to show the title or not.                  | [optional] if omitted the server will use the default value of True |
| **title**            | **str**                                                       | Title of the widget.                               | [optional]                                                          |
| **title_align**      | [**WidgetTextAlign**](WidgetTextAlign.md)                     |                                                    | [optional]                                                          |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
