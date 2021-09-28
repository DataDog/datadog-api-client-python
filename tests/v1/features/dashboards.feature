@endpoint(dashboards) @endpoint(dashboards-v1)
Feature: Dashboards
  Interact with your dashboard lists through the API to make it easier to
  organize, find, and share all of your dashboards with your team and
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Dashboards" API

  @generated @skip
  Scenario: Create a new dashboard returns "Bad Request" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [null], "reflow_type": "auto", "restricted_roles": [null], "template_variable_presets": [{"name": null, "template_variables": [{"name": null, "value": null}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "system.cpu.user"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a new dashboard returns "OK" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [null], "reflow_type": "auto", "restricted_roles": [null], "template_variable_presets": [{"name": null, "template_variables": [{"name": null, "value": null}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "system.cpu.user"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new dashboard with a profile metric query
    Given new "CreateDashboard" request
    And body from file "dashboard_payload.json"
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new dashboard with a query value widget using the percentile aggregator
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with QVW Percentile Aggregator", "widgets": [{"definition":{"title_size":"16","title":"","title_align":"left","precision":2,"time":{},"autoscale":true,"requests":[{"formulas":[{"formula":"query1"}],"response_format":"scalar","queries":[{"query":"p90:dist.dd.dogweb.latency{*}","data_source":"metrics","name":"query1","aggregator":"percentile"}]}],"type":"query_value"},"layout":{"y":0,"x":0,"height":2,"width":2}}]}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new dashboard with an audit logs query
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with Audit Logs Query", "widgets": [{"definition": {"type": "timeseries","requests": [{"response_format": "timeseries","queries": [{"search": {"query": ""},"data_source": "audit","compute": {"aggregation": "count"},"name": "query1","indexes": ["*"],"group_by": []}]}]},"layout": {"x": 2,"y": 0,"width": 4,"height": 2}}]}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new dashboard with apm dependency stats widget
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [{"definition": { "title": "", "title_size": "16", "title_align": "left", "type": "query_table", "requests": [ { "response_format": "scalar", "queries": [ { "primary_tag_value": "edge-eu1.prod.dog", "stat": "avg_duration", "resource_name": "DELETE FROM monitor_history.monitor_state_change_history WHERE org_id = ? AND monitor_id IN ? AND group = ?", "name": "query1", "service": "cassandra", "data_source": "apm_dependency_stats", "env": "ci", "primary_tag_name": "datacenter", "operation_name": "cassandra.query" } ] } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].queries[0].primary_tag_value" is equal to "edge-eu1.prod.dog"
    And the response "widgets[0].definition.requests[0].queries[0].stat" is equal to "avg_duration"
    And the response "widgets[0].definition.requests[0].queries[0].resource_name" is equal to "DELETE FROM monitor_history.monitor_state_change_history WHERE org_id = ? AND monitor_id IN ? AND group = ?"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].service" is equal to "cassandra"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "apm_dependency_stats"
    And the response "widgets[0].definition.requests[0].queries[0].env" is equal to "ci"
    And the response "widgets[0].definition.requests[0].queries[0].primary_tag_name" is equal to "datacenter"
    And the response "widgets[0].definition.requests[0].queries[0].operation_name" is equal to "cassandra.query"

  Scenario: Create a new dashboard with apm resource stats widget
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [{"definition": { "title": "", "title_size": "16", "title_align": "left", "type": "query_table", "requests": [ { "response_format": "scalar", "queries": [ { "primary_tag_value": "edge-eu1.prod.dog", "stat": "hits", "name": "query1", "service": "cassandra", "data_source": "apm_resource_stats", "env": "ci", "primary_tag_name": "datacenter", "operation_name": "cassandra.query", "group_by": ["resource_name"] } ] } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].queries[0].primary_tag_value" is equal to "edge-eu1.prod.dog"
    And the response "widgets[0].definition.requests[0].queries[0].stat" is equal to "hits"
    And the response "widgets[0].definition.requests[0].queries[0].group_by[0]" is equal to "resource_name"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].service" is equal to "cassandra"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "apm_resource_stats"
    And the response "widgets[0].definition.requests[0].queries[0].env" is equal to "ci"
    And the response "widgets[0].definition.requests[0].queries[0].primary_tag_name" is equal to "datacenter"
    And the response "widgets[0].definition.requests[0].queries[0].operation_name" is equal to "cassandra.query"

  Scenario: Create a new dashboard with formulas and functions scatterplot widget
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "id": 5346764334358972, "definition": { "title": "", "title_size": "16", "title_align": "left", "type": "scatterplot", "requests": { "table": { "formulas": [ { "formula": "query1", "dimension": "x", "alias": "my-query1" }, { "formula": "query2", "dimension": "y", "alias": "my-query2" } ], "queries": [ { "data_source": "metrics", "name": "query1", "query": "avg:system.cpu.user{*} by {service}", "aggregator": "avg" }, { "data_source": "metrics", "name": "query2", "query": "avg:system.mem.used{*} by {service}", "aggregator": "avg" } ], "response_format": "scalar" } } }, "layout": { "x": 0, "y": 0, "width": 4, "height": 2 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests.table.formulas[0].formula" is equal to "query1"
    And the response "widgets[0].definition.requests.table.formulas[0].dimension" is equal to "x"
    And the response "widgets[0].definition.requests.table.formulas[0].alias" is equal to "my-query1"
    And the response "widgets[0].definition.requests.table.formulas[1].formula" is equal to "query2"
    And the response "widgets[0].definition.requests.table.formulas[1].dimension" is equal to "y"
    And the response "widgets[0].definition.requests.table.formulas[1].alias" is equal to "my-query2"
    And the response "widgets[0].definition.requests.table.queries[0].data_source" is equal to "metrics"
    And the response "widgets[0].definition.requests.table.queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests.table.queries[0].query" is equal to "avg:system.cpu.user{*} by {service}"
    And the response "widgets[0].definition.requests.table.queries[0].aggregator" is equal to "avg"
    And the response "widgets[0].definition.requests.table.queries[1].data_source" is equal to "metrics"
    And the response "widgets[0].definition.requests.table.queries[1].name" is equal to "query2"
    And the response "widgets[0].definition.requests.table.queries[1].query" is equal to "avg:system.mem.used{*} by {service}"
    And the response "widgets[0].definition.requests.table.queries[1].aggregator" is equal to "avg"
    And the response "widgets[0].definition.requests.table.response_format" is equal to "scalar"

  Scenario: Create a new dashboard with funnel widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with funnel widget","widgets": [{"definition": {"type": "funnel","requests": [{"query":{"data_source":"rum","query_string":"","steps":[]},"request_type":"funnel"}]}}]}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new dashboard with list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"issue_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a new dashboard with timeseries widget containing style attributes
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with timeseries widget","widgets": [{"definition": {"type": "timeseries","requests": [{"q": "sum:trace.test.errors{env:prod,service:datadog-api-spec} by {resource_name}.as_count()","on_right_yaxis": false,"style": {"palette": "warm","line_type": "solid","line_width": "normal"},"display_type": "bars"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].on_right_yaxis" is false
    And the response "widgets[0].definition.requests[0].style" is equal to {"palette": "warm","line_type": "solid","line_width": "normal"}
    And the response "widgets[0].definition.requests[0].display_type" is equal to "bars"
    And the response "widgets[0].definition.requests[0].q" is equal to "sum:trace.test.errors{env:prod,service:datadog-api-spec} by {resource_name}.as_count()"

  @generated @skip
  Scenario: Delete a dashboard returns "Dashboards Not Found" response
    Given new "DeleteDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  @generated @skip
  Scenario: Delete a dashboard returns "OK" response
    Given new "DeleteDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete dashboards returns "Bad Request" response
    Given new "DeleteDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete dashboards returns "Dashboards Not Found" response
    Given new "DeleteDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  Scenario: Delete dashboards returns "No Content" response
    Given there is a valid "dashboard" in the system
    And new "DeleteDashboards" request
    And body with value {"data": [{"id": "{{ dashboard.id }}", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip
  Scenario: Get a dashboard returns "Item Not Found" response
    Given new "GetDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Get a dashboard returns "OK" response
    Given new "GetDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  Scenario: Get all dashboards returns "OK" response
    Given new "ListDashboards" request
    And there is a valid "dashboard" in the system
    And request contains "filter[shared]" parameter with value false
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Restore deleted dashboards returns "Bad Request" response
    Given new "RestoreDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Restore deleted dashboards returns "Dashboards Not Found" response
    Given new "RestoreDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  @generated @skip
  Scenario: Restore deleted dashboards returns "No Content" response
    Given new "RestoreDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip
  Scenario: Update a dashboard returns "Bad Request" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [null], "reflow_type": "auto", "restricted_roles": [null], "template_variable_presets": [{"name": null, "template_variables": [{"name": null, "value": null}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "system.cpu.user"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a dashboard returns "Item Not Found" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [null], "reflow_type": "auto", "restricted_roles": [null], "template_variable_presets": [{"name": null, "template_variables": [{"name": null, "value": null}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "system.cpu.user"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Update a dashboard returns "OK" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [null], "reflow_type": "auto", "restricted_roles": [null], "template_variable_presets": [{"name": null, "template_variables": [{"name": null, "value": null}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "system.cpu.user"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 200 OK
