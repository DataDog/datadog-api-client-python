# Changelog

## 2.8.0 / 2023-01-05

### Fixed
* Remove incorrect required fields from CloudConfigurationComplianceRuleOptions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1276
* Update CI Visibility types of BucketResponse schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1278
* Fix logs aggregate integer facets by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1285
### Added
* Add support for query scalar and timeseries endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1274
* Add estimated rum sessions usage types to UA enums by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1269
* Update API spec to allow primary timeframe, target, and warning by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1280
* Add Usage Metering Cont Usage fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1281
* Add secure field to synthetics config variables by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1283
* Expose helper method to retrieve oneOf instance by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/1284


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.7.0...2.8.0

## 2.7.0 / 2022-12-20

### Fixed
* Add missing response fields to MTD usage attribution endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1259
* Fix missing field in Synthetics tests authentication configuration by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1263
* Mark `hosts` response version fields as nullable by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1261
### Added
* Add fields for CSPM GCP usage by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1237
* Add offset and limit parameter to SLO correction API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1241
* Add documentation for Logs Pipelines ReferenceTableLogsLookupProcessor  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1240
* Adding new field for the usage metering infra hosts by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1244
* Add `include_percentiles` field in Logs Custom Metrics by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1224
* Add OAuth support for Synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1247
* Add new billable summary fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1257
* RUM Applications Management API add client_token by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1243
* Support GRPC unary calls in Synthetics by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1253
* Add style object to dashboard widget formulas by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1266
* Add enable_samples monitor option by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1267
* Update security_monitoring endpoints for cloud_configuration rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1268
* Add support for sensitive data scanner APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1265
* Add synthetics_parallel_testing to Usage Metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1270
* Synthetics add pagination params to get all tests endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1271


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.6.0...2.7.0

## 2.6.0 / 2022-11-16

### Fixed
* Fix service catalog schema change by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1232
### Added
* Add support for CI Visibility API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1210
* Add support for querying logs in Online Archives by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1199
* Add new SDS fields to usage API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1211
* Remove Beta status for SLO history endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1212
* Update formula and function monitor enum datasource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1217
* Add scheduling_options to monitor definition by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1218
* Appsec Fargate Public Documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1221
* Adds noScreenshot to SyntheticsStep by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1223
* Add support for xpath assertions in synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1204
* Add bodyType to Synthetics request by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1229


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.5.0...2.6.0

## 2.5.0 / 2022-10-24

### Fixed
* Add Default Rule ID in SignalRuleResponseQuery by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1196
* Remove incident's resolved attribute from update requests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1197
* Fix event monitor created_at by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1198
* Fix spectral rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1202
### Added
* Add notify_by monitor option by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1189
* Add support for service definitions APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1203
* Add support for confluent cloud integration by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1143
* Add type annotations to models by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1200
### Deprecated
* Deprecate metric field of Security Monitoring Rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1208


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.4.0...2.5.0

## 2.4.0 / 2022-10-03

### Fixed
* Refactor RuleQuery models by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1183
* Fix SearchSLO response structure by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1184
* Handle deprecation of APIs and attributes by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1170
### Added
* Add ListActiveConfigurations endpoint and add new filter[queried] param to list tag configurations endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1120
* Improve enum handling by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1159
* Support proxy in async client by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1162
* Add doesNotExist to synthetics operator enum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1153
* Add TopologyMapWidget to dashboard schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1157
* Add Overall Status support to SLO Search API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1158
* Add APM Fargate to Usage Metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1152
* Add support for template variable multiselect in dashboards by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1163
* Add storage option to widget query definitions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1167
* Add support for retrieving a security signal by ID by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1175
* Add support for signal correlation API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1168
* Add support for SLO List widget by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1174
* Add new historical_cost endpoint, and update estimate_cost by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1166
* Add support for incident attachment APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1181

## New Contributors
* @nkzou made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1151
* @dependabot made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1171

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.3.0...2.4.0

