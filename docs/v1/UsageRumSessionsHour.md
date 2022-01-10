# UsageRumSessionsHour

Number of RUM Sessions recorded for each hour for a given organization.

## Properties

| Name                      | Type         | Description                                                                                        | Notes      |
| ------------------------- | ------------ | -------------------------------------------------------------------------------------------------- | ---------- |
| **hour**                  | **datetime** | The hour for the usage.                                                                            | [optional] |
| **org_name**              | **str**      | The organization name.                                                                             | [optional] |
| **public_id**             | **str**      | The organization public ID.                                                                        | [optional] |
| **replay_session_count**  | **int**      | Contains the number of RUM Replay Sessions (data available beginning November 1, 2021).            | [optional] |
| **session_count**         | **int**      | Contains the number of browser RUM Lite Sessions.                                                  | [optional] |
| **session_count_android** | **int**      | Contains the number of mobile RUM Sessions on Android (data available beginning December 1, 2020). | [optional] |
| **session_count_ios**     | **int**      | Contains the number of mobile RUM Sessions on iOS (data available beginning December 1, 2020).     | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
