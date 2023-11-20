@endpoint(dashboards) @endpoint(dashboards-v1)
Feature: Dashboards
  Interact with your dashboard lists through the API to make it easier to
  organize, find, and share all of your dashboards with your team and
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Dashboards" API

  @team:DataDog/dashboards-backend
  Scenario: Create a distribution widget using a histogram request containing a formulas and functions APM Stats query
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "description": "", "widgets": [ { "definition": { "title": "APM Stats - Request latency HOP", "title_size": "16", "title_align": "left", "show_legend": false, "type": "distribution", "xaxis": { "max": "auto", "include_zero": true, "scale": "linear", "min": "auto" }, "yaxis": { "max": "auto", "include_zero": true, "scale": "linear", "min": "auto" }, "requests": [ { "query": { "primary_tag_value": "*", "stat": "latency_distribution", "data_source": "apm_resource_stats", "name": "query1", "service": "azure-bill-import", "group_by": [ "resource_name" ], "env": "staging", "primary_tag_name": "datacenter", "operation_name": "universal.http.client" }, "request_type": "histogram", "style": { "palette": "dog_classic" } } ] }, "layout": { "x": 8, "y": 0, "width": 4, "height": 2 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].request_type" is equal to "histogram"
    And the response "widgets[0].definition.requests[0].style" is equal to { "palette": "dog_classic" }
    And the response "widgets[0].definition.requests[0].query.primary_tag_value" is equal to "*"
    And the response "widgets[0].definition.requests[0].query.stat" is equal to "latency_distribution"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "apm_resource_stats"
    And the response "widgets[0].definition.requests[0].query.name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].query.service" is equal to "azure-bill-import"
    And the response "widgets[0].definition.requests[0].query.group_by" is equal to ["resource_name"]
    And the response "widgets[0].definition.requests[0].query.env" is equal to "staging"
    And the response "widgets[0].definition.requests[0].query.primary_tag_name" is equal to "datacenter"
    And the response "widgets[0].definition.requests[0].query.operation_name" is equal to "universal.http.client"

  @team:DataDog/dashboards-backend
  Scenario: Create a distribution widget using a histogram request containing a formulas and functions events query
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "description": "{{ unique }}", "widgets": [ { "definition": { "title": "Events Platform - Request latency HOP", "title_size": "16", "title_align": "left", "show_legend": false, "type": "distribution", "xaxis": { "max": "auto", "include_zero": true, "scale": "linear", "min": "auto" }, "yaxis": { "max": "auto", "include_zero": true, "scale": "linear", "min": "auto" }, "requests": [ { "query": { "search": { "query": "" }, "data_source": "events", "compute": { "metric": "@duration", "aggregation": "min" }, "name": "query1", "indexes": [ "*" ], "group_by": [] }, "request_type": "histogram" } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 2 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].request_type" is equal to "histogram"
    And the response "widgets[0].definition.requests[0].query.search.query" is equal to ""
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "events"
    And the response "widgets[0].definition.requests[0].query.compute.metric" is equal to "@duration"
    And the response "widgets[0].definition.requests[0].query.compute.aggregation" is equal to "min"
    And the response "widgets[0].definition.requests[0].query.name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].query.indexes" is equal to ["*"]
    And the response "widgets[0].definition.requests[0].query.group_by" is equal to []

  @team:DataDog/dashboards-backend
  Scenario: Create a distribution widget using a histogram request containing a formulas and functions metrics query
    Given new "CreateDashboard" request
    And body with value {"title":"{{ unique }}","widgets":[{"definition":{"title":"Metrics HOP","title_size":"16","title_align":"left","show_legend":false,"type":"distribution","custom_links":[{"label":"Example","link":"https://example.org/"}],"xaxis":{"max":"auto","include_zero":true,"scale":"linear","min":"auto"},"yaxis":{"max":"auto","include_zero":true,"scale":"linear","min":"auto"},"requests":[{"query":{"query":"histogram:trace.Load{*}","data_source":"metrics","name":"query1"},"request_type":"histogram","style":{"palette":"dog_classic"}}]},"layout":{"x":0,"y":0,"width":4,"height":2}}],"layout_type":"ordered"}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].request_type" is equal to "histogram"
    And the response "widgets[0].definition.requests[0].style" is equal to { "palette": "dog_classic" }
    And the response "widgets[0].definition.requests[0].query.query" is equal to "histogram:trace.Load{*}"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "metrics"
    And the response "widgets[0].definition.requests[0].query.name" is equal to "query1"
    And the response "widgets[0].definition.custom_links" has item with field "label" with value "Example"

  @team:DataDog/dashboards-backend
  Scenario: Create a geomap widget using an event_list request
    Given new "CreateDashboard" request
    And body with value {"title": "{{ unique }}","description": "{{ unique }}","widgets":[{"definition":{"title":"","title_size":"16","title_align":"left","type":"geomap","requests":[{"response_format":"event_list","query":{"data_source":"logs_stream","query_string":"","indexes":[]},"columns":[{"field":"@network.client.geoip.location.latitude","width":"auto"},{"field":"@network.client.geoip.location.longitude","width":"auto"},{"field":"@network.client.geoip.country.iso_code","width":"auto"},{"field":"@network.client.geoip.subdivision.name","width":"auto"},{"field":"classic","width":"auto"},{"field":"","width":"auto"}]}],"style":{"palette":"hostmap_blues","palette_flip":false},"view":{"focus":"WORLD"}},"layout":{"x":0,"y":0,"width":12,"height":6}}],"template_variables":[],"layout_type":"ordered","notify_list":[],"reflow_type":"fixed","tags":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "event_list"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "logs_stream"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard returns "Bad Request" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "tags": [], "template_variable_presets": [{"template_variables": [{"values": []}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "defaults": ["my-host-1", "my-host-2"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard returns "OK" response
    Given new "CreateDashboard" request
    And body from file "dashboard_payload.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }} with Profile Metrics Query"
    And the response "widgets[0].definition.requests[0].profile_metrics_query.search.query" is equal to "runtime:jvm"
    And the response "widgets[0].definition.requests[0].profile_metrics_query.compute.facet" is equal to "@prof_core_cpu_cores"
    And the response "widgets[0].definition.requests[0].profile_metrics_query.compute.aggregation" is equal to "sum"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a change widget using formulas and functions slo query
    Given there is a valid "slo" in the system
    And new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": {"title": "", "title_size": "16", "title_align": "left", "time": {}, "type": "change", "requests": [ {"formulas": [ { "formula": "hour_before(query1)" }, { "formula": "query1" } ], "queries": [ {"name": "query1", "data_source": "slo", "slo_id": "{{ slo.data[0].id }}", "measure": "slo_status", "group_mode": "overall", "slo_query_type": "metric", "additional_query_filters": "*" } ], "response_format": "scalar", "order_by": "change", "change_type": "absolute", "increase_good": true, "order_dir": "asc" } ] }, "layout": { "x":0, "y": 0, "width": 4, "height": 2 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].increase_good" is equal to true
    And the response "widgets[0].definition.requests[0].order_by" is equal to "change"
    And the response "widgets[0].definition.requests[0].change_type" is equal to "absolute"
    And the response "widgets[0].definition.requests[0].order_dir" is equal to "asc"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "slo"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].group_mode" is equal to "overall"
    And the response "widgets[0].definition.requests[0].queries[0].measure" is equal to "slo_status"
    And the response "widgets[0].definition.requests[0].queries[0].slo_query_type" is equal to "metric"
    And the response "widgets[0].definition.requests[0].queries[0].slo_id" has the same value as "slo.data[0].id"
    And the response "widgets[0].definition.requests[0].queries[0].additional_query_filters" is equal to "*"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "hour_before(query1)"
    And the response "widgets[0].definition.requests[0].formulas[1].formula" is equal to "query1"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a formulas and functions change widget
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": { "title": "", "title_size": "16", "title_align": "left", "time": {}, "type": "change", "requests": [ { "formulas": [ { "formula": "hour_before(query1)" }, { "formula": "query1" } ], "queries": [ { "data_source": "logs", "name": "query1", "search": { "query": "" }, "indexes": [ "*" ], "compute": { "aggregation": "count" }, "group_by": [] } ], "response_format": "scalar", "compare_to": "hour_before", "increase_good": true, "order_by": "change", "change_type": "absolute", "order_dir": "desc" } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].compare_to" is equal to "hour_before"
    And the response "widgets[0].definition.requests[0].increase_good" is equal to true
    And the response "widgets[0].definition.requests[0].order_by" is equal to "change"
    And the response "widgets[0].definition.requests[0].change_type" is equal to "absolute"
    And the response "widgets[0].definition.requests[0].order_dir" is equal to "desc"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "logs"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].compute.aggregation" is equal to "count"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "hour_before(query1)"
    And the response "widgets[0].definition.requests[0].formulas[1].formula" is equal to "query1"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a formulas and functions treemap widget
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": { "title": "", "type": "treemap", "requests": [ { "formulas": [ { "formula": "hour_before(query1)" }, { "formula": "query1" } ], "queries": [ { "data_source": "logs", "name": "query1", "search": { "query": "" }, "indexes": [ "*" ], "compute": { "aggregation": "count" }, "group_by": [] } ], "response_format": "scalar" } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "logs"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].compute.aggregation" is equal to "count"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "hour_before(query1)"
    And the response "widgets[0].definition.requests[0].formulas[1].formula" is equal to "query1"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a query value widget using the percentile aggregator
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with QVW Percentile Aggregator", "widgets": [{"definition":{"title_size":"16","title":"","title_align":"left","precision":2,"time":{},"autoscale":true,"requests":[{"formulas":[{"formula":"query1"}],"response_format":"scalar","queries":[{"query":"p90:dist.dd.dogweb.latency{*}","data_source":"metrics","name":"query1","aggregator":"percentile"}]}],"type":"query_value"},"layout":{"y":0,"x":0,"height":2,"width":2}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }} with QVW Percentile Aggregator"
    And the response "widgets[0].definition.title_size" is equal to "16"
    And the response "widgets[0].definition.title_align" is equal to "left"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "query1"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a query value widget using timeseries background
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with QVW Timeseries Background", "widgets": [{"definition":{"title_size":"16","title":"","title_align":"left","precision":2,"time":{},"autoscale":true,"requests":[{"formulas":[{"formula":"query1"}],"response_format":"scalar","queries":[{"query":"sum:my.cool.count.metric{*}","data_source":"metrics","name":"query1","aggregator":"percentile"}]}],"type":"query_value","timeseries_background":{"type":"area","yaxis":{"include_zero":true}}},"layout":{"y":0,"x":0,"height":2,"width":2}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }} with QVW Timeseries Background"
    And the response "widgets[0].definition.title_size" is equal to "16"
    And the response "widgets[0].definition.title_align" is equal to "left"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "query1"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].queries[0].query" is equal to "sum:my.cool.count.metric{*}"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a timeseries widget and an overlay request
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }}", "widgets": [{"definition": {"type": "timeseries", "requests": [{"on_right_yaxis": false, "queries": [{"data_source": "metrics", "name": "mymetric", "query": "avg:system.cpu.user{*}"}], "response_format": "timeseries", "display_type": "line"}, {"response_format": "timeseries", "queries": [{"data_source": "metrics", "name": "mymetricoverlay", "query": "avg:system.cpu.user{*}"}], "style": {"palette": "purple", "line_type": "solid", "line_width": "normal"}, "display_type": "overlay"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "timeseries"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "metrics"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "mymetric"
    And the response "widgets[0].definition.requests[0].queries[0].query" is equal to "avg:system.cpu.user{*}"
    And the response "widgets[0].definition.requests[1].display_type" is equal to "overlay"
    And the response "widgets[0].definition.requests[1].queries[0].query" is equal to "avg:system.cpu.user{*}"
    And the response "widgets[0].definition.requests[1].queries[0].name" is equal to "mymetricoverlay"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with a timeseries widget using formulas and functions cloud cost query
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": { "title": "Example Cloud Cost Query", "title_size": "16", "title_align": "left", "type": "timeseries",  "requests": [ { "formulas": [ { "formula": "query1" } ], "queries": [ { "data_source": "cloud_cost", "name": "query1", "query": "sum:aws.cost.amortized{*} by {aws_product}.rollup(sum, monthly)" } ], "response_format": "timeseries", "style": { "palette": "dog_classic", "line_type": "solid", "line_width": "normal" }, "display_type": "bars" } ], "time": { "live_span": "week_to_date" } } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "timeseries"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "cloud_cost"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].query" is equal to "sum:aws.cost.amortized{*} by {aws_product}.rollup(sum, monthly)"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "query1"
    And the response "widgets[0].definition.time.live_span" is equal to "week_to_date"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with alert_graph widget
    Given there is a valid "monitor" in the system
    And new "CreateDashboard" request
    And body from file "dashboards_json_payload/alert_graph_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "alert_graph"
    And the response "widgets[0].definition.viz_type" is equal to "timeseries"
    And the response "widgets[0].definition.alert_id" is equal to "{{ monitor.id }}"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with alert_value widget
    Given there is a valid "monitor" in the system
    And new "CreateDashboard" request
    And body from file "dashboards_json_payload/alert_value_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "alert_value"
    And the response "widgets[0].definition.alert_id" is equal to "{{ monitor.id }}"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with an audit logs query
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with Audit Logs Query", "widgets": [{"definition": {"type": "timeseries","requests": [{"response_format": "timeseries","queries": [{"search": {"query": ""},"data_source": "audit","compute": {"aggregation": "count"},"name": "query1","indexes": ["*"],"group_by": []}]}]},"layout": {"x": 2,"y": 0,"width": 4,"height": 2}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }} with Audit Logs Query"
    And the response "widgets[0].definition.type" is equal to "timeseries"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "timeseries"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "audit"

  @team:DataDog/dashboards-backend
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

  @team:DataDog/dashboards-backend
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

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with apm_issue_stream list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"apm_issue_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }} with list_stream widget"
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].columns[0].width" is equal to "auto"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "apm_issue_stream"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with check_status widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/check_status_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "check_status"
    And the response "widgets[0].definition.check" is equal to "datadog.agent.up"
    And the response "widgets[0].definition.grouping" is equal to "check"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with ci_test_stream list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"ci_test_stream","query_string":"test_level:suite"},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "ci_test_stream"
    And the response "widgets[0].definition.requests[0].query.query_string" is equal to "test_level:suite"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with distribution widget and apm stats data
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [{"definition": { "title": "", "title_size": "16", "title_align": "left", "type": "distribution", "requests": [{ "apm_stats_query": { "env": "prod", "service": "cassandra", "name": "cassandra.query", "primary_tag": "datacenter:dc1", "row_type": "service" }}] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].apm_stats_query.primary_tag" is equal to "datacenter:dc1"
    And the response "widgets[0].definition.requests[0].apm_stats_query.row_type" is equal to "service"
    And the response "widgets[0].definition.requests[0].apm_stats_query.env" is equal to "prod"
    And the response "widgets[0].definition.requests[0].apm_stats_query.service" is equal to "cassandra"
    And the response "widgets[0].definition.requests[0].apm_stats_query.name" is equal to "cassandra.query"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with event_stream list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered","title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns": [{"width": "auto","field": "timestamp"}],"query": {"data_source": "event_stream","query_string": "","event_size": "l"},"response_format": "event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "event_list"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "event_stream"
    And the response "widgets[0].definition.requests[0].query.event_size" is equal to "l"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with event_stream widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/event_stream_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "event_stream"
    And the response "widgets[0].definition.query" is equal to "example-query"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with event_timeline widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/event_timeline_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "event_timeline"
    And the response "widgets[0].definition.query" is equal to "status:error priority:all"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with formula and function heatmap widget
    Given new "CreateDashboard" request
    And body with value {"title": "{{ unique }}", "widgets": [{"layout": {"x": 0, "y": 0, "width": 47, "height": 15}, "definition": {"title": "", "title_size": "16", "title_align": "left", "time": {}, "type": "heatmap", "requests": [{"response_format": "timeseries", "queries": [{"data_source": "metrics", "name": "query1", "query": "avg:system.cpu.user{*}"}], "formulas": [{"formula": "query1"}], "style": {"palette": "dog_classic"}}]}}], "template_variables": [], "layout_type": "free", "is_read_only": false, "notify_list": []}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "heatmap"
    And the response "widgets[0].definition.requests[0].queries[0].query" is equal to "avg:system.cpu.user{*}"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "metrics"
    And the response "widgets[0].definition.requests[0].style.palette" is equal to "dog_classic"

  @team:DataDog/dashboards-backend
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

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with free_text widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/free_text_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "free_text"
    And the response "widgets[0].definition.text" is equal to "Example free text"
    And the response "widgets[0].definition.color" is equal to "#4d4d4d"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with funnel widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with funnel widget","widgets": [{"definition": {"type": "funnel","requests": [{"query":{"data_source":"rum","query_string":"","steps":[]},"request_type":"funnel"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }} with funnel widget"
    And the response "widgets[0].definition.type" is equal to "funnel"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "rum"
    And the response "widgets[0].definition.requests[0].request_type" is equal to "funnel"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with geomap widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/geomap_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "geomap"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with heatmap widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/heatmap_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "heatmap"
    And the response "widgets[0].definition.requests[0].q" is equal to "avg:system.cpu.user{*} by {service}"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with hostmap widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/hostmap_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "hostmap"
    And the response "widgets[0].definition.requests.fill.q" is equal to "avg:system.cpu.user{*} by {host}"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with iframe widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/iframe_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "iframe"
    And the response "widgets[0].definition.url" is equal to "https://docs.datadoghq.com/api/latest/"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with image widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/image_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "image"
    And the response "widgets[0].definition.url" is equal to "https://example.com/image.png"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with invalid team tags returns "Bad Request" response
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": { "title": "", "title_size": "16", "title_align": "left", "time": {}, "type": "change", "requests": [ { "formulas": [ { "formula": "hour_before(query1)" }, { "formula": "query1" } ], "queries": [ { "data_source": "logs", "name": "query1", "search": { "query": "" }, "indexes": [ "*" ], "compute": { "aggregation": "count" }, "group_by": [] } ], "response_format": "scalar", "compare_to": "hour_before", "increase_good": true, "order_by": "change", "change_type": "absolute", "order_dir": "desc" } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "tags": ["tm:foobar"], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"apm_issue_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "apm_issue_stream"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with list_stream widget with a valid sort parameter ASC
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered","title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns": [{"width": "auto","field": "timestamp"}],"query": {"data_source": "event_stream","query_string": "","event_size": "l", "sort": {"column": "timestamp", "order": "asc"}},"response_format": "event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "event_list"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "event_stream"
    And the response "widgets[0].definition.requests[0].query.event_size" is equal to "l"
    And the response "widgets[0].definition.requests[0].query.sort.column" is equal to "timestamp"
    And the response "widgets[0].definition.requests[0].query.sort.order" is equal to "asc"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with list_stream widget with a valid sort parameter DESC
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered","title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns": [{"width": "auto","field": "timestamp"}],"query": {"data_source": "event_stream","query_string": "","event_size": "l", "sort": {"column": "timestamp", "order": "desc"}},"response_format": "event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "event_list"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "event_stream"
    And the response "widgets[0].definition.requests[0].query.event_size" is equal to "l"
    And the response "widgets[0].definition.requests[0].query.sort.column" is equal to "timestamp"
    And the response "widgets[0].definition.requests[0].query.sort.order" is equal to "desc"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with log_stream widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/log_stream_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "log_stream"
    And the response "widgets[0].definition.query" is equal to ""
    And the response "widgets[0].definition.indexes[0]" is equal to "main"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with logs query table widget and storage parameter
    Given new "CreateDashboard" request
    And body with value {"layout_type":"ordered","title":"{{ unique }} with query table widget and storage parameter","widgets":[{"definition":{"type":"query_table","requests":[{"queries":[{"data_source":"logs","name":"query1","search":{"query":""},"indexes":["*"],"compute":{"aggregation":"count"},"group_by":[],"storage":"online_archives"}],"formulas":[{"conditional_formats":[],"cell_display_mode":"bar","formula":"query1","limit":{"count":50,"order":"desc"}}],"response_format":"scalar"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "query_table"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "logs"
    And the response "widgets[0].definition.requests[0].queries[0].storage" is equal to "online_archives"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with logs_pattern_stream list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"logs_pattern_stream","query_string":"","group_by":[{"facet":"service"}]},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "logs_pattern_stream"
    And the response "widgets[0].definition.requests[0].query.group_by[0].facet" is equal to "service"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with logs_stream list_stream widget and storage parameter
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"logs_stream","query_string":"", "storage": "hot"},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "logs_stream"
    And the response "widgets[0].definition.requests[0].query.storage" is equal to "hot"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with logs_transaction_stream list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"logs_transaction_stream","query_string":"","group_by":[{"facet":"service"}],"compute":[{"facet":"service","aggregation":"count"}]},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "logs_transaction_stream"
    And the response "widgets[0].definition.requests[0].query.group_by[0].facet" is equal to "service"
    And the response "widgets[0].definition.requests[0].query.compute[0].facet" is equal to "service"
    And the response "widgets[0].definition.requests[0].query.compute[0].aggregation" is equal to "count"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with manage_status widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/manage_status_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "manage_status"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with manage_status widget and show_priority parameter
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/manage_status_widget_priority_sort.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "manage_status"
    And the response "widgets[0].definition.show_priority" is false
    And the response "widgets[0].definition.sort" is equal to "priority,asc"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with note widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/note_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "note"
    And the response "widgets[0].definition.content" is equal to "# Example Note"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with powerpack widget
    Given new "CreateDashboard" request
    And there is a valid "powerpack" in the system
    And body from file "dashboards_json_payload/powerpack_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "powerpack"
    And the response "widgets[0].definition.powerpack_id" has the same value as "powerpack.data.id"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with query_table widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/query_table_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "query_table"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with query_value widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/query_value_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "query_value"
    And the response "widgets[0].definition.requests[0].queries[0].query" is equal to "avg:system.cpu.user{*}"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with rum_issue_stream list_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"rum_issue_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].response_format" is equal to "event_list"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with run-workflow widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/run_workflow_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "run_workflow"
    And the response "widgets[0].definition.workflow_id" is equal to "2e055f16-8b6a-4cdd-b452-17a34c44b160"
    And the response "widgets[0].definition.inputs[0]" is equal to {"name": "environment", "value": "$env.value"}

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with scatterplot widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/scatterplot_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "scatterplot"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with servicemap widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/servicemap_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "servicemap"
    And the response "widgets[0].definition.filters" is equal to ["env:none","environment:*"]

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with slo list widget
    Given there is a valid "slo" in the system
    And new "CreateDashboard" request
    And body from file "dashboards_json_payload/slo_list_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "slo_list"
    And the response "widgets[0].definition.requests[0].query.query_string" is equal to "env:prod AND service:my-app"
    And the response "widgets[0].definition.requests[0].query.limit" is equal to 75

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with slo list widget with sort
    Given there is a valid "slo" in the system
    And new "CreateDashboard" request
    And body from file "dashboards_json_payload/slo_list_widget_with_sort.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "slo_list"
    And the response "widgets[0].definition.requests[0].query.query_string" is equal to "env:prod AND service:my-app"
    And the response "widgets[0].definition.requests[0].query.limit" is equal to 75
    And the response "widgets[0].definition.requests[0].query.sort[0].column" is equal to "status.sli"
    And the response "widgets[0].definition.requests[0].query.sort[0].order" is equal to "asc"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with slo widget
    Given there is a valid "slo" in the system
    And new "CreateDashboard" request
    And body from file "dashboards_json_payload/slo_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "slo"
    And the response "widgets[0].definition.slo_id" is equal to "{{ slo.data[0].id }}"
    And the response "widgets[0].definition.additional_query_filters" is equal to "!host:excluded_host"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with split graph widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/split_graph_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "split_group"
    And the response "widgets[0].definition.source_widget_definition.type" is equal to "timeseries"
    And the response "widgets[0].definition.source_widget_definition.requests[0].response_format" is equal to "timeseries"
    And the response "widgets[0].definition.source_widget_definition.requests[0].queries[0].data_source" is equal to "metrics"
    And the response "widgets[0].definition.source_widget_definition.requests[0].queries[0].query" is equal to "avg:system.cpu.user{*}"
    And the response "widgets[0].definition.source_widget_definition.requests[0].style.palette" is equal to "dog_classic"
    And the response "widgets[0].definition.split_config.split_dimensions[0].one_graph_per" is equal to "service"
    And the response "widgets[0].definition.split_config.limit" is equal to 24
    And the response "widgets[0].definition.split_config.sort.compute.aggregation" is equal to "sum"
    And the response "widgets[0].definition.split_config.sort.compute.metric" is equal to "system.cpu.user"
    And the response "widgets[0].definition.split_config.sort.order" is equal to "desc"
    And the response "widgets[0].definition.split_config.static_splits[0][0].tag_key" is equal to "service"
    And the response "widgets[0].definition.split_config.static_splits[0][0].tag_values[0]" is equal to "cassandra"
    And the response "widgets[0].definition.split_config.static_splits[0][1].tag_key" is equal to "datacenter"
    And the response "widgets[0].definition.split_config.static_splits[0][1].tag_values" has length 0
    And the response "widgets[0].definition.split_config.static_splits[1][0].tag_key" is equal to "demo"
    And the response "widgets[0].definition.split_config.static_splits[1][0].tag_values[0]" is equal to "env"
    And the response "widgets[0].definition.size" is equal to "md"
    And the response "widgets[0].definition.has_uniform_y_axes" is equal to true

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with sunburst widget and metrics data
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": { "title": "", "title_size": "16", "title_align": "left", "type": "sunburst", "requests": [ { "response_format": "scalar", "formulas": [ { "formula": "query1" } ], "queries": [ { "query": "sum:system.mem.used{*} by {service}", "data_source": "metrics", "name": "query1", "aggregator": "sum" } ], "style": { "palette": "dog_classic" } } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].response_format" is equal to "scalar"
    And the response "widgets[0].definition.requests[0].queries[0].query" is equal to "sum:system.mem.used{*} by {service}"
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "metrics"
    And the response "widgets[0].definition.requests[0].queries[0].name" is equal to "query1"
    And the response "widgets[0].definition.requests[0].queries[0].aggregator" is equal to "sum"
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "query1"
    And the response "widgets[0].definition.requests[0].style.palette" is equal to "dog_classic"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with team tags returns "OK" response
    Given new "CreateDashboard" request
    And body with value { "title": "{{ unique }}", "widgets": [ { "definition": { "title": "", "title_size": "16", "title_align": "left", "time": {}, "type": "change", "requests": [ { "formulas": [ { "formula": "hour_before(query1)" }, { "formula": "query1" } ], "queries": [ { "data_source": "logs", "name": "query1", "search": { "query": "" }, "indexes": [ "*" ], "compute": { "aggregation": "count" }, "group_by": [] } ], "response_format": "scalar", "compare_to": "hour_before", "increase_good": true, "order_by": "change", "change_type": "absolute", "order_dir": "desc" } ] }, "layout": { "x": 0, "y": 0, "width": 4, "height": 4 } } ], "tags": ["team:foobar"], "layout_type": "ordered" }
    When the request is sent
    Then the response status is 200 OK
    And the response "title" is equal to "{{ unique }}"
    And the response "tags" array contains value "team:foobar"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with template variable defaults and default returns "Bad Request" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "defaults": ["my-host"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with template variable defaults returns "OK" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "defaults": ["my-host"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "template_variables[0].name" is equal to "host1"
    And the response "template_variables[0].available_values[0]" is equal to "my-host"
    And the response "template_variables[0].defaults[0]" is equal to "my-host"

  @skip-validation @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with template variable defaults whose value has no length returns "Bad Request" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "defaults": [""], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with template variable presets using values and value returns "Bad Request" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "template_variable_presets": [{"name": "my saved view", "template_variables": [{"name": "datacenter", "value": "*", "values": [ "*" ]}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "defaults": ["my-host"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with template variable presets using values returns "OK" response
    Given new "CreateDashboard" request
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "template_variable_presets": [{"name": "my saved view", "template_variables": [{"name": "datacenter", "values": ["*", "my-host"]}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "defaults": ["my-host"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "template_variable_presets[0].name" is equal to "my saved view"
    And the response "template_variable_presets[0].template_variables[0].name" is equal to "datacenter"
    And the response "template_variable_presets[0].template_variables[0].values[0]" is equal to "*"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with timeseries widget and formula style attributes
    Given new "CreateDashboard" request
    And body with value {"title": "{{ unique }} with formula style","widgets": [{"definition": {"title": "styled timeseries","show_legend": true,"legend_layout": "auto","legend_columns": ["avg","min","max","value","sum"],"time": {},"type": "timeseries","requests": [{"formulas": [{"formula": "query1","style": {"palette_index": 4,"palette": "classic"}}],"queries": [{"query": "avg:system.cpu.user{*}","data_source": "metrics","name": "query1"}],"response_format": "timeseries","style": {"palette": "dog_classic","line_type": "solid","line_width": "normal"},"display_type": "line"}]}}],"layout_type": "ordered","reflow_type": "auto"}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].formulas[0].formula" is equal to "query1"
    And the response "widgets[0].definition.requests[0].formulas[0].style.palette" is equal to "classic"
    And the response "widgets[0].definition.requests[0].formulas[0].style.palette_index" is equal to 4

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with timeseries widget containing style attributes
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with timeseries widget","widgets": [{"definition": {"type": "timeseries","requests": [{"q": "sum:trace.test.errors{env:prod,service:datadog-api-spec} by {resource_name}.as_count()","on_right_yaxis": false,"style": {"palette": "warm","line_type": "solid","line_width": "normal"},"display_type": "bars"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].on_right_yaxis" is false
    And the response "widgets[0].definition.requests[0].style" is equal to {"palette": "warm","line_type": "solid","line_width": "normal"}
    And the response "widgets[0].definition.requests[0].display_type" is equal to "bars"
    And the response "widgets[0].definition.requests[0].q" is equal to "sum:trace.test.errors{env:prod,service:datadog-api-spec} by {resource_name}.as_count()"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with toplist widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/toplist_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "toplist"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with topology_map widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/topology_map_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "topology_map"
    And the response "widgets[0].definition.requests[0].request_type" is equal to "topology"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "service_map"
    And the response "widgets[0].definition.requests[0].query.service" is equal to ""
    And the response "widgets[0].definition.requests[0].query.filters" is equal to ["env:none","environment:*"]

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with trace_service widget
    Given new "CreateDashboard" request
    And body from file "dashboards_json_payload/trace_service_widget.json"
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "trace_service"
    And the response "widgets[0].definition.env" is equal to "none"

  @team:DataDog/dashboards-backend
  Scenario: Create a new dashboard with trace_stream widget
    Given new "CreateDashboard" request
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"},{"width":"auto","field":"service"}],"query":{"data_source":"trace_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.type" is equal to "list_stream"
    And the response "widgets[0].definition.requests[0].query.data_source" is equal to "trace_stream"

  @team:DataDog/dashboards-backend
  Scenario: Create a new timeseries widget with ci_pipelines data source
    Given new "CreateDashboard" request
    And body with value {"title":"{{ unique }} with ci_pipelines datasource","widgets":[{"definition":{"title":"","show_legend":true,"legend_layout":"auto","legend_columns":["avg","min","max","value","sum"],"time":{},"type":"timeseries","requests":[{"formulas":[{"formula":"query1"}],"queries":[{"data_source":"ci_pipelines","name":"query1","search":{"query":"ci_level:job"},"indexes":["*"],"compute":{"aggregation":"count", "metric": "@ci.queue_time"},"group_by":[]}],"response_format":"timeseries","style":{"palette":"dog_classic","line_type":"solid","line_width":"normal"},"display_type":"line"}]}}],"layout_type":"ordered","reflow_type":"auto"}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "ci_pipelines"
    And the response "widgets[0].definition.requests[0].queries[0].search.query" is equal to "ci_level:job"

  @team:DataDog/dashboards-backend
  Scenario: Create a new timeseries widget with ci_tests data source
    Given new "CreateDashboard" request
    And body with value {"title":"{{ unique }} with ci_tests datasource","widgets":[{"definition":{"title":"","show_legend":true,"legend_layout":"auto","legend_columns":["avg","min","max","value","sum"],"time":{},"type":"timeseries","requests":[{"formulas":[{"formula":"query1"}],"queries":[{"data_source":"ci_tests","name":"query1","search":{"query":"test_level:test"},"indexes":["*"],"compute":{"aggregation":"count"},"group_by":[]}],"response_format":"timeseries","style":{"palette":"dog_classic","line_type":"solid","line_width":"normal"},"display_type":"line"}]}}],"layout_type":"ordered","reflow_type":"auto"}
    When the request is sent
    Then the response status is 200 OK
    And the response "widgets[0].definition.requests[0].queries[0].data_source" is equal to "ci_tests"
    And the response "widgets[0].definition.requests[0].queries[0].search.query" is equal to "test_level:test"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Create a shared dashboard returns "Bad Request" response
    Given new "CreatePublicDashboard" request
    And body with value {"dashboard_id": "123-abc-456", "dashboard_type": "custom_timeboard", "global_time": {"live_span": "1h"}, "global_time_selectable_enabled": null, "selectable_template_vars": [{"default_value": "*", "name": "exampleVar", "prefix": "test", "visible_tags": ["selectableValue1", "selectableValue2"]}], "share_list": ["test@datadoghq.com", "test2@email.com"], "share_type": "open"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards-backend
  Scenario: Create a shared dashboard returns "Dashboard Not Found" response
    Given new "CreatePublicDashboard" request
    And body with value {"dashboard_id": "abc-123-def", "dashboard_type": "custom_timeboard", "share_type": "open", "global_time": {"live_span": "1h"}}
    When the request is sent
    Then the response status is 404 Dashboard Not Found

  @team:DataDog/dashboards-backend
  Scenario: Create a shared dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And new "CreatePublicDashboard" request
    And body with value {"dashboard_id": "{{dashboard.id}}", "dashboard_type": "custom_timeboard", "share_type": "open", "global_time": {"live_span": "1h"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboard_id" has the same value as "dashboard.id"
    And the response "dashboard_type" is equal to "custom_timeboard"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Delete a dashboard returns "Dashboards Not Found" response
    Given new "DeleteDashboard" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  @team:DataDog/dashboards-backend
  Scenario: Delete a dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And new "DeleteDashboard" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "deleted_dashboard_id" is equal to "{{ dashboard.id }}"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Delete dashboards returns "Bad Request" response
    Given new "DeleteDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Delete dashboards returns "Dashboards Not Found" response
    Given new "DeleteDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  @team:DataDog/dashboards-backend
  Scenario: Delete dashboards returns "No Content" response
    Given there is a valid "dashboard" in the system
    And new "DeleteDashboards" request
    And body with value {"data": [{"id": "{{ dashboard.id }}", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Get a dashboard returns "Item Not Found" response
    Given new "GetDashboard" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @team:DataDog/dashboards-backend
  Scenario: Get a dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And new "GetDashboard" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "description" is equal to null

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get a dashboard returns 'author_name'
    Given there is a valid "dashboard" in the system
    And new "GetDashboard" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "author_name" is equal to "Frog Account"

  @team:DataDog/dashboards-backend
  Scenario: Get a shared dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "shared_dashboard" in the system
    And new "GetPublicDashboard" request
    And request contains "token" parameter from "shared_dashboard.token"
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboard_id" has the same value as "dashboard.id"
    And the response "token" has the same value as "shared_dashboard.token"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Get a shared dashboard returns "Shared Dashboard Not Found" response
    Given new "GetPublicDashboard" request
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Shared Dashboard Not Found

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get all dashboards returns "OK" response
    Given new "ListDashboards" request
    And there is a valid "dashboard" in the system
    And request contains "filter[shared]" parameter with value false
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboards[0].title" has the same value as "dashboard.title"
    And the response "dashboards[0].id" has the same value as "dashboard.id"

  @replay-only @skip-validation @team:DataDog/dashboards-backend @with-pagination
  Scenario: Get all dashboards returns "OK" response with pagination
    Given new "ListDashboards" request
    And request contains "count" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Get all invitations for a shared dashboard returns "Not Found" response
    Given new "GetPublicDashboardInvitations" request
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards-backend
  Scenario: Get all invitations for a shared dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "shared_dashboard" in the system
    And new "GetPublicDashboardInvitations" request
    And request contains "token" parameter from "shared_dashboard.token"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get deleted dashboards returns "OK" response
    Given new "ListDashboards" request
    And there is a valid "dashboard" in the system
    And the "dashboard" was deleted
    And request contains "filter[deleted]" parameter with value true
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboards[0].title" has the same value as "dashboard.title"
    And the response "dashboards[0].id" has the same value as "dashboard.id"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Restore deleted dashboards returns "Bad Request" response
    Given new "RestoreDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Restore deleted dashboards returns "Dashboards Not Found" response
    Given new "RestoreDashboards" request
    And body with value {"data": [{"id": "123-abc-456", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  @team:DataDog/dashboards-backend
  Scenario: Restore deleted dashboards returns "No Content" response
    Given there is a valid "dashboard" in the system
    And the "dashboard" was deleted
    And new "RestoreDashboards" request
    And body with value {"data": [{"id": "{{ dashboard.id }}", "type": "dashboard"}]}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Revoke a shared dashboard URL returns "OK" response
    Given new "DeletePublicDashboard" request
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Revoke a shared dashboard URL returns "Shared Dashboard Not Found" response
    Given new "DeletePublicDashboard" request
    And request contains "token" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Shared Dashboard Not Found

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Revoke shared dashboard invitations returns "Not Found" response
    Given new "DeletePublicDashboardInvitation" request
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"email": "test@datadoghq.com"}, "type": "public_dashboard_invitation"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Revoke shared dashboard invitations returns "OK" response
    Given new "DeletePublicDashboardInvitation" request
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"email": "test@datadoghq.com"}, "type": "public_dashboard_invitation"}]}
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Send shared dashboard invitation email returns "Bad Request" response
    Given new "SendPublicDashboardInvitation" request
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"email": "test@datadoghq.com"}, "type": "public_dashboard_invitation"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Send shared dashboard invitation email returns "Not Found" response
    Given new "SendPublicDashboardInvitation" request
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"email": "test@datadoghq.com"}, "type": "public_dashboard_invitation"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards-backend
  Scenario: Send shared dashboard invitation email returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "shared_dashboard" in the system
    And new "SendPublicDashboardInvitation" request
    And request contains "token" parameter from "shared_dashboard.token"
    And body with value {"data": {"attributes": {"email": "{{unique_lower_alnum}}@datadoghq.com"}, "type": "public_dashboard_invitation"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.email" has the same value as "shared_dashboard.share_list[0]"
    And the response "data.attributes.share_token" has the same value as "shared_dashboard.token"

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Update a dashboard returns "Bad Request" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "tags": [], "template_variable_presets": [{"template_variables": [{"values": []}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "defaults": ["my-host-1", "my-host-2"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Update a dashboard returns "Item Not Found" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    And body with value {"description": null, "is_read_only": false, "layout_type": "ordered", "notify_list": [], "reflow_type": "auto", "restricted_roles": [], "tags": [], "template_variable_presets": [{"template_variables": [{"values": []}]}], "template_variables": [{"available_values": ["my-host", "host1", "host2"], "default": "my-host", "defaults": ["my-host-1", "my-host-2"], "name": "host1", "prefix": "host"}], "title": "", "widgets": [{"definition": {"requests": {"fill": {"q": "avg:system.cpu.user{*}"}}, "type": "hostmap"}}]}
    When the request is sent
    Then the response status is 404 Item Not Found

  @team:DataDog/dashboards-backend
  Scenario: Update a dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","description":"Updated description","widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"apm_issue_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "description" is equal to "Updated description"

  @team:DataDog/dashboards-backend
  Scenario: Update a dashboard with tags returns "OK" response
    Given there is a valid "dashboard" in the system
    And new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    And body with value {"layout_type": "ordered", "title": "{{ unique }} with list_stream widget","description":"Updated description", "tags": ["team:foo", "team:bar"], "widgets": [{"definition": {"type": "list_stream","requests": [{"columns":[{"width":"auto","field":"timestamp"}],"query":{"data_source":"apm_issue_stream","query_string":""},"response_format":"event_list"}]}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "tags" is equal to ["team:foo", "team:bar"]

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Update a shared dashboard returns "Bad Request" response
    Given new "UpdatePublicDashboard" request
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"global_time": {"live_span": "1h"}, "share_list": ["test@datadoghq.com", "test2@datadoghq.com"], "share_type": "invite"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Update a shared dashboard returns "Item Not Found" response
    Given new "UpdatePublicDashboard" request
    And request contains "token" parameter from "REPLACE.ME"
    And body with value {"global_time": {"live_span": "1h"}, "share_list": ["test@datadoghq.com", "test2@datadoghq.com"], "share_type": "invite"}
    When the request is sent
    Then the response status is 404 Item Not Found

  @team:DataDog/dashboards-backend
  Scenario: Update a shared dashboard returns "OK" response
    Given there is a valid "dashboard" in the system
    And there is a valid "shared_dashboard" in the system
    And new "UpdatePublicDashboard" request
    And request contains "token" parameter from "shared_dashboard.token"
    And body with value {"global_time": {"live_span": "15m"}, "share_list": [], "share_type": "open"}
    When the request is sent
    Then the response status is 200 OK
    And the response "dashboard_id" has the same value as "dashboard.id"
    And the response "dashboard_type" is equal to "custom_timeboard"
    And the response "global_time.live_span" is equal to "15m"
    And the response "share_type" is equal to "open"
    And the response "share_list" has length 0