## 2.3.0 / 2022-08-31

### Fixed
* Update Pagerduty operation `DeletePagerDutyIntegrationService` response status code by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1114
* Fix oneOf primitive objects creation by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1125
### Added
* Add support for digest auth in synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1121
* Add support for RUM application endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1122
* add priority parameters for dashboard monitor summary widget by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1127
* Add `logs_pattern_stream` to `list_stream` widget source by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1129
* Add group_retention_duration and on_missing_data monitor options by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1124
* Expose CSPM aws host count in Usage Metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1141
* Add estimated ingested logs attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1115
* Add org region to usage summary and billable usage summary by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1136
* add compression methods to metric payloads by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1112
* Add role relationships to RoleUpdateData by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1138
* Add `ci_tests` enum to FormulaAndFunctionEventsDataSource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1137
* Add missing options and request option to synthetics test by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1128
* Add support for global variable from multistep synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1100
### Changed
* update deprecated usage attribution API docs to direct users to migra… by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1130
* [Synthetics] remove started form eventType enum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1132


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.2.0...2.3.0

## 2.2.0 / 2022-08-01

### Added
* docs(dataviz): update Treemap widget definition with deprecated properties + updated description [VIZZ-2305] by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1099
* Add hourly usage v2 endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1084
* Add metrics field in the RuleQuery by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1085
* Add support for Events V2 endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1057
* [RQ-2492]: Add custom_events to list of product families in hourly-usage api. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1108
* Re-introduce Estimated Cost API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1116


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.1.0...2.2.0

## 2.1.0 / 2022-07-19

### Fixed
* Remove include_percentiles default by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1065
* Mark message as required for Synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1059
* Add synthetics results api replay only tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1098
### Added
* New usage metering endpoint for estimated cost by org by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1069
* Add estimated indexed spans usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1068
* Handle raw  json for additionalProperties in typescript  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1040
* Add Application Security Monitoring Hosts Attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1070
* Add support for security monitoring rule dynamic criticality by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1054
* Update IP ranges with synthetics private locations section by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1075
* Add typing information to pagination methods by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1078
* Add new products to billable summary by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1080
* Update usage attribution enums by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1071
* Add estimated ingested spans to usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1089
* Add v2 Security monitoring signals triage operations. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1081
### Changed
* Add typing to API arguments by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1076
* Update metric intake v2 accept response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1077
* Add description of metric type enums by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1090
* remove x-unstable property for usage attribution endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1097

## New Contributors
* @ganeshkumarsv made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1095

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.0.0...2.1.0

## 2.0.0 / 2022-06-24

### Fixed
* AuthN Mapping spec cleanup to match implementation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1006
* Fix compress call by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1028
* Add cls to the list of keywords by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1038
* Fix additionalProperties on SyntheticsAPITestResultData by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1036
* Fix synthetics vitals type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1039
### Added
* Add connection to synthetics assertion type enum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1010
* Add grpc subtype to synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/985
* Add support for `zstd1` Content-Encoding by @jirikuncar in https://github.com/DataDog/datadog-api-client-python/pull/946
* Add include descendants to monthly and hourly usage attribution APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1032
* Add v2 endpoints for Opsgenie Integration by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1021
* Add distribution points intake endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1019
* Add height and width params to graph snapshot by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1048
* Add support for defining histogram requests in Distribution widgets by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1030
* Add DowngradeOrg endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1050
* Add new options for new value detection type on security monitoring rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1042
* Add ci execution rule in Synthetics options by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1043
* Add SLO Search API endpoint  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/949
### Changed
* Remove unstable marker from SLO corrections API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1020
* Remove unstable/beta note since Metrics Without Limits is GA by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1029
* Refactor API client by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1018
* Remove unstable marker on security list signal endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1047

## New Contributors
* @jybp made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1063

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/1.12...2.0.0

## 1.12 / 2022-05-23

