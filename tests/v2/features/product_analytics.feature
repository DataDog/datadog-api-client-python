@endpoint(product-analytics) @endpoint(product-analytics-v2)
Feature: Product Analytics
  Send server-side events to Product Analytics. Server-Side Events Ingestion
  allows you to collect custom events from any server-side source, and
  retains events for 15 months. Server-side events are helpful for
  understanding causes of a funnel drop-off which are external to the
  client-side (for example, payment processing error).  **Note**: Sending
  server-side events impacts billing. Review the [pricing
  page](https://www.datadoghq.com/pricing/?product=product-
  analytics#products) and contact your Customer Success Manager for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "ProductAnalytics" API

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute a Sankey diagram returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsSankey" enabled
    And new "QueryProductAnalyticsSankey" request
    And body with value {"data": {"attributes": {"definition": {"entries_per_step": 10, "number_of_steps": 3, "source": "@view.name", "target": "@view.name"}, "search": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "query": "@type:view"}, "time": {"from": 1756425600000, "to": 1756857600000}}, "type": "sankey_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute a Sankey diagram returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsSankey" enabled
    And new "QueryProductAnalyticsSankey" request
    And body with value {"data": {"attributes": {"definition": {"entries_per_step": 10, "number_of_steps": 3, "source": "@view.name", "target": "@view.name"}, "search": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "query": "@type:view"}, "time": {"from": 1756425600000, "to": 1756857600000}}, "type": "sankey_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute a retention grid returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionGrid" enabled
    And new "QueryProductAnalyticsRetentionGrid" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"computation_scope": {"target": {"type": "index", "value": 0}, "type": "cohort"}, "compute": {"aggregation": "count", "metric": "__dd.retention_rate"}, "group_by": [{"facet": "@geo.country", "limit": 10, "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "target": "cohort"}], "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "retention_grid_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute a retention grid returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionGrid" enabled
    And new "QueryProductAnalyticsRetentionGrid" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"computation_scope": {"target": {"type": "index", "value": 0}, "type": "cohort"}, "compute": {"aggregation": "count", "metric": "__dd.retention_rate"}, "group_by": [{"facet": "@geo.country", "limit": 10, "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "target": "cohort"}], "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "retention_grid_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute journey funnel analysis returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyFunnel" enabled
    And new "QueryProductAnalyticsJourneyFunnel" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"compute": {}, "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}}, "to": 1756857600000}, "type": "journey_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute journey funnel analysis returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyFunnel" enabled
    And new "QueryProductAnalyticsJourneyFunnel" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"compute": {}, "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}}, "to": 1756857600000}, "type": "journey_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute journey scalar analytics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyScalar" enabled
    And new "QueryProductAnalyticsJourneyScalar" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"compute": {"aggregation": "count", "target": {"type": "node", "value": "A"}}, "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}}, "to": 1756857600000}, "type": "formula_journey_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute journey scalar analytics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyScalar" enabled
    And new "QueryProductAnalyticsJourneyScalar" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"compute": {"aggregation": "count", "target": {"type": "node", "value": "A"}}, "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}}, "to": 1756857600000}, "type": "formula_journey_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute journey timeseries analytics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyTimeseries" enabled
    And new "QueryProductAnalyticsJourneyTimeseries" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"compute": {"aggregation": "count", "target": {"type": "node", "value": "A"}}, "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}}, "to": 1756857600000}, "type": "formula_journey_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute journey timeseries analytics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyTimeseries" enabled
    And new "QueryProductAnalyticsJourneyTimeseries" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"compute": {"aggregation": "count", "target": {"type": "node", "value": "A"}}, "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}}, "to": 1756857600000}, "type": "formula_journey_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute retention scalar values returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionScalar" enabled
    And new "QueryProductAnalyticsRetentionScalar" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"computation_scope": {"target": {"type": "index", "value": 0}, "type": "cohort"}, "compute": {"aggregation": "count", "metric": "__dd.retention_rate"}, "group_by": [{"facet": "@geo.country", "limit": 10, "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "target": "cohort"}], "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "formula_retention_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute retention scalar values returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionScalar" enabled
    And new "QueryProductAnalyticsRetentionScalar" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"computation_scope": {"target": {"type": "index", "value": 0}, "type": "cohort"}, "compute": {"aggregation": "count", "metric": "__dd.retention_rate"}, "group_by": [{"facet": "@geo.country", "limit": 10, "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "target": "cohort"}], "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "formula_retention_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute retention timeseries returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionTimeseries" enabled
    And new "QueryProductAnalyticsRetentionTimeseries" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"computation_scope": {"target": {"type": "index", "value": 0}, "type": "cohort"}, "compute": {"aggregation": "count", "metric": "__dd.retention_rate"}, "group_by": [{"facet": "@geo.country", "limit": 10, "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "target": "cohort"}], "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "formula_retention_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute retention timeseries returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionTimeseries" enabled
    And new "QueryProductAnalyticsRetentionTimeseries" request
    And body with value {"data": {"attributes": {"exclude_anonymous_traffic": false, "from": 1756425600000, "query": {"computation_scope": {"target": {"type": "index", "value": 0}, "type": "cohort"}, "compute": {"aggregation": "count", "metric": "__dd.retention_rate"}, "group_by": [{"facet": "@geo.country", "limit": 10, "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "target": "cohort"}], "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "formula_retention_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute scalar analytics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsScalar" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute scalar analytics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsScalar" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute timeseries analytics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsTimeseries" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Compute timeseries analytics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryProductAnalyticsTimeseries" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"compute": {"aggregation": "count"}, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List analytics events returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsList" enabled
    And new "QueryProductAnalyticsList" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"columns": ["@view.name"], "limit": 100, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_list_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List analytics events returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsList" enabled
    And new "QueryProductAnalyticsList" request
    And body with value {"data": {"attributes": {"from": 1771232048460, "query": {"columns": ["@view.name"], "limit": 100, "query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}}, "to": 1771836848262}, "type": "formula_analytics_extended_list_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List journey entities returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyList" enabled
    And new "QueryProductAnalyticsJourneyList" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"computed_columns": [{"name": "first_conversion_timestamps"}], "conversion_type": "conversion", "entity_columns": [], "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}, "sort": {"order": "desc"}, "target": {"type": "node", "value": "A"}}, "to": 1756857600000}, "type": "journey_list_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List journey entities returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsJourneyList" enabled
    And new "QueryProductAnalyticsJourneyList" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"computed_columns": [{"name": "first_conversion_timestamps"}], "conversion_type": "conversion", "entity_columns": [], "group_by": [{"facet": "@geo.country", "should_exclude_missing": false, "sort": {"aggregation": "count", "order": "desc"}, "source": "product_analytics_audience_filters.users", "target": {"type": "node", "value": "A"}, "value_filters": []}], "search": {"expression": "A -> B", "filters": {"audience_filters": {"accounts": [{"name": "enterprise_accounts"}], "formula": "power_users AND NOT trial_segment", "segments": [{"name": "trial_segment", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "power_users"}]}, "graph_filters": [{"name": "__dd.time_to_convert", "operator": "<=", "target": {"type": "node", "value": "A"}, "value": 60000}]}, "join_keys": {"primary": "@session.id", "secondary": []}, "node_objects": {"A": {"data_source": "product_analytics", "search": {"query": "@type:view @view.name:Login"}}, "B": {"data_source": "product_analytics", "search": {"query": "@type:action @action.target.name:Submit"}}}}, "sort": {"order": "desc"}, "target": {"type": "node", "value": "A"}}, "to": 1756857600000}, "type": "journey_list_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List the entities behind a retention cell returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionList" enabled
    And new "QueryProductAnalyticsRetentionList" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"columns": [{"field": {"path": "@usr.email"}}], "computation_scope": {"cohort_target": {"type": "index", "value": 0}, "return_period_target": {"type": "index", "value": 0}, "type": "cell"}, "limit": 100, "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "retention_list_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: List the entities behind a retention cell returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryProductAnalyticsRetentionList" enabled
    And new "QueryProductAnalyticsRetentionList" request
    And body with value {"data": {"attributes": {"from": 1756425600000, "query": {"columns": [{"field": {"path": "@usr.email"}}], "computation_scope": {"cohort_target": {"type": "index", "value": 0}, "return_period_target": {"type": "index", "value": 0}, "type": "cell"}, "limit": 100, "search": {"cohort_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}, "filters": {"audience_filters": {"accounts": [{"name": ""}], "formula": "u", "segments": [{"name": "", "segment_id": "00000000-0000-0000-0000-000000000000"}], "users": [{"name": "u", "query": "*"}]}}, "retention_entity": "@usr.id", "return_condition": "conversion_on_or_after", "return_criteria": {"base_query": {"data_source": "product_analytics", "search": {"query": "@type:view"}}, "time_interval": {"type": "calendar", "value": {"alignment": "monday", "quantity": 1, "timezone": "UTC", "type": "week"}}}}}, "to": 1756857600000}, "type": "retention_list_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Bad Request" response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Payload Too Large" response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 413 Payload Too Large

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Request Timeout" response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 408 Request Timeout

  @generated @skip @team:DataDog/product-analytics-backend
  Scenario: Send server-side events returns "Request accepted for processing (always 202 empty JSON)." response
    Given new "SubmitProductAnalyticsEvent" request
    And body with value {"account": {"id": "account-67890"}, "application": {"id": "123abcde-123a-123b-1234-123456789abc"}, "event": {"name": "payment.processed"}, "session": {"id": "session-abcdef"}, "type": "server", "usr": {"id": "user-12345"}}
    When the request is sent
    Then the response status is 202 Request accepted for processing (always 202 empty JSON).
