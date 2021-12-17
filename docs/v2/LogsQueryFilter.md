# LogsQueryFilter

The search and filter query settings

## Properties

| Name        | Type      | Description                                                                                                    | Notes                                                                    |
| ----------- | --------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **\_from**  | **str**   | The minimum time for the requested logs, supports date math and regular timestamps (milliseconds).             | [optional] if omitted the server will use the default value of "now-15m" |
| **indexes** | **[str]** | For customers with multiple indexes, the indexes to search. Defaults to [&#39;*&#39;] which means all indexes. | [optional] if omitted the server will use the default value of ["*"]     |
| **query**   | **str**   | The search query - following the log search syntax.                                                            | [optional] if omitted the server will use the default value of "\*"      |
| **to**      | **str**   | The maximum time for the requested logs, supports date math and regular timestamps (milliseconds).             | [optional] if omitted the server will use the default value of "now"     |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