### Fixed
* Remove duplicated lazy imports by @therve in https://github.com/DataDog/datadog-api-client-python/pull/983
* Remove unused pararameter from authn mapping by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/986
### Added
* Expose v2 usage endpoint for application security monitoring by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/978
* Add `rehydration_max_scan_size_in_gb` field to Logs Archives by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/973
* Add `mute_first_recovery_notification` option to downtime by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/942
* Add lambda traced invocations usage endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/984
* Expose new usage field for react sessions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/987
* Add missing option and enum value for SecurityMonitoringRule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/993
* Adds docs for metric estimate endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/975
* Allow additional log attributes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/966
* Add v2 endpoint for submitting series by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/911
* Add `ci-tests` monitor type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/992
* Add RUM settings schema to synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1001
* Add v1 signal triage endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/997
### Deprecated
* Deprecate old usage apis by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/989


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/1.11.0...1.12

## 1.11.0 / 2022-04-27

### Fixed
* Fix type for `date` field in `LogsByRetentionMonthlyUsage` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/864
* Fix org name maximum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/894
* Fix pagination for top avg metrics endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/899
* Rename models and operations with mixed cases by @therve in https://github.com/DataDog/datadog-api-client-python/pull/904
* Fix generation of oneOf types by @jirikuncar in https://github.com/DataDog/datadog-api-client-python/pull/921
* Allow bool coercion/conversion by @therve in https://github.com/DataDog/datadog-api-client-python/pull/922
* Fix type of nullable additionalProperties by @jirikuncar in https://github.com/DataDog/datadog-api-client-python/pull/926
* Make type optional for synthetics basic auth model by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/933
* Fix camel case version of `ListSLOs` by @jirikuncar in https://github.com/DataDog/datadog-api-client-python/pull/955
* Serialize body in async client by @therve in https://github.com/DataDog/datadog-api-client-python/pull/952
* Set correct type for `tags` property by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/950
### Added
* Add impossible travel detection method by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/855
* Add CI App usage endpoint and usage summary columns by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/860
* [RUM] Add search endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/859
* Add support for getting online archive usage by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/868
* Add endpoint for retrieving audit logs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/866
* Add support for Error Tracking monitors by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/896
* Add support for `ci-pipelines` monitor using Formulas and Functions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/906
* Add aggregate endpoint for RUM by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/919
* Add  `median` aggregation functions to RUM and logs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/931
* Add endpoint for validation of existing monitors by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/932
* Create new ListStreamSource types in order to deprecate ISSUE_STREAM by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/939
* [Query Value Widget] Add the timeseries background by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/930
* Add `restricted_roles` to Synthetics tests and private locations by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/941
* Add v2 SAML config IdP Metadata upload endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/948
* Support pagination in Python by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/957
* Add Usage API endpoint for observability-pipelines and add properties to v1 GetUsageSummary by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/928
* Add Historical Chargeback Summary endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/967
### Changed
* Move shared modules outside of versions by @therve in https://github.com/DataDog/datadog-api-client-python/pull/870
* Bump minimum python by @therve in https://github.com/DataDog/datadog-api-client-python/pull/883
* Migrate to a global configuration by @therve in https://github.com/DataDog/datadog-api-client-python/pull/900
### Removed
* Remove `lambda_usage` and `lambda_percentage` from usage API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/914
* [dashboards] Removed `issue_stream` type from `ListStreamSource` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/944
### Deprecated
* [monitors] Deprecate `locked` property and clarify documentation for `restricted_roles` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/888

## New Contributors
* @juan-fernandez made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/869

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/1.10.0...1.11.0

## 1.10.0 / 2022-03-02

### Fixed
* Add missing type to enum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/844
* Add nullable user relationships to incidents and use this relationship schema for `commander_user` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/799
* Fix event intake response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/849
* Use custom generator by @therve in https://github.com/DataDog/datadog-api-client-python/pull/853
### Added
* [Synthetics] Add missing option for SSL tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/851


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/1.9.0...1.10.0

