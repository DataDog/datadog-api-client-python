# logs_group_by_histogram.LogsGroupByHistogram

Used to perform a histogram computation (only for measure facets). Note: At most 100 buckets are allowed, the number of buckets is (max - min)/interval.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **float** | The bin size of the histogram buckets | 
**max** | **float** | The maximum value for the measure used in the histogram (values greater than this one are filtered out) | 
**min** | **float** | The minimum value for the measure used in the histogram (values smaller than this one are filtered out) | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)


