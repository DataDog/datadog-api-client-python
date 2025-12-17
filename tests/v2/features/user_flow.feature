@endpoint(user-flow) @endpoint(user-flow-v2)
Feature: User Flow
  API for user flow.

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Get rum sankey returns "Successful response with Sankey diagram data" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "UserFlow" API
    And operation "GetRumSankey" enabled
    And new "GetRumSankey" request
    And body with value {"data": {"attributes": {"data_source": "", "definition": {"entries_per_step": 10, "number_of_steps": 5, "source": "@view.name", "target": "@view.name"}, "enforced_execution_type": "", "request_id": "", "sampling": {"enabled": true}, "search": {"audience_filters": {}, "query": "@type:view @application.id:*", "subquery_id": ""}, "time": {"from": 1756425600000, "to": 1756857600000}}, "id": "sankey_request", "type": "sankey_request"}}
    When the request is sent
    Then the response status is 200 Successful response with Sankey diagram data
