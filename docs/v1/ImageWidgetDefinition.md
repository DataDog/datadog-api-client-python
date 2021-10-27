# ImageWidgetDefinition

The image widget allows you to embed an image on your dashboard. An image can be a PNG, JPG, or animated GIF. Only available on FREE layout dashboards.

## Properties

| Name                 | Type                                                          | Description                             | Notes                                                               |
| -------------------- | ------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| **type**             | [**ImageWidgetDefinitionType**](ImageWidgetDefinitionType.md) |                                         |
| **url**              | **str**                                                       | URL of the image.                       |
| **has_background**   | **bool**                                                      | Whether to display a background or not. | [optional] if omitted the server will use the default value of True |
| **has_border**       | **bool**                                                      | Whether to display a border or not.     | [optional] if omitted the server will use the default value of True |
| **horizontal_align** | [**WidgetHorizontalAlign**](WidgetHorizontalAlign.md)         |                                         | [optional]                                                          |
| **margin**           | [**WidgetMargin**](WidgetMargin.md)                           |                                         | [optional]                                                          |
| **sizing**           | [**WidgetImageSizing**](WidgetImageSizing.md)                 |                                         | [optional]                                                          |
| **url_dark_theme**   | **str**                                                       | URL of the image in dark mode.          | [optional]                                                          |
| **vertical_align**   | [**WidgetVerticalAlign**](WidgetVerticalAlign.md)             |                                         | [optional]                                                          |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
