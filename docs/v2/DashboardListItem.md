# DashboardListItem

A dashboard within a list.

## Properties

| Name             | Type                                  | Description                                       | Notes                 |
| ---------------- | ------------------------------------- | ------------------------------------------------- | --------------------- |
| **id**           | **str**                               | ID of the dashboard.                              |
| **type**         | [**DashboardType**](DashboardType.md) |                                                   |
| **author**       | [**Creator**](Creator.md)             |                                                   | [optional]            |
| **created**      | **datetime**                          | Date of creation of the dashboard.                | [optional] [readonly] |
| **icon**         | **str**                               | URL to the icon of the dashboard.                 | [optional] [readonly] |
| **is_favorite**  | **bool**                              | Whether or not the dashboard is in the favorites. | [optional] [readonly] |
| **is_read_only** | **bool**                              | Whether or not the dashboard is read only.        | [optional] [readonly] |
| **is_shared**    | **bool**                              | Whether the dashboard is publicly shared or not.  | [optional] [readonly] |
| **modified**     | **datetime**                          | Date of last edition of the dashboard.            | [optional] [readonly] |
| **popularity**   | **int**                               | Popularity of the dashboard.                      | [optional] [readonly] |
| **title**        | **str**                               | Title of the dashboard.                           | [optional] [readonly] |
| **url**          | **str**                               | URL path to the dashboard.                        | [optional] [readonly] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
