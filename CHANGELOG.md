# Changelog

## 1.1.0 / 2021-06-08

* [Added] Add CWS to usage metering endpoint. See [#458](https://github.com/DataDog/datadog-api-client-python/pull/458).
* [Added] Add endpoint to list Synthetics global variables. See [#459](https://github.com/DataDog/datadog-api-client-python/pull/459).
* [Added] Add monitors search endpoint. See [#455](https://github.com/DataDog/datadog-api-client-python/pull/455).
* [Added] Add `tag_config_source` to usage attribution response. See [#449](https://github.com/DataDog/datadog-api-client-python/pull/449).
* [Added] Add endpoints to configure Security Filters. See [#440](https://github.com/DataDog/datadog-api-client-python/pull/440).
* [Added] Add `active_child` nested downtime object to `Downtime` component for downtime APIs. See [#434](https://github.com/DataDog/datadog-api-client-python/pull/434).
* [Added] Add audit logs to usage endpoints. See [#466](https://github.com/DataDog/datadog-api-client-python/pull/466).
* [Added] Add `override_label` and `is_hidden` attribute for `WidgetCustomLink`. See [#438](https://github.com/DataDog/datadog-api-client-python/pull/438).
* [Added] Add monitor `name` and `priority` attributes to synthetics test options. See [#473](https://github.com/DataDog/datadog-api-client-python/pull/473).
* [Fixed] Fix type of day/month response attribute in custom metrics usage. See [#471](https://github.com/DataDog/datadog-api-client-python/pull/471).
* [Fixed] Fix handling of log aggregation `oneOf`. See [#463](https://github.com/DataDog/datadog-api-client-python/pull/463).
* [Fixed] Make `assertions` field optional for multistep synthetics tests, and add `global` config variable type. See [#457](https://github.com/DataDog/datadog-api-client-python/pull/457).
* [Fixed] Properly mark monitor required fields. See [#448](https://github.com/DataDog/datadog-api-client-python/pull/448).
* [Fixed] Rename `incident_integration_metadata` to `incident_integrations` to match API. See [#444](https://github.com/DataDog/datadog-api-client-python/pull/444).
* [Fixed] Properly mark several synthetics attributes as read only. See [#437](https://github.com/DataDog/datadog-api-client-python/pull/437).
* [Fixed] Fix paging attributes of usage attribution endpoints. See [#435](https://github.com/DataDog/datadog-api-client-python/pull/435).
* [Changed] Rename `compliance` to `CSPM` in usage endpoint. See [#466](https://github.com/DataDog/datadog-api-client-python/pull/466).

## 1.0.0 / 2021-05-12

* [Added] Notebooks Public API Documentation. See [#432](https://github.com/DataDog/datadog-api-client-python/pull/432).
* [Added] Add `logs_by_retention` usage property and `GetUsageLogsByRetention` endpoint. See [#425](https://github.com/DataDog/datadog-api-client-python/pull/425).
* [Added] Add anomaly detection method to `SecurityMonitoringRuleDetectionMethod` enum. See [#424](https://github.com/DataDog/datadog-api-client-python/pull/424).
* [Added] Add `with_configured_alert_ids` parameter to get a SLO details endpoint. See [#421](https://github.com/DataDog/datadog-api-client-python/pull/421).
* [Added] Add `setCookie`, `dnsServerPort`,  `allowFailure ` and `isCritical` fields for Synthetics tests. See [#418](https://github.com/DataDog/datadog-api-client-python/pull/418).
* [Added] Add `metadata` property with pagination info to `SLOList` endpoint response. See [#414](https://github.com/DataDog/datadog-api-client-python/pull/414).
* [Added] Add new properties to group widget, note widget and image widget. See [#412](https://github.com/DataDog/datadog-api-client-python/pull/412).
* [Added] Add support for a `rate` metric type in manage metric tags v2 endpoint. See [#409](https://github.com/DataDog/datadog-api-client-python/pull/409).
* [Added] Add support for ICMP Synthetics tests. See [#406](https://github.com/DataDog/datadog-api-client-python/pull/406).
* [Added] Add vSphere usage information. See [#402](https://github.com/DataDog/datadog-api-client-python/pull/402).
* [Added] Mark metric volumes and ingested tags endpoints as stable. See [#396](https://github.com/DataDog/datadog-api-client-python/pull/396).
* [Added] Add `filter[shared]` query parameter for searching dashboards. See [#390](https://github.com/DataDog/datadog-api-client-python/pull/390).
* [Added] Add profiling product fields in usage metering endpoint. See [#389](https://github.com/DataDog/datadog-api-client-python/pull/389).
* [Added] Add `title` and `background_color` properties to dashboard group widget. See [#388](https://github.com/DataDog/datadog-api-client-python/pull/388).
* [Added] Add `marker`, `xaxis` and `yaxis` properties on distribution widgets. See [#400](https://github.com/DataDog/datadog-api-client-python/pull/400).
* [Fixed] Remove default value of `is_column_break` layout property of dashboard. See [#431](https://github.com/DataDog/datadog-api-client-python/pull/431).
* [Fixed] Remove nulltype. See [#401](https://github.com/DataDog/datadog-api-client-python/pull/401).
* [Changed] Enumerate accepted values for fields parameter in usage attribution requests. See [#428](https://github.com/DataDog/datadog-api-client-python/pull/428).
* [Changed] Add new enum value for tick interval and remove `request` as required field from synthetics test. See [#426](https://github.com/DataDog/datadog-api-client-python/pull/426).
* [Deprecated] Deprecate `legend_size` and `show_legend` properties on distribution widgets. See [#400](https://github.com/DataDog/datadog-api-client-python/pull/400).
* [Removed] Remove deprecated Synthetics methods `CreateTest` and `UpdateTest`. See [#403](https://github.com/DataDog/datadog-api-client-python/pull/403).

## 1.0.0b8 / 2021-04-15

* [Added] Add `reflow_type` property to dashboard object. See [#372](https://github.com/DataDog/datadog-api-client-python/pull/372).
* [Added] Add security track and formulas and functions support for geomap dashboard widget. See [#370](https://github.com/DataDog/datadog-api-client-python/pull/370).
* [Added] Generate intake endpoints. See [#367](https://github.com/DataDog/datadog-api-client-python/pull/367).
* [Added] Add endpoint for listing all downtimes for the specified monitor. See [#361](https://github.com/DataDog/datadog-api-client-python/pull/361).
* [Added] Add `modified_at` attribute to user response v2 schema. See [#352](https://github.com/DataDog/datadog-api-client-python/pull/352).
* [Added] Add default environment loading in clients. See [#347](https://github.com/DataDog/datadog-api-client-python/pull/347).
* [Added] Add `passed`, `noSavingResponseBody`, `noScreenshot`, and `disableCors` fields to Synthetics. See [#346](https://github.com/DataDog/datadog-api-client-python/pull/346).
* [Added] Add compliance usage endpoint and compliance host statistics. See [#342](https://github.com/DataDog/datadog-api-client-python/pull/342).
* [Added] Add tag filter options for `/api/v{1,2}/metrics`. See [#340](https://github.com/DataDog/datadog-api-client-python/pull/340).
* [Added] Add usage fields for Heroku and OpenTelemetry. See [#337](https://github.com/DataDog/datadog-api-client-python/pull/337).
* [Added] Add `global_time_target` field to SLO widget. See [#335](https://github.com/DataDog/datadog-api-client-python/pull/335).
* [Added] Add method to export an API test in Synthetics. See [#334](https://github.com/DataDog/datadog-api-client-python/pull/334).
* [Added] Add metadata to usage top average metrics response. See [#333](https://github.com/DataDog/datadog-api-client-python/pull/333).
* [Added] Add median as valid aggregator for formulas and functions. See [#328](https://github.com/DataDog/datadog-api-client-python/pull/328).
* [Fixed] Fix Python template for exclusiveMinimum/Maximum. See [#377](https://github.com/DataDog/datadog-api-client-python/pull/377).
* [Fixed] Make python fail properly when invalid key is passed. See [#350](https://github.com/DataDog/datadog-api-client-python/pull/350).
* [Fixed] Fix parsing of `oneOf` attributes. See [#344](https://github.com/DataDog/datadog-api-client-python/pull/344).
* [Fixed] Browser Test message required. See [#330](https://github.com/DataDog/datadog-api-client-python/pull/330).
* [Changed] Return correct object in `GetBrowserTest` endpoint. See [#359](https://github.com/DataDog/datadog-api-client-python/pull/359).
* [Changed] Change python API model. See [#351](https://github.com/DataDog/datadog-api-client-python/pull/351).
* [Changed] Add agent rules in security monitoring rules queries. See [#336](https://github.com/DataDog/datadog-api-client-python/pull/336).

## 1.0.0b7 / 2021-03-22

* [Added] Add `legend_layout` and `legend_columns` to timeseries widget definition. See [#320](https://github.com/DataDog/datadog-api-client-python/pull/320).
* [Added] Add support for multistep tests in Synthetics. See [#313](https://github.com/DataDog/datadog-api-client-python/pull/313).
* [Added] Add core web vitals to synthetics browser test results. See [#308](https://github.com/DataDog/datadog-api-client-python/pull/308).
* [Added] Add v2 metric tags and metric volumes endpoints. See [#307](https://github.com/DataDog/datadog-api-client-python/pull/307).
* [Added] Add new endpoints for browser and API tests in Synthetics. See [#301](https://github.com/DataDog/datadog-api-client-python/pull/301).
* [Added] Add `groupby_simple_monitor` option to monitors. See [#300](https://github.com/DataDog/datadog-api-client-python/pull/300).
* [Added] Allow formula and functions in query value requests. See [#299](https://github.com/DataDog/datadog-api-client-python/pull/299).
* [Added] Allow formula and functions in toplist requests. See [#298](https://github.com/DataDog/datadog-api-client-python/pull/298).
* [Added] Add slack resource. See [#292](https://github.com/DataDog/datadog-api-client-python/pull/292).
* [Added] Add `detectionMethod` and `newValueOptions` fields to security monitoring rules. See [#290](https://github.com/DataDog/datadog-api-client-python/pull/290).
* [Added] Expose "event-v2 alert" monitor type. See [#289](https://github.com/DataDog/datadog-api-client-python/pull/289).
* [Added] Add new US3 region. See [#288](https://github.com/DataDog/datadog-api-client-python/pull/288).
* [Added] Add `org_name` field to usage attribution response. See [#287](https://github.com/DataDog/datadog-api-client-python/pull/287).
* [Changed] Make query name required in formulas and functions queries. See [#311](https://github.com/DataDog/datadog-api-client-python/pull/311).
* [Changed] Rename objects for formulas and functions to be more generic. See [#294](https://github.com/DataDog/datadog-api-client-python/pull/294).
* [Changed] Update response schema for service level objective operation `GetSLOHistory`. See [#319](https://github.com/DataDog/datadog-api-client-python/pull/319).

## 1.0.0b6 / 2021-02-16

* [Added] Add profile_metrics_query properties to dashboard widget requests. See [#282](https://github.com/DataDog/datadog-api-client-python/pull/282).
* [Added] Add geomap widget to dashboards v1. See [#278](https://github.com/DataDog/datadog-api-client-python/pull/278).
* [Added] Add v2 API for metric tag configuration. See [#277](https://github.com/DataDog/datadog-api-client-python/pull/277).
* [Added] Add Lambda invocations usage to response. See [#276](https://github.com/DataDog/datadog-api-client-python/pull/276).
* [Added] Remove unstable flag for logs apis. See [#268](https://github.com/DataDog/datadog-api-client-python/pull/268).
* [Added] Add restricted roles to monitor update. See [#255](https://github.com/DataDog/datadog-api-client-python/pull/255).
* [Added] Add endpoint for IoT billing usage. See [#251](https://github.com/DataDog/datadog-api-client-python/pull/251).
* [Added] Add query parameters for SLO search endpoint. See [#249](https://github.com/DataDog/datadog-api-client-python/pull/249).
* [Added] Add fields for formula and function query definition and widget formulas. See [#245](https://github.com/DataDog/datadog-api-client-python/pull/245).
* [Added] Add global_time to time_window slo widget. See [#243](https://github.com/DataDog/datadog-api-client-python/pull/243).
* [Added] Update required fields in create and update SLO correction requests. See [#235](https://github.com/DataDog/datadog-api-client-python/pull/235).
* [Added] Add docs for log index creation. See [#232](https://github.com/DataDog/datadog-api-client-python/pull/232).
* [Added] Add SLO Corrections. See [#226](https://github.com/DataDog/datadog-api-client-python/pull/226).
* [Fixed] Add missing tlsVersion and minTlsVersion to Synthetics assertion types. See [#284](https://github.com/DataDog/datadog-api-client-python/pull/284).
* [Fixed] Rule: all nested objects in arrays must be defined on top-level. See [#279](https://github.com/DataDog/datadog-api-client-python/pull/279).
* [Fixed] Add support for DD_SITE in examples. See [#271](https://github.com/DataDog/datadog-api-client-python/pull/271).
* [Fixed] Change dashboards analyzed_spans to spans. See [#270](https://github.com/DataDog/datadog-api-client-python/pull/270).
* [Fixed] Fix AWS tag filter delete request. See [#266](https://github.com/DataDog/datadog-api-client-python/pull/266).
* [Fixed] Remove an unnecessary field from TimeSeriesFormulaAndFunctionEventQuery. See [#265](https://github.com/DataDog/datadog-api-client-python/pull/265).
* [Fixed] Fix unit format in SLO history response. See [#260](https://github.com/DataDog/datadog-api-client-python/pull/260).
* [Fixed] Change dashboards group_by from object to list of objects. See [#259](https://github.com/DataDog/datadog-api-client-python/pull/259).
* [Fixed] Fix monitor location of restricted roles. See [#254](https://github.com/DataDog/datadog-api-client-python/pull/254).
* [Fixed] Format the python client using black. See [#252](https://github.com/DataDog/datadog-api-client-python/pull/252).
* [Fixed] Fix paging parameter names for logs aggregate queries. See [#248](https://github.com/DataDog/datadog-api-client-python/pull/248).
* [Fixed] Update to latest apigentools image. See [#230](https://github.com/DataDog/datadog-api-client-python/pull/230).
* [Fixed] Add additionalProperties: false to synthetics target field. See [#228](https://github.com/DataDog/datadog-api-client-python/pull/228).
* [Changed] Fix integer/number formats in Logs and Synthetics endpoints. See [#229](https://github.com/DataDog/datadog-api-client-python/pull/229).

## 1.0.0b5 / 2021-01-13

* [Added] Add new live and rehydrated logs breakdowns to Usage API. See [#223](https://github.com/DataDog/datadog-api-client-python/pull/223).
* [Added] Add support for Synthetics variables from test. See [#214](https://github.com/DataDog/datadog-api-client-python/pull/214).
* [Added] Add filters to rule endpoints in security monitoring API. See [#209](https://github.com/DataDog/datadog-api-client-python/pull/209).
* [Added] Add Azure app services fields to usage v1 endpoints. See [#208](https://github.com/DataDog/datadog-api-client-python/pull/208).
* [Added] Add mobile RUM OS types usage fields. See [#207](https://github.com/DataDog/datadog-api-client-python/pull/207).
* [Added] Add config variables for synthetics API tests. See [#206](https://github.com/DataDog/datadog-api-client-python/pull/206).
* [Added] Add endpoints for the public API of Logs2Metrics. See [#203](https://github.com/DataDog/datadog-api-client-python/pull/203).
* [Added] Add endpoints for API Keys v2. See [#200](https://github.com/DataDog/datadog-api-client-python/pull/200).
* [Added] Add javascript value to synthetics browser variable types. See [#197](https://github.com/DataDog/datadog-api-client-python/pull/197).
* [Added] Add synthetics assertion operator. See [#186](https://github.com/DataDog/datadog-api-client-python/pull/186).
* [Changed] Extract enum to specific schema in incidents endpoint. See [#222](https://github.com/DataDog/datadog-api-client-python/pull/222).
* [Changed] Extract key sorting enum to a specific schema in key management endpoints. See [#218](https://github.com/DataDog/datadog-api-client-python/pull/218).
* [Changed] Rename `list_sl_os` to `list_slos`. See [#216](https://github.com/DataDog/datadog-api-client-python/pull/216).
* [Removed] Remove Synthetic resources property. See [#201](https://github.com/DataDog/datadog-api-client-python/pull/201).

## 1.0.0b4 / 2020-12-10

* [Added] Add Application keys v2 API. See [#182](https://github.com/DataDog/datadog-api-client-python/pull/182).
* [Added] Mark Usage Attribution endpoint as public beta. See [#170](https://github.com/DataDog/datadog-api-client-python/pull/170).
* [Added] Add AWS filtering endpoints. See [#168](https://github.com/DataDog/datadog-api-client-python/pull/168).
* [Added] Add limit parameter for get usage top average metrics. See [#166](https://github.com/DataDog/datadog-api-client-python/pull/166).
* [Added] Add endpoint to fetch process summaries. See [#165](https://github.com/DataDog/datadog-api-client-python/pull/165).
* [Added] Add synthetics private location endpoints. See [#164](https://github.com/DataDog/datadog-api-client-python/pull/164).
* [Added] Add user_update, recommendation and snapshot as event alert types. See [#163](https://github.com/DataDog/datadog-api-client-python/pull/163).
* [Added] Add Usage Attribution endpoint. See [#161](https://github.com/DataDog/datadog-api-client-python/pull/161).
* [Added] Add new API for incident management usage. See [#159](https://github.com/DataDog/datadog-api-client-python/pull/159).
* [Changed] Mark request bodies as required or explicitly optional. See [#176](https://github.com/DataDog/datadog-api-client-python/pull/176).
* [Changed] Mark query field as optional when searching logs. See [#158](https://github.com/DataDog/datadog-api-client-python/pull/158).
* [Deprecated] Deprecate subscription and billing fields in create organization endpoint. See [#167](https://github.com/DataDog/datadog-api-client-python/pull/167).
* [Removed] Remove org_id parameter from Usage Attribution endpoint. See [#172](https://github.com/DataDog/datadog-api-client-python/pull/172).

## 1.0.0b3 / 2020-11-18

* [Added] Add the incident schema. See [#154](https://github.com/DataDog/datadog-api-client-python/pull/154).
* [Added] Add IP prefixes by location for synthetics endpoints. See [#149](https://github.com/DataDog/datadog-api-client-python/pull/149).
* [Added] Add filter parameter for listing teams and services. See [#148](https://github.com/DataDog/datadog-api-client-python/pull/148).
* [Added] Add restricted roles to monitor create and edit requests. See [#146](https://github.com/DataDog/datadog-api-client-python/pull/146).
* [Added] Add 3 new palettes to the conditional formatting options. See [#141](https://github.com/DataDog/datadog-api-client-python/pull/141).
* [Fixed] Quota & retention are now editable fields in log indexes. See [#150](https://github.com/DataDog/datadog-api-client-python/pull/150).
* [Fixed] Add patch to support validating nullable values. See [#144](https://github.com/DataDog/datadog-api-client-python/pull/144).
* [Changed] Change event_query property to use log query definition in dashboard widgets. See [#155](https://github.com/DataDog/datadog-api-client-python/pull/155).
* [Changed] Rename tracing without limits and traces usage endpoints. See [#145](https://github.com/DataDog/datadog-api-client-python/pull/145).

## 1.0.0b2 / 2020-11-05

* [Added] Add missing synthetics step types. See [#129](https://github.com/DataDog/datadog-api-client-python/pull/129).
* [Added] Add include_tags in logs archives. See [#126](https://github.com/DataDog/datadog-api-client-python/pull/126).
* [Changed] Change teams and services objects names to be incident specific. See [#134](https://github.com/DataDog/datadog-api-client-python/pull/134).
* [Removed] Remove `require_full_window` client default value for monitors. See [#135](https://github.com/DataDog/datadog-api-client-python/pull/135).

## 1.0.0b1 / 2020-10-21

* Initial beta release of this client
