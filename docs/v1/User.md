# User

Create, edit, and disable users.

## Properties

| Name         | Type     | Description                                              | Notes                 |
| ------------ | -------- | -------------------------------------------------------- | --------------------- |
| **disabled** | **bool** | The new disabled status of the user.                     | [optional]            |
| **email**    | **str**  | The new email of the user.                               | [optional]            |
| **handle**   | **str**  | The user handle, must be a valid email.                  | [optional]            |
| **icon**     | **str**  | Gravatar icon associated to the user.                    | [optional] [readonly] |
| **name**     | **str**  | The name of the user.                                    | [optional]            |
| **verified** | **bool** | Whether or not the user logged in Datadog at least once. | [optional] [readonly] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
