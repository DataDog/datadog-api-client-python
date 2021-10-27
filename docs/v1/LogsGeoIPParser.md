# LogsGeoIPParser

The GeoIP parser takes an IP address attribute and extracts if available the Continent, Country, Subdivision, and City information in the target attribute path.

## Properties

| Name           | Type                                              | Description                                                                                        | Notes                                                                |
| -------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **type**       | [**LogsGeoIPParserType**](LogsGeoIPParserType.md) |                                                                                                    |
| **sources**    | **[str]**                                         | Array of source attributes.                                                                        | defaults to ["network.client.ip"]                                    |
| **target**     | **str**                                           | Name of the parent attribute that contains all the extracted details from the &#x60;sources&#x60;. | defaults to "network.client.geoip"                                   |
| **is_enabled** | **bool**                                          | Whether or not the processor is enabled.                                                           | [optional] if omitted the server will use the default value of False |
| **name**       | **str**                                           | Name of the processor.                                                                             | [optional]                                                           |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
