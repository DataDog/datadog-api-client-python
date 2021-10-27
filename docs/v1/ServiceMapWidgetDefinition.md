# ServiceMapWidgetDefinition

This widget displays a map of a service to all of the services that call it, and all of the services that it calls.

## Properties

| Name             | Type                                                                    | Description                                                           | Notes      |
| ---------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------- |
| **filters**      | **[str]**                                                               | Your environment and primary tag (or \* if enabled for your account). |
| **service**      | **str**                                                                 | The ID of the service you want to map.                                |
| **type**         | [**ServiceMapWidgetDefinitionType**](ServiceMapWidgetDefinitionType.md) |                                                                       |
| **custom_links** | [**[WidgetCustomLink]**](WidgetCustomLink.md)                           | List of custom links.                                                 | [optional] |
| **title**        | **str**                                                                 | The title of your widget.                                             | [optional] |
| **title_align**  | [**WidgetTextAlign**](WidgetTextAlign.md)                               |                                                                       | [optional] |
| **title_size**   | **str**                                                                 | Size of the title.                                                    | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
