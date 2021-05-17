# WidgetCustomLink

Custom links help you connect a data value to a URL, like a Datadog page or your AWS console.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_hidden** | **bool** | The flag for toggling context menu link visibility. | [optional] 
**label** | **str** | The label for the custom link URL. Keep the label short and descriptive. Use metrics and tags as variables. | [optional] 
**link** | **str** | The URL of the custom link. URL must include &#x60;http&#x60; or &#x60;https&#x60;. A relative URL must start with &#x60;/&#x60;. | [optional] 
**override_label** | **str** | The label ID that refers to a context menu link. Can be &#x60;logs&#x60;, &#x60;hosts&#x60;, &#x60;traces&#x60;, &#x60;profiles&#x60;, &#x60;processes&#x60;, &#x60;containers&#x60;, or &#x60;rum&#x60;. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


