# Changelog

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
