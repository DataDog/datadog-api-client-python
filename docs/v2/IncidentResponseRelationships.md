# IncidentResponseRelationships

The incident's relationships from a response.

## Properties

| Name                      | Type                                                                                            | Description | Notes      |
| ------------------------- | ----------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **commander_user**        | [**NullableRelationshipToUser**](NullableRelationshipToUser.md)                                 |             | [optional] |
| **created_by_user**       | [**RelationshipToUser**](RelationshipToUser.md)                                                 |             | [optional] |
| **integrations**          | [**RelationshipToIncidentIntegrationMetadatas**](RelationshipToIncidentIntegrationMetadatas.md) |             | [optional] |
| **last_modified_by_user** | [**RelationshipToUser**](RelationshipToUser.md)                                                 |             | [optional] |
| **postmortem**            | [**RelationshipToIncidentPostmortem**](RelationshipToIncidentPostmortem.md)                     |             | [optional] |

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to README]](README.md)