## 1.9.0 / 2022-02-17

### Fixed
* Add missing type to `CloudWorkloadSecurityAgentRuleAttributes` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/841
### Added
* Add organization metadata to additional Usage API responses by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/809
* Add support for formula and function in monitors by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/815
* Add endpoint for managing SAML AuthN mappings by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/813
* [Synthetics] Add `isCritical` to browser test steps by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/826
* Add metrics bulk-config endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/818
* Add support for "estimated usage attribution" by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/839
* Add org metadata for all hourly usage endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/843
### Changed
* Add CSPM usage fields and change properties to nullable doubles by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/795
* Add synthetics test result failure field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/811
* Fix funnel steps definition by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/832
* Store unknown model properties in `_data_store` map by @therve in https://github.com/DataDog/datadog-api-client-python/pull/837
* Extract incident meta object by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/838


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/1.8.0...1.9.0

## 1.8.0 / 2022-01-20

* [Added] Add `filter[deleted]` parameter for searching recently deleted dashboards. See [#787](https://github.com/DataDog/datadog-api-client-python/pull/787).
* [Added] Add support for authentication and proxy options in Synthetics. See [#742](https://github.com/DataDog/datadog-api-client-python/pull/742).
* [Added] Support formulas and functions in Treemap Widget. See [#782](https://github.com/DataDog/datadog-api-client-python/pull/782).
* [Added] Add Cloud Workload Security Agent Rules API. See [#769](https://github.com/DataDog/datadog-api-client-python/pull/769).
* [Added] Add `offset` and `limit` parameters to usage listing endpoint. See [#774](https://github.com/DataDog/datadog-api-client-python/pull/774).
* [Added] Add monthly usage attribution API spec. See [#754](https://github.com/DataDog/datadog-api-client-python/pull/754).
* [Added] Add missing hosts metadata fields. See [#747](https://github.com/DataDog/datadog-api-client-python/pull/747).
* [Added] Add `replay_session_count ` and update documentation for `rum_session_count`. See [#773](https://github.com/DataDog/datadog-api-client-python/pull/773).
* [Added] Add retry options for a step in Synthetics multistep test. See [#758](https://github.com/DataDog/datadog-api-client-python/pull/758).
* [Added] Document `author_name` in dashboard response. See [#755](https://github.com/DataDog/datadog-api-client-python/pull/755).
* [Added] Add organization metadata for RUM sessions usage and expose `rum_browser_and_mobile_session_count`. See [#748](https://github.com/DataDog/datadog-api-client-python/pull/748).
* [Added] Add endpoint to retrieve hourly usage attribution. See [#724](https://github.com/DataDog/datadog-api-client-python/pull/724).
* [Added] Add support for scoped application keys. See [#705](https://github.com/DataDog/datadog-api-client-python/pull/705).
* [Added] Add endpoint for cloning roles. See [#732](https://github.com/DataDog/datadog-api-client-python/pull/732).
* [Added] Add organization metadata for audit logs, CWS, CSPM, DBM. See [#740](https://github.com/DataDog/datadog-api-client-python/pull/740).
* [Added] Add `ci-pipelines alert` to monitors enum. See [#731](https://github.com/DataDog/datadog-api-client-python/pull/731).
* [Added] Add support for sunburst widget in dashboard. See [#736](https://github.com/DataDog/datadog-api-client-python/pull/736).
* [Added] Add async client to Python. See [#737](https://github.com/DataDog/datadog-api-client-python/pull/737).
* [Fixed] Clarify required fields for `SyntheticsAPIStep`, `SyntheticsAPITest`, and `SyntheticsBrowserTest`. See [#667](https://github.com/DataDog/datadog-api-client-python/pull/667).
* [Fixed] Fixes to Cloud Workload Security API. See [#785](https://github.com/DataDog/datadog-api-client-python/pull/785).
* [Fixed] Make downtime weekdays nullable. See [#761](https://github.com/DataDog/datadog-api-client-python/pull/761).
* [Fixed] Do type conversion all the time in Python. See [#757](https://github.com/DataDog/datadog-api-client-python/pull/757).
* [Fixed] Fix a typo in an incident field attribute description. See [#713](https://github.com/DataDog/datadog-api-client-python/pull/713).
* [Fixed] Fix `SecurityMonitoringSignal.attributes.tags` type. See [#716](https://github.com/DataDog/datadog-api-client-python/pull/716).
* [Changed] Remove read only fields in `EventCreateRequest`. See [#783](https://github.com/DataDog/datadog-api-client-python/pull/783).
* [Changed] Change pagination arguments for querying usage attribution. See [#753](https://github.com/DataDog/datadog-api-client-python/pull/753).
* [Deprecated] Remove session counts from RUM units response. See [#728](https://github.com/DataDog/datadog-api-client-python/pull/728).
* [Removed] Remove deprecated AgentRule field in Security Rules API for CWS. See [#746](https://github.com/DataDog/datadog-api-client-python/pull/746).

## 1.7.0 / 2021-12-10

* [Added] [dashboards formulas and functions] Add formulas and functions support to change widget. See [#567](https://github.com/DataDog/datadog-api-client-python/pull/567).
* [Added] Add RUM Units to usage metering API. See [#657](https://github.com/DataDog/datadog-api-client-python/pull/657).
* [Added] Add trigger synthetics tests endpoint. See [#642](https://github.com/DataDog/datadog-api-client-python/pull/642).
* [Added] [Synthetics] Add support for UDP API tests. See [#662](https://github.com/DataDog/datadog-api-client-python/pull/662).
* [Added] Add support for `websocket` synthetics tests. See [#674](https://github.com/DataDog/datadog-api-client-python/pull/674).
* [Added] Add support for profiled Fargate tasks in Usage API. See [#670](https://github.com/DataDog/datadog-api-client-python/pull/670).
* [Added] Add 429 error responses. See [#675](https://github.com/DataDog/datadog-api-client-python/pull/675).
* [Added] Document query in `MonitorSearchResult`. See [#690](https://github.com/DataDog/datadog-api-client-python/pull/690).
* [Added] Expose `public_id` and `org_name` in Usage API response. See [#692](https://github.com/DataDog/datadog-api-client-python/pull/692).
* [Added] Add endpoint to get corrections applied to an SLO. See [#689](https://github.com/DataDog/datadog-api-client-python/pull/689).
* [Added] Expose estimated logs usage in Usage Attribution API. See [#700](https://github.com/DataDog/datadog-api-client-python/pull/700).
* [Added] Add Limit Note for Hourly Requests. See [#699](https://github.com/DataDog/datadog-api-client-python/pull/699).
* [Fixed] Fix type for `ratio_in_month` in usage metering. See [#652](https://github.com/DataDog/datadog-api-client-python/pull/652).
* [Fixed] Change `UsageNetworkFlowsHour.indexed_event_count` to match actual API. See [#661](https://github.com/DataDog/datadog-api-client-python/pull/661).
* [Fixed] SLO Correction attributes `rrule` and `duration` can be nullable. See [#665](https://github.com/DataDog/datadog-api-client-python/pull/665).
* [Fixed] Mark `batch_id` in Synthetics Trigger CI response as nullable. See [#677](https://github.com/DataDog/datadog-api-client-python/pull/677).
* [Fixed] Remove event title length constraint. See [#682](https://github.com/DataDog/datadog-api-client-python/pull/682).
* [Fixed] Fix monitor `timeout_h` example and limits. See [#687](https://github.com/DataDog/datadog-api-client-python/pull/687).
* [Fixed] Be more resilient to plain text errors. See [#696](https://github.com/DataDog/datadog-api-client-python/pull/696).
* [Fixed] Make python fail properly on invalid header. See [#711](https://github.com/DataDog/datadog-api-client-python/pull/711).
* [Fixed] Remove python unused conversion arguments calls. See [#714](https://github.com/DataDog/datadog-api-client-python/pull/714).
* [Changed] [Synthetics] Fix required target in assertions and type in step results. See [#666](https://github.com/DataDog/datadog-api-client-python/pull/666).
* [Changed] Reorganize python params_map. See [#710](https://github.com/DataDog/datadog-api-client-python/pull/710).

## 1.6.0 / 2021-11-09

* [Added] Add support for Azure `automute` option. See [#647](https://github.com/DataDog/datadog-api-client-python/pull/647).
* [Added] Add v2 intake endpoint. See [#640](https://github.com/DataDog/datadog-api-client-python/pull/640).
* [Added] Add support for RRULE fields in SLO corrections. See [#600](https://github.com/DataDog/datadog-api-client-python/pull/600).
* [Added] Add aggregations attribute to v2 metric tag configuration. See [#577](https://github.com/DataDog/datadog-api-client-python/pull/577).
* [Added] Add `apm_stats_query` property to `DistributionWidgetRequest`. See [#628](https://github.com/DataDog/datadog-api-client-python/pull/628).
* [Fixed] Use plural form for dbm hosts usage properties. See [#611](https://github.com/DataDog/datadog-api-client-python/pull/611).
* [Fixed] Make monitor properties `priority` and `restricted_roles` nullable. See [#627](https://github.com/DataDog/datadog-api-client-python/pull/627).
* [Changed] Update Synthetics CI test metadata. See [#610](https://github.com/DataDog/datadog-api-client-python/pull/610).
* [Deprecated] Update property descriptions for Dashboard RBAC release. See [#639](https://github.com/DataDog/datadog-api-client-python/pull/639).

## 1.5.0 / 2021-10-15

* [Added] Add `type` and `is_template` properties to notebooks. See [#615](https://github.com/DataDog/datadog-api-client-python/pull/615).
* [Added] Add `renotify_occurrences` and `renotify_statuses` monitor options. See [#613](https://github.com/DataDog/datadog-api-client-python/pull/613).
* [Added] Add `servername` property to SSL Synthetics tests request. See [#603](https://github.com/DataDog/datadog-api-client-python/pull/603).
* [Added] Document encoding in metrics intake. See [#604](https://github.com/DataDog/datadog-api-client-python/pull/604).
* [Added] Add support for formulas and functions in the Scatterplot Widget for dashboards. See [#587](https://github.com/DataDog/datadog-api-client-python/pull/587).
* [Added] Add support for gzip and deflate encoding. See [#593](https://github.com/DataDog/datadog-api-client-python/pull/593).
* [Added] Add information about creator to Synthetics tests details. See [#596](https://github.com/DataDog/datadog-api-client-python/pull/596).
* [Added] Add support for funnel widget in dashboards. See [#590](https://github.com/DataDog/datadog-api-client-python/pull/590).
* [Added] Add formula and function APM resource stats query definition for dashboards. See [#582](https://github.com/DataDog/datadog-api-client-python/pull/582).
* [Added] ApmDependencyStatsQuery for formulas and functions dashboard widgets. See [#581](https://github.com/DataDog/datadog-api-client-python/pull/581).
* [Fixed] Fix handling of primitive types in oneOfs. See [#621](https://github.com/DataDog/datadog-api-client-python/pull/621).
* [Fixed] Remove event title length constraint. See [#598](https://github.com/DataDog/datadog-api-client-python/pull/598).
* [Fixed] Allow nullable date in notebook cells. See [#607](https://github.com/DataDog/datadog-api-client-python/pull/607).
* [Fixed] `IncidentFieldAttributesMultipleValue` can be nullable. See [#602](https://github.com/DataDog/datadog-api-client-python/pull/602).
* [Fixed] Fix incidents schemas. See [#601](https://github.com/DataDog/datadog-api-client-python/pull/601).
* [Fixed] Make sure that OpenAPI definition are valid with real server responses. See [#595](https://github.com/DataDog/datadog-api-client-python/pull/595).
* [Fixed] Fix typo in usage attribution field names for profiled containers. See [#597](https://github.com/DataDog/datadog-api-client-python/pull/597).
* [Fixed] Make the name property required for APM Dependency Stat Query widget. See [#586](https://github.com/DataDog/datadog-api-client-python/pull/586).
* [Fixed] Mark SLO Correction Type as required. See [#568](https://github.com/DataDog/datadog-api-client-python/pull/568).
* [Changed] Enable compression in responses. See [#612](https://github.com/DataDog/datadog-api-client-python/pull/612).
* [Changed] Use AVG aggregation function for DBM queries. See [#592](https://github.com/DataDog/datadog-api-client-python/pull/592).

## 1.4.O / 2021-09-14

* [Added] Add restricted roles for Synthetics global variables. See [#550](https://github.com/DataDog/datadog-api-client-python/pull/550).
* [Added] Add events data source to Dashboard widgets. See [#545](https://github.com/DataDog/datadog-api-client-python/pull/545).
* [Added] Add support for security monitoring rule `type` property. See [#544](https://github.com/DataDog/datadog-api-client-python/pull/544).
* [Added] Add `batch_id` to the synthetics trigger endpoint response. See [#556](https://github.com/DataDog/datadog-api-client-python/pull/556).
* [Added] Add `audit alert` monitor type. See [#559](https://github.com/DataDog/datadog-api-client-python/pull/559).
* [Added] Add DBM usage endpoint. See [#546](https://github.com/DataDog/datadog-api-client-python/pull/546).
* [Added] Add config variables to Synthetics browser test config. See [#563](https://github.com/DataDog/datadog-api-client-python/pull/563).
* [Added] Add `available_values` property to template variables schema. See [#564](https://github.com/DataDog/datadog-api-client-python/pull/564).
* [Added] Add `follow_redirects` options to test request in Synthetics. See [#571](https://github.com/DataDog/datadog-api-client-python/pull/571).
* [Fixed] Minor fixes of the incident schema. See [#552](https://github.com/DataDog/datadog-api-client-python/pull/552).
* [Fixed] Make SLO history metadata unit nullable. See [#555](https://github.com/DataDog/datadog-api-client-python/pull/555).
* [Fixed] Fix python unparsed serialization. See [#569](https://github.com/DataDog/datadog-api-client-python/pull/569).
* [Fixed] Fix SLO history error response type for overall errors. See [#570](https://github.com/DataDog/datadog-api-client-python/pull/570).
* [Changed] Fix SLO history schema for groups and monitors fields. See [#575](https://github.com/DataDog/datadog-api-client-python/pull/575).
* [Changed] Remove metadata from required list for metric SLO history endpoint. See [#579](https://github.com/DataDog/datadog-api-client-python/pull/579).

## 1.3.0 / 2021-08-16

* [Added] Add Webhooks integration support. See [#549](https://github.com/DataDog/datadog-api-client-python/pull/549).
* [Added] Add missing synthetics variable parser type `x_path`. See [#548](https://github.com/DataDog/datadog-api-client-python/pull/548).
* [Added] Add `audit_stream` to `ListStreamSource`. See [#536](https://github.com/DataDog/datadog-api-client-python/pull/536).
* [Added] Add percentile to dashboard `WidgetAggregator` schema. See [#532](https://github.com/DataDog/datadog-api-client-python/pull/532).
* [Added] Add `id_str` property to Event response. See [#538](https://github.com/DataDog/datadog-api-client-python/pull/538).
* [Added] Add edge to Synthetics devices. See [#542](https://github.com/DataDog/datadog-api-client-python/pull/542).
* [Added] Add endpoints to manage Service Accounts v2. See [#523](https://github.com/DataDog/datadog-api-client-python/pull/523).
* [Added] Add `new_group_delay` and deprecate `new_host_delay` monitor properties. See [#535](https://github.com/DataDog/datadog-api-client-python/pull/535).
* [Added] Add `include_descendants` param to usage attribution API. See [#540](https://github.com/DataDog/datadog-api-client-python/pull/540).
* [Added] Update to latest openapi generator image. See [#528](https://github.com/DataDog/datadog-api-client-python/pull/528).
* [Added] Add support for list widget in dashboards. See [#504](https://github.com/DataDog/datadog-api-client-python/pull/504).
* [Added] Extend table widget requests to support formulas and functions. See [#526](https://github.com/DataDog/datadog-api-client-python/pull/526).
* [Added] Add CSPM to usage attribution. See [#518](https://github.com/DataDog/datadog-api-client-python/pull/518).
* [Added] Add support for dashboard bulk delete, restore endpoints. See [#501](https://github.com/DataDog/datadog-api-client-python/pull/501).
* [Added] Add support for audit logs data source in dashboards. See [#521](https://github.com/DataDog/datadog-api-client-python/pull/521).
* [Added] Add `allow_insecure` option for multistep steps in Synthetics. See [#515](https://github.com/DataDog/datadog-api-client-python/pull/515).
* [Fixed] Improve resiliency of the Python SDK. See [#531](https://github.com/DataDog/datadog-api-client-python/pull/531).
* [Fixed] Fix serialization of query metrics response containing nullable points. See [#516](https://github.com/DataDog/datadog-api-client-python/pull/516).
* [Fixed] Fix `status` property name for browser error status in Synthetics. See [#517](https://github.com/DataDog/datadog-api-client-python/pull/517).
* [Changed] Add separate schema for deleting AWS account. See [#513](https://github.com/DataDog/datadog-api-client-python/pull/513).
* [Removed] Remove deprecated endpoints `/api/v1/usage/traces` and `/api/v1/usage/tracing-without-limits`. See [#519](https://github.com/DataDog/datadog-api-client-python/pull/519).

## 1.2.0 / 2021-07-08

* [Added] Add support for `GET /api/v2/application_keys/{app_key_id}`. See [#502](https://github.com/DataDog/datadog-api-client-python/pull/502).
* [Added] Add `meta` property with pagination info to SLOCorrectionList endpoint response. See [#499](https://github.com/DataDog/datadog-api-client-python/pull/499).
* [Added] Add support for treemap widget. See [#494](https://github.com/DataDog/datadog-api-client-python/pull/494).
* [Added] Add missing properties `query_index` and `tag_set` to `MetricsQueryMetadata`. See [#468](https://github.com/DataDog/datadog-api-client-python/pull/468).
* [Added] Add missing fields `hasExtendedTitle`, `type`, `version` and `updateAuthorId` for Security Monitoring Rule endpoints. See [#483](https://github.com/DataDog/datadog-api-client-python/pull/483).
* [Added] Dashboard RBAC role support. See [#478](https://github.com/DataDog/datadog-api-client-python/pull/478).
* [Added] Add missing fields in usage billable summary keys. See [#477](https://github.com/DataDog/datadog-api-client-python/pull/477).
* [Fixed] Remove US only constraint for AWS tag filtering. See [#490](https://github.com/DataDog/datadog-api-client-python/pull/490).
* [Fixed] Add BDD tests to synthetics. See [#489](https://github.com/DataDog/datadog-api-client-python/pull/489).
* [Fixed] Fix Python type checking. See [#487](https://github.com/DataDog/datadog-api-client-python/pull/487).
* [Fixed] Handle null in query metrics unit. See [#486](https://github.com/DataDog/datadog-api-client-python/pull/486).
* [Changed] Specify format of `report_id` parameter. See [#510](https://github.com/DataDog/datadog-api-client-python/pull/510).
* [Changed] Remove Synthetics tick interval enum. See [#488](https://github.com/DataDog/datadog-api-client-python/pull/488).

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
