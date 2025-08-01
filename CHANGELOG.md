# CHANGELOG

## 2.40.0/2025-07-14

### Added
* Add Datasets API to Open API Spec  [#2691](https://github.com/DataDog/datadog-api-client-python/pull/2691)
* Add support for vulnerability management - GetSBOMsList new endpoint and update existing ones [#2690](https://github.com/DataDog/datadog-api-client-python/pull/2690)
* Add spreadsheet to restriction_policy specs [#2684](https://github.com/DataDog/datadog-api-client-python/pull/2684)
* Adds missing /api/v1/synthetics/tests/search spec [#2673](https://github.com/DataDog/datadog-api-client-python/pull/2673)
* Add API spec for AWS Integrations IAM permissions [#2665](https://github.com/DataDog/datadog-api-client-python/pull/2665)
* New keys added for multiple products [#2663](https://github.com/DataDog/datadog-api-client-python/pull/2663)
* Add extractFromEmailBody step for synthetics browser test [#2660](https://github.com/DataDog/datadog-api-client-python/pull/2660)
* Add support for `Array Processor` in `Logs Pipelines` [#2658](https://github.com/DataDog/datadog-api-client-python/pull/2658)
* Update Incident API specs to include `is_test` in `POST /incidents` and incidents response [#2651](https://github.com/DataDog/datadog-api-client-python/pull/2651)

### Fixed
* update aiosonic from 0.15.1 to 0.24.0 [#2677](https://github.com/DataDog/datadog-api-client-python/pull/2677)
* Synthetics mobile test `message` field is now required [#2657](https://github.com/DataDog/datadog-api-client-python/pull/2657)

### Deprecated
* stop supporting python 3.7 for the client [#2676](https://github.com/DataDog/datadog-api-client-python/pull/2676)

### Changed
* Update template variable schemas with type field in dashboards and shared dashboards endpoints for group by template variables [#2659](https://github.com/DataDog/datadog-api-client-python/pull/2659)
* Update events intake specs for v2 Events post endpoint [#2652](https://github.com/DataDog/datadog-api-client-python/pull/2652)

### Removed
* Remove caseIndex from historical jobs api spec [#2656](https://github.com/DataDog/datadog-api-client-python/pull/2656)

## 2.39.0/2025-06-30

### Fixed
* Synthetics mobile test `message` field is now required [#2657](https://github.com/DataDog/datadog-api-client-python/pull/2657)
* Make dns port be string and number [#2641](https://github.com/DataDog/datadog-api-client-python/pull/2641)
* Fix basic auth requirements [#2638](https://github.com/DataDog/datadog-api-client-python/pull/2638)
* Add support for the api_security detection rule type [#2633](https://github.com/DataDog/datadog-api-client-python/pull/2633)

### Security
* Remove caseIndex from historical jobs api spec [#2656](https://github.com/DataDog/datadog-api-client-python/pull/2656)

### Changed
* Update events intake specs for v2 Events post endpoint [#2652](https://github.com/DataDog/datadog-api-client-python/pull/2652)
* Update events intake specs for v2 Events post endpoint [#2615](https://github.com/DataDog/datadog-api-client-python/pull/2615)
* Add billing read permission [#2611](https://github.com/DataDog/datadog-api-client-python/pull/2611)

### Added
* Update Incident API specs to include `is_test` in `POST /incidents` and incidents response [#2651](https://github.com/DataDog/datadog-api-client-python/pull/2651)
* Add App Key Registration API  [#2645](https://github.com/DataDog/datadog-api-client-python/pull/2645)
* Microsoft Sentinel Public API support [#2636](https://github.com/DataDog/datadog-api-client-python/pull/2636)
* Add the AP2 datacenter. [#2634](https://github.com/DataDog/datadog-api-client-python/pull/2634)
* Add custom fields to Rule update/validate API public documentation. [#2624](https://github.com/DataDog/datadog-api-client-python/pull/2624)
* Add hash field to actions in CWS agent rules [#2621](https://github.com/DataDog/datadog-api-client-python/pull/2621)
* Add `form` field for `multipart/form-data` HTTP API tests [#2606](https://github.com/DataDog/datadog-api-client-python/pull/2606)

### Deprecated
* Deprecate SLO metadata fields in api spec [#2608](https://github.com/DataDog/datadog-api-client-python/pull/2608)

## 2.38.0/2025-06-24

### Fixed
* Fix basic auth requirements [#2638](https://github.com/DataDog/datadog-api-client-python/pull/2638)
* Add support for the api_security detection rule type [#2633](https://github.com/DataDog/datadog-api-client-python/pull/2633)

### Added
* Microsoft Sentinel Public API support [#2636](https://github.com/DataDog/datadog-api-client-python/pull/2636)
* Add the AP2 datacenter. [#2634](https://github.com/DataDog/datadog-api-client-python/pull/2634)
* Add custom fields to Rule update/validate API public documentation. [#2624](https://github.com/DataDog/datadog-api-client-python/pull/2624)
* Add hash field to actions in CWS agent rules [#2621](https://github.com/DataDog/datadog-api-client-python/pull/2621)
* Add `form` field for `multipart/form-data` HTTP API tests [#2606](https://github.com/DataDog/datadog-api-client-python/pull/2606)
* SDCD-1142: adding `custom_tags` optional attribute to DORA API spec [#2605](https://github.com/DataDog/datadog-api-client-python/pull/2605)
* Add sampling fields to SDS spec [#2601](https://github.com/DataDog/datadog-api-client-python/pull/2601)
* Add new endpoint to upsert/list/delete custom kinds [#2600](https://github.com/DataDog/datadog-api-client-python/pull/2600)
* Add spec for team on-call endpoint [#2598](https://github.com/DataDog/datadog-api-client-python/pull/2598)

### Changed
* Update events intake specs for v2 Events post endpoint [#2615](https://github.com/DataDog/datadog-api-client-python/pull/2615)
* Add billing read permission [#2611](https://github.com/DataDog/datadog-api-client-python/pull/2611)

## 2.37.0/2025-06-23

### Fixed
* Fix basic auth requirements [#2638](https://github.com/DataDog/datadog-api-client-python/pull/2638)
* Add support for the api_security detection rule type [#2633](https://github.com/DataDog/datadog-api-client-python/pull/2633)

### Added
* Microsoft Sentinel Public API support [#2636](https://github.com/DataDog/datadog-api-client-python/pull/2636)
* Add custom fields to Rule update/validate API public documentation. [#2624](https://github.com/DataDog/datadog-api-client-python/pull/2624)
* Add hash field to actions in CWS agent rules [#2621](https://github.com/DataDog/datadog-api-client-python/pull/2621)
* Add `form` field for `multipart/form-data` HTTP API tests [#2606](https://github.com/DataDog/datadog-api-client-python/pull/2606)
* SDCD-1142: adding `custom_tags` optional attribute to DORA API spec [#2605](https://github.com/DataDog/datadog-api-client-python/pull/2605)
* Add sampling fields to SDS spec [#2601](https://github.com/DataDog/datadog-api-client-python/pull/2601)
* Add new endpoint to upsert/list/delete custom kinds [#2600](https://github.com/DataDog/datadog-api-client-python/pull/2600)
* Add spec for team on-call endpoint [#2598](https://github.com/DataDog/datadog-api-client-python/pull/2598)

### Changed
* Update events intake specs for v2 Events post endpoint [#2615](https://github.com/DataDog/datadog-api-client-python/pull/2615)
* Add billing read permission [#2611](https://github.com/DataDog/datadog-api-client-python/pull/2611)
* Update DORA endpoints [#2591](https://github.com/DataDog/datadog-api-client-python/pull/2591)

## 2.36.0/2025-06-16

### Changed
* Add billing read permission [#2611](https://github.com/DataDog/datadog-api-client-python/pull/2611)
* Update DORA endpoints [#2591](https://github.com/DataDog/datadog-api-client-python/pull/2591)

### Added
* Add `form` field for `multipart/form-data` HTTP API tests [#2606](https://github.com/DataDog/datadog-api-client-python/pull/2606)
* Add new endpoint to upsert/list/delete custom kinds [#2600](https://github.com/DataDog/datadog-api-client-python/pull/2600)
* Add spec for team on-call endpoint [#2598](https://github.com/DataDog/datadog-api-client-python/pull/2598)
* Add support for Datadog Events as a data source for rules [#2578](https://github.com/DataDog/datadog-api-client-python/pull/2578)
* Add public APIs to search DORA events [#2575](https://github.com/DataDog/datadog-api-client-python/pull/2575)
* Add support for all subtypes in multistep steps [#2573](https://github.com/DataDog/datadog-api-client-python/pull/2573)
* Added new optional field definition to include more detail in findings for '/api/v2/posture_management/findings'  [#2569](https://github.com/DataDog/datadog-api-client-python/pull/2569)
* Exposing set action on Terraform V2 [#2568](https://github.com/DataDog/datadog-api-client-python/pull/2568)
* Adding endpoints to manage Resource Evaluation Filters [#2567](https://github.com/DataDog/datadog-api-client-python/pull/2567)
* Add monitor draft status field [#2566](https://github.com/DataDog/datadog-api-client-python/pull/2566)

### Fixed
* add `include` parameter to On-Call team rules test [#2582](https://github.com/DataDog/datadog-api-client-python/pull/2582)
* fix On-Call spec [#2572](https://github.com/DataDog/datadog-api-client-python/pull/2572)

## 2.35.0/2025-05-28

### Fixed
* add `include` parameter to On-Call team rules test [#2582](https://github.com/DataDog/datadog-api-client-python/pull/2582)
* fix On-Call spec [#2572](https://github.com/DataDog/datadog-api-client-python/pull/2572)
* Fix incorrect pattern for url [#2558](https://github.com/DataDog/datadog-api-client-python/pull/2558)
* Make metadata optional for GCS destination [#2549](https://github.com/DataDog/datadog-api-client-python/pull/2549)
* Remove isReadOnly default when creating dashboards [#2548](https://github.com/DataDog/datadog-api-client-python/pull/2548)
* Make assertion target be int or string [#2545](https://github.com/DataDog/datadog-api-client-python/pull/2545)

### Added
* Add support for Datadog Events as a data source for rules [#2578](https://github.com/DataDog/datadog-api-client-python/pull/2578)
* Add public APIs to search DORA events [#2575](https://github.com/DataDog/datadog-api-client-python/pull/2575)
* Adding endpoints to manage Resource Evaluation Filters [#2567](https://github.com/DataDog/datadog-api-client-python/pull/2567)
* Add Sev0 as a supported incident severity [#2561](https://github.com/DataDog/datadog-api-client-python/pull/2561)
* Share timerestriction object [#2557](https://github.com/DataDog/datadog-api-client-python/pull/2557)
* add On-Call Paging spec [#2551](https://github.com/DataDog/datadog-api-client-python/pull/2551)
* Add pagination method for NDM ListDevices. [#2547](https://github.com/DataDog/datadog-api-client-python/pull/2547)

## 2.34.0 / 2025-04-14

### Fixed
* Change `type` to enum to discriminate included items in the response of `ListCatalogEntity` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2465
* Deprecate options from logs aggregate API public spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2476
* change a category in enum for datadog_appsec_waf_custom_rule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2470
### Added
* Add datasource to job definition for security monitoring  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2460
* Include new rum types in Usage_metering Yaml by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2463
* Adding new UT apm_error_events keys in summary endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2457
* Add more triggers for workflow automation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2471
* Add specs for Cloud Network Monitoring API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2480
* Add more Security Monitoring Data Source enum values by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2475
* Add componentOf field to Service, Queue, and Datastore V3 Software Catalog definitions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2478
* Add 'mute_buttons' argument to slack channel definition by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2482
* Add Observability Pipelines API  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2481
* add rum slo bugfix by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2490
* Add trace_rate support to APM retention filter APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2494
* Update NDM GetInterfaces documentation to add ip_addresses attribute by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2493
* Add assertRequests browser step type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2498
* Add user behavior case actions in API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2497
### Changed
* Remove OpenAPI enum enforcement of Service Definition v2dot2 type field from service definition endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2461
* Add on-call schedules endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2486

## New Contributors
* @ofek made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/2403

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.33.1...2.34.0

## 2.33.1 / 2025-03-11

### Changed
* Remove meta from RUM retention filters APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2454


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.33.0...2.33.1

## 2.33.0 / 2025-03-11

### Fixed
* Remove `javascript` browser variable type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2399
* Additional rules to inject openapi type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2420
* Fix `ListCatalogEntity` pagination endpoint to use correct offset value by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2439
### Added
* add new related_assets filter query parameter to the get a list of metrics V2 API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2366
* Add actions and groupSignalsBy field in detection rules API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2401
* Add Workflows CRUD Public API Endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2391
* Add endpoint to retrieve Security Monitoring rule version history by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2372
* Adds override_existing_configurations and include_actively_queried_configurations to bulk tag config endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2410
* Add `number_format` to each formula in widget by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2413
* Add `trend` support for `cell_display_mode` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2409
* Add support for span id remapper in logs pipelines processors by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2421
* Add evaluation_window and keep_alive for Security monitoring rule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2422
* Add `extractedValuesFromScript` to multistep API tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2426
* Update timezone for cumulative window by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2425
* Document Agentless AWS scan options routes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2435
* Create types for app builder queries explicitly, remove experimental flag by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2411
* Document Agentless AWS on demand routes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2440
* Add quality_issues to monitor schema on monitor search API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2442
* Introduce public v2 endpoints for Application Security by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2427
* Add delete log index to public API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2441
* Add v2 endpoints for RUM retention filters. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2436
* Added storage class information to the S3 archive destination by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2448
### Changed
* Revert GetSBOM to `x-unstable` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2404
* Update documentation with account filtering info for aws_cur_config endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2416
* Update sharing APIs to match server by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2424
* Update Vulnerabilities endpoints documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2428
### Deprecated
* Deprecate API management endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2415

## New Contributors
* @ava-silver made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/2433

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.32.0...2.33.0

## 2.32.0 / 2025-02-05

### Fixed
* Modify owner properties to be a string by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2392
### Added
* Add UT breakdown for fargate_container_profiler billing dimension by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2323
* Add synthetics browser step public_id field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2183
* Add support for vulnerability management  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2324
* add start_date to suppression APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2291
* Add CSM Coverage Analysis API specs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2329
* Add allow_self_lockout to documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2338
* Ephemeral Infra_host new keys in summary endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2340
* Update app builder API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2333
* Add meta and source fields to JSONAPIErrorItem by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2332
* Add CSM Agentless Read Endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2330
* Update rum doc to include new usage types by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2343
* add cost monitor type to API Spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2354
* Add Action Connection API for Workflow Automation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2341
* Add `type` in Data Deletion API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2358
* Add a cost monitor example by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2363
* Add `provider_name` attribute to pipelines API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2345
* Add support for vulnerability management - GetSBOM new endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2359
* Remove preview status for GetBillingDimensionMapping endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2371
* Add encryption field to logs archive destination by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2369
* Add tags and description to logs pipelines by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2374
* Publish security notification rules API endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2367
* Publish app builder API documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2347
* update public document with configuration event type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2382
* Add support for Entity kind API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2387
* Rename `embeddedQueries` attribute to `queries` in app builder api by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2388
### Changed
* Fix specification for Azure metric filtering by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2327
* Change allow_self_lockout from string to bool by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2342
* remove flag Beta for cost-by-tag endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2379
* Added Support for Workflow Webhooks Public API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2383
* Vulnerabilities endpoints GA - Remove `x-unstable` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2389


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.31.0...2.32.0

## 2.31.0 / 2024-12-17

### Fixed
* Stop strings in arbitrary type fields from automatically converting to UUID by @nkzou in https://github.com/DataDog/datadog-api-client-python/pull/2274
### Added
* Adds accepted reasons for archiving signal by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2162
* Add usage type breakdown for error tracking billing dimension by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2251
* Add Historical Job endpoints to Datadog API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2250
* Add new keys for CWS Fargate Task in summary usage and usage attribution endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2254
* Add missing measures for SLOs data source by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2255
* Create AWS Integrations v2 API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1990
* Add step_functions as valid enum for v1 AWS tag filter spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2263
* Fix authz scope descriptions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2273
* Updated OpenAPI logs_pattern_query to support Patterns for any attribute by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2272
* Add API specification for events intake v2 by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2205
* Data Deletion Endpoints Documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2258
* Add `exitIfSucceed` to multistep API tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2307
* Security Monitoring Rule - Add the updatedAt field in the SecurityMonitoringStandardRuleResponse by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2283
* add docs for pagination in /api/v2/metrics endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2174
* Add daily as a valid enum for SLOReportInterval by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2316
* Add new product Code Security host for summary endpoint and UA endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2285
* Add CSM Agents Read Endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2314
* Add app builder API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2309
### Changed
* Fix spelling error for bindings by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2252
* Revert the earlier spelling change by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2257
* Remove mobile device ids and make all device ids simple string by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2269
* Remove support for `namespace_filters.include/exclude_all` in v2 AWS Integrations API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2271
* Add running pipelines on custom pipelines API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2266
### Removed
* Remove unnecessary field in list stream column config by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2317
### Deprecated
* Remove `/api/v2/cost/enabled` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2304

## New Contributors
* @bthuilot made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/2312

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.30.0...2.31.0

## 2.30.0 / 2024-11-07

### Fixed
* Fix Toplist widget's stacked display style - remove legend as required field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2184
* Remove user fields that are unsupported by the Incidents API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2195
* Refactor data serialization by @therve in https://github.com/DataDog/datadog-api-client-python/pull/2211
* Fix Synthetics batch status by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2245
### Added
* Add MSTeams integration metadata info by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2197
* Add `code_analysis_sa_committers_hwm` and `code_analysis_sca_committers_hwm` to UsageMetering by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2198
* Update GCP API Spec to support `is_resource_change_collection_enabled` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2201
* Add vulnerability type to Findings API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2200
* Update Documentation for Data Stream Monitoring by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2207
* Add LLM Observability to ListStreamSource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2206
* Add synthetics stepDetail.allowFailure and stepDetail.failure by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2217
* Integrate incident types into Incidents API documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2199
* Add `use_recommended_keywords` attribute to sensitive data scanner rule spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2228
* Add code 512 to retry status codes by @HantingZhang2 in https://github.com/DataDog/datadog-api-client-python/pull/2225
* Add domain allowlist endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2224
* Add v2 endpoints for RUM custom metrics. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2223
* Documentation for beta /v2/usage/billing_dimension_mapping by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2152
* Add `alwaysExecute` and `exitIfSucceed` to Synthetics steps by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2246
* Add metric_namespace_configs to GCP v2 API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2248
### Changed
* Edit Naming for v2 Microsoft Teams Integration Endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2196
* Change the mobile device ids from enum to string by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2194
* Mark Cost Attribution end_month parameter as not required by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2181
* Allow for any type for additionalProperties in HTTPLogItem by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2216
* Make some amendments to the new mobiles schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2215
* Make value be oneOf number or string by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2229
* Add examples for resources for Cloudflare by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2222
### Removed
* Remove deprecated estimated usage types for usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2220
### Deprecated
* Deprecate two sds metadata fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2214
* Delete `api/v2/cost/aws_related_accounts` from spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2232
* Deprecate `api/v2/cost/enabled` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2241


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.29.0...2.30.0

## 2.29.0 / 2024-10-02

### Fixed
* change schema used in FastlyServicesResponse by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2173
* Fix crash when closing an async client. by @jack-edmonds-dd in https://github.com/DataDog/datadog-api-client-python/pull/2186
### Added
* Add new synthetics HTTP javascript assertion by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2091
* Dashboards - Toplist widget style - Add palette by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2146
* Allow Table Widget requests to specify text replace formatting in dashboards by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2147
* Add documentation for Data Jobs Monitoring summary keys by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2154
* Update estimate docs with realtime changes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2177
* Ensure clients can handle empty oneOf objects by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2175
* Add referenceTables field to security monitoring endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2170
* Add UA documentation for new DJM usage_type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2171
* Add v2 endpoints for MS Teams Integration by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2180
* Add documention for OCI Integration by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2188
* Add schema for mobile test by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2163
* Add Synthetics endpoint to fetch uptimes in API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2140
### Changed
* Split the synthetics request port field into a oneOf by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2157
* Remove unused field `color` in `TeamUpdateAttributes` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2155
* Powerpack add support for prefix and available values by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2164
* Update v2 metrics list endpoint filter by metric type to use metric type category by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2179


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.28.0...2.29.0

## 2.28.0 / 2024-09-04

### Fixed
* Enable additionalProperties by default by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/2111
* Add `is_totp` and `is_fido` to Synthetic global variables by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2059
* Handle nested oneOfs during serialization by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/2136
### Added
* Add `api_key` and `name` to `CloudflareAccountResponseAttributes`. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2105
* Add `api_key` and `name` to `FastlyAccountUpdateRequestAttributes`. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2106
* Add `opsgenie_api_key` to `OpsgenieServiceResponseAttributes`. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2107
* Add `category` and `remote_config_read_enabled` to `APIKeyCreateAttributes`, and add `LeakedKey`. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2108
* Allow 4 group-bys for pattern viz by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2116
* add url attribute to metrics assets v2 api by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2118
* Add editable field to suppression rule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2021
* Add `num_flex_logs_retention_days` field to logs_indexes api spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2119
* Software catalog openapi spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2137
### Changed
* allow variables in port by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2092
* Fix VFTs and extracted local variables enum types by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2078
* Changed Widget time schema to add support for new fixed_span and live_span object by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2097
### Deprecated
* mark groupby_simple_monitor as deprecated by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2134


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.27.0...2.28.0

## 2.27.0 / 2024-08-12

### Fixed
* fix monitor enum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2046
* dashboards add support for time-slice SLOs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2047
* Make modified by field nullable for get all API keys by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2053
* Add `409 Conflict` to `CreateGlobalVariable` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2063
* Dont inject content type on empty body by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/2079
### Added
* add cross org uuids to timeseries query by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2010
* Add network performance monitor type to API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2022
* Document `force_delete_dependencies` for synthetics test deletion by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2016
* Support metric filtering in integration azure GET, PUT APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2027
* add enableProfiling and enableSecurityTesting options by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2037
* Add convert rule JSON to terraform to Datadog API Spec. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2014
* add changes for datadog partner program to estimated cost and billable usage APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2018
* Add type as a required field for the different basic auth types by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2029
* Adding Network Device Monitoring API Documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2024
* Security Monitoring - Support anomaly threshold detection method by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2044
* update hourly usage API docs for partner program by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2054
* Add resource_type query param to authn mapping spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1989
* Add rum stream to API definition by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2058
* Support `incident_analytics` enum in dashboard widget `FormulaAndFunctionEventsDataSource` data sources by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2068
* update usage summary API docs for partner program by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2065
* update historical_cost and projected_cost for partner program by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2056
* Add custom cost endpoints to public API documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2076
* Update documentation for Cloud SIEM Analyzed Logs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2070
* Update documentation for App Sec SCA by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2061
* Add trigger API documentation for workflow automation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2034
* Add PUT endpoint to scorecards APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2081
* Documentation for new device tags endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2072
* Update documentation for Flex Logs Starter by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2089
### Changed
* add mfa_enabled field and change created_at type to datetime by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2090
### Deprecated
* Deprecate `ListAWSRelatedAccounts` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2062

## New Contributors
* @amaskara-dd made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/2051

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.26.0...2.27.0

## 2.26.0 / 2024-07-01

### Fixed
* Security Monitoring - Define specific payload for rule validation/testing by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1987
* Remove the maximum limitation for the synthetics renotify_interval monitor option by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1991
* Add bodyHash as a synthetics assertion type. by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1992
* Handle unparseable objects in the Python client. by @jack-edmonds-dd in https://github.com/DataDog/datadog-api-client-python/pull/2009
* Add missing attributes envelope in ListAPIs response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2000
### Added
* Allow the usage of the filters field when creating an agent rule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1967
* Add tileDef sort attribute by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1969
* Add Security Monitoring rule test endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1983
* Add originalFileName field to the SyntheticsTestRequestBodyFile definition by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1988
* Add support for API management ListAPIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1995
* Add elementsOperator to json path assertion for synthetic HTTP tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2006
* Add /api/v2/org_configs specs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2005
* Update docs for RU Rollout New and Deprecated Keys planned for Oct 1st by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2020
* Add option for wait step in multistep api tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2019
### Changed
* Monitor priority can have custom ranges and be null by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/2017

## New Contributors
* @tim-chaplin-dd made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1927
* @jack-edmonds-dd made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/2009

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.25.0...2.26.0

## 2.25.0 / 2024-05-21

### Fixed
* Fix param retrieval for async client paginated calls by @garretruh in https://github.com/DataDog/datadog-api-client-python/pull/1951
### Added
* Add JSONSchema assertion support to API and multistep tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1925
* add 1 day logs to usage api docs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1952
* Update UserTeamIncluded to include teams by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1957
* Security Monitoring - Make Default Tags available in the response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1966
* Add flex logs storage tier by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1968
### [**Breaking**] Changed
* Rename the Cloud Workload Security tag to CSM Threats by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1956

## New Contributors
* @garretruh made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1951

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.24.1...2.25.0

## 2.24.1 / 2024-04-18

### Fixed
* fix case search documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1943
### Added
* Add support variablesFromScript in Synthetics API test by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1945


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.24.0...2.24.1

## 2.24.0 / 2024-04-11

### Fixed
* Update Cleanup script to use GCP STS endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1903
* Add include data to get team memberships response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1889
### Added
* Add `ci-pipeline-fingerprints` field in v2.2 by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1909
* Add validation endpoint for Security Monitoring Rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1930
* Add UA documentation for online_archive and incident_management by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1932
* Mark `unit` as nullable by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1934
* Add query_interval_seconds to time-slice SLO condition parameters by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1936
* Support providing files for the file upload feature when creating a Synthetic API test by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1935
* Adding SLO Reporting API Documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1906
* Security Monitoring Suppression - Add data_exclusion_query field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1940
* aws api adding extended and deprecating old resource collection field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1938
### Changed
* Add Team relationship to AuthNMappings by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1864
### Deprecated
* Remove deprecated /api/v1/usage/attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1920
* Deprecate legacy hourly usage metering endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1916


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.23.0...2.24.0

## 2.23.0 / 2024-03-13

### Fixed
* Move under common tag Case Management by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1867
* Include user data with team membership resource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1863
* Disable additionalProperties for Downtime Schedule UpdateRequest oneOfs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1873
* Fix ListServiceDefinitions pagination information by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1897
### Added
* Case Management Public API documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1848
* Make grpc steps available for synthetics api multisteps tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1866
* Add cloud run filter to GCP v1 and v2 spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1845
* add ASM serverless to usage metering API docs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1876
* Add new products to usage API docs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1880
* Adds support for `ListMetricAssets` endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1878
* Add support for new CRUD agent rules endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1892
* Add documentation for workflow usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1898
* Add Custom Destinations Public API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1902
### Changed
* Update spec for DORA Metrics Incident endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1865
### Deprecated
* Deprecate the pattern property for SDS Standard Pattern Attributes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1893
* Deprecate Incident Services endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1904

## New Contributors
* @antonio-ramadas-dd made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1901

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.22.0...2.23.0

## 2.22.0 / 2024-02-06

### Fixed
* Add test support for file parameters by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1839
* Make validation target type a union of int and float by @nkzou in https://github.com/DataDog/datadog-api-client-python/pull/1843
* Security Monitoring Suppressions - Make expiration date nullable in update payload by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1849
### Added
* Security Monitoring - Add API support for suppression rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1834
* Document support for BYDAY in SLO corrections by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1840
* Add missing optional field env in DORA API endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1841
* Add compressedProtoFile field to SyntheticsTestRequest by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1838
* Add daily limit reset options to logs indexes api by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1842
* Add support for API management API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1837
* Add pagination helper for team memberships by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1851
* Increase limit on allowed number of graphs in split graph widget by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1856
### Deprecated
* Mark dashboard 'is_read_only' and 'restricted_roles' properties as deprecated by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1827


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.21.0...2.22.0

## 2.21.0 / 2024-01-10

### Fixed
* Prioritize auth configuration values over environment variables by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1787
### Added
* Add priority field to SDS rule and standard-pattern by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1803
* Document new `resource_collection` and `is_security_command_center_enabled` fields in GCP APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1804
* Add SAML attributes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1797
* Security Monitoring - Support custom third party rules by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1821
* Add public API support for time-slice SLOs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1813
* Add included_keyword_configuration field to SDS rule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1824
* Update Documentation for APM DevSecOps by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1825
### Changed
* Mark v1 downtime endpoints as deprecated by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1818
* Adding Cloud Cost Management API Documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1811
* Add support for Cloudflare API `zone` and `resource` fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1823


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.20.0...2.21.0

## 2.20.0 / 2023-12-12

### Fixed
* Fix Powerpack schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1752
### Added
* Add support for projected-cost endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1735
* Document missing incident fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1756
* Add active billing dimensions to usage metering by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1773
* Add Cost Attribution To Usage Metering Public Beta Documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1759
* Update spec to include new DORA API endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1772
* Add support to patch Synthetics test with partial data using JSON Patch by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1767
* Document new api/app key schemas by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1755
* Document new field `filters` for `CloudWorkloadSecurityAgentRule` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1774
* Live and historical custom timeseries docs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1765
* Add week_to_date and month_to_date to widget livespan by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1768
* Document `included_keywords` in `ListStandardPatterns` response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1777
* Document fields `remote_config_read_enabled` and `category` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1775
* Update Azure Spec to include Resource Collection by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1782
* Allow creation of Application Security detection rules from the v2 API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1784
* Add Okta Integration APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1766
* Remove unstable flag for Events v2 api by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1791


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.19.0...2.20.0

## 2.19.0 / 2023-11-15

### Fixed
* Add minimal typing_extensions version by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1728
* Remove notify_no_data default by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1732
* Fix SecurityMonitoringSignalAttribute field name by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1739
* Fix typo in service definition field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1754
### Added
* Update documentation for Cloud SIEM by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1722
* Add containers API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1723
* Add serverless apm to usage attribution api by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1729
* Document missing parameters by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1680
* Powerpack Live Span Support by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1738
* Add Amazon EventBridge endpoints to AWS Integration API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1724
* Add Container App filters to Azure API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1703
* Add UUID format support by @HantingZhang2 in https://github.com/DataDog/datadog-api-client-python/pull/1743
* Add new UA products to usage metering docs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1741
* Add scorecards endpoints  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1747
* Document top list widget style by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1733
* Add optional group-bys support to security signals by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1748
### Changed
* Add Beta Banner to Send Pipeline Events Endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1737
* Remove endpoint for mute or unmute a finding and add support for bulk mute findings endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1734


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.18.0...2.19.0

## 2.18.0 / 2023-10-16

### Fixed
* Fix schema for query scalar API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1668
* Remove the application key from CreateCIAppPipelineEvent endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1679
* Document 403 on team endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1687
* Pass all keyword/ arguments to avoid panics with `setuptools_scm` > 8 by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/1702
* Powerpack improve group_widget object by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1704
* Remove escalation message default by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1720
### Added
* Add split graph widget to dashboard schema  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1644
* Update public docs for CSM Enterprise and CSPM by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1664
* Add serverless apps to usage and usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1685
* Add Network Device Monitoring Netflow to usage by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1694
* Add Powerpacks endpoints to public api spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1665
* Add account-tags to GCP Service Account Attributes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1678
* Add powerpack widget to dashboard schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1697
* Add custom schedule to monitor scheduling options by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1681
* Service Catalog support service definition schema v2.2 by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1709
* Powerpack pagination and test fixes by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1716
* Add support for container images endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1714
* Add global IP ranges to spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1349
### Changed
* Add APM retention filter api documentation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1653
* Update request requirements of CI Visibility public pipelines write API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1689
* Add get APM retention filter endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1692
* Remove beta label notice on create pipeline API endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1715

## New Contributors
* @romainkomorndatadog made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1710

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.17.0...2.18.0

## 2.17.0 / 2023-09-14

### Fixed
* Fix downtimes monitor relationship id schema type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1649
* Pass SSL configuration arguments to Async Api Client by @vxuv in https://github.com/DataDog/datadog-api-client-python/pull/1655
### Added
* Add trace_stream to dashboard ListStreamSource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1622
* Add pagination extension to SLO corrections by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1631
* Adding aas count to the documentation for summary and hourly usage endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1635
* Add pagination extension to SLOs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1632
* Add pagination extension to monitors by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1633
* Add pagination extension to synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1640
* Add 'style' to sunburst requests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1639
* Add pagination extension to notebook by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1642
* Add support for dashboard listing pagination parameters by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1646
* Add pagination parameters to downtimes listing by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1648
* Add pagination extension to user list by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1647
* Add pagination extension to team listing by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1650
* Remove private beta for Downtimes v2 by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1645
* Update v1 monitor api docs to exclude downtimes v2 by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1660
* Add timing scope for response time assertions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1651
* Add Formula and Function query support to heatmap widgets by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1661
* Add synthetics mobile application testing to usage metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1657
### Changed
* Add spectral rule for validating `no unnamed objects` in lists by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1656

## New Contributors
* @vxuv made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1655

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.16.0...2.17.0

## 2.16.0 / 2023-08-23

### Fixed
* Handle `{}` and `bool` for additionalProperties by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/1590
* Update team schemas by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1588
* Mark downtime v2 start response as required by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1601
* Document new properties and fix security monitoring schemas by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1587
* Add missing CI App fields `page` and `test_level` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1565
### Added
* Update stated limit for api/v2/metrics from 14 days to 30 days by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1594
* Add missing sensitive data scanner fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1584
* Add support for retry of HTTP requests by @HantingZhang2 in https://github.com/DataDog/datadog-api-client-python/pull/1384
* Add Workflow Executions to usage metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1597
* Add missing `type` field for OnDemandConcurrencyCap response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1586
* Add CI Visibility Intelligent Test Runner to usage metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1595
* Add custom_links to distribution widget schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1605
* Add usage field `region` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1606
* Add `message` field to audit logs response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1608
* Add `tags` field to dashboard list response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1607
* Support retry in async client by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1613
* API specs for user team memberships by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1618
* Document `EQUAL` comparator by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1621
* Add persistCookies option synthetics test request by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1620
* Expose sds_scanned_bytes_usage in usage attribution API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1624
* Add support in azure integration endpoint for app service plan filters/cspm/custom metrics by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1619
* Support paginated methods in async client by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1615
* Add APM and USM usage attribution type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1617
* Document new attributes for team models by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1614

## New Contributors
* @HantingZhang2 made their first contribution in https://github.com/DataDog/datadog-api-client-python/pull/1384

**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.15.0...2.16.0

## 2.15.0 / 2023-07-20

### Fixed
* Spans API docs update by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1553
* Fix filter indexes parameter in logs search by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1559
* Fix Spans endpoint schemas by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1580
### Added
* Add support for geomap widget using response_type `event_list` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1534
* Add support for the spans API endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1539
* Add a new field additional_query_filters to formula and function slo query by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1555
* Add support for `enable_custom_metrics` in Confluent Account by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1562
* Add missing `id` attribute for Confluent Account Response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1560
* Fix downtimes v2 schema and add missing field `canceled` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1568
* Add cloud_cost data source and query definition to dashboards by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1569
* Add missing cloud workload security fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1575
* Add `integration_id` field for dashboard list item by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1579
* Add events response fields `message` and `status` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1576
* Add missing `GetRUMApplications` response field `id` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1577
* Add missing service definition fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1578
* Add overlay type to Dashboards WidgetDisplayType by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1581
* Update IP ranges with remote configuration section by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1583
* Add missing `relationships` to UsersInvitations response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1585
* Added optional field filters when creating a cloud configuration rule by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1589
### Changed
* Add downtime v2 API in private beta by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1482
* Allow use of latest urllib3 by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1556
* Mark `access_role` as nullable by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1566


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.14.0...2.15.0

## 2.14.0 / 2023-06-27

### Fixed
* Mark `restricted_roles` as nullable in monitor update request by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1508
* Mark additional usage fields as `nullable` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1516
* Updated findings api error responses by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1486
* Mark usage metering field `lines_indexed` as `nullable` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1521
* Update dashboard widget axis field descriptions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1507
* Fix `CreateGCPSTSAccount` return code and update tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1528
* Fix `CreateGCPSTSAccount` response status code by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1531
* Add missing descriptions for authorization scopes in public docs  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1529
* Update CI Visibility pipelines write API endpoint fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1535
### Added
* Add support for mute findings endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1469
* Expose `database-monitoring` monitor type by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1354
* Add endpoint to get Synthetics default locations by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1515
* Add usage metering RUM Roku fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1522
* Add usage metering fields for AWS and Azure cloud cost management by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1524
* Add support for CI Visibility create pipeline events endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1523
* Add isUndefined synthetics assertion operator by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1527
* Add missing Synthetics and Metrics Scope descriptions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1530
### Deprecated
* mark v1 GCP APIs as deprecated by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1518


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.13.2...2.14.0

## 2.13.2 / 2023-06-05

### Fixed
* Re-introduce array container models by @skarimo in https://github.com/DataDog/datadog-api-client-python/pull/1503


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.13.1...2.13.2

## 2.13.1 / 2023-06-01

### Fixed
* Add back array models for compatibility by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1499
### Changed
* Team name and handle length updates by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1495


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.13.0...2.13.1

## 2.13.0 / 2023-05-31

### Fixed
* Mark usage fields as nullable by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1432
* Properly mark usage fields as nullable by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1451
* Remove read only attributes from team create and update by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1455
### Added
* Expose `include_breakdown` param for v2 hourly_usage by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1424
* Add support for deserializing `additionalProperties` in GO client by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1417
* Add new grpc assertions for Synthetics tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1429
* add additional_query_filters to slo widget  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1443
* Add `customer_impact_scope` to fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1441
* Add notify_end_states and notify_end_types options to downtime by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1445
* Add snapshot timestamp to GetFinding by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1457
* Support schema version parameter in Get and List Service Definition endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1460
* Add Application Vulnerability Management to usage metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1461
* Add formula and function slo query to dash widgets by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1466
* Add secure field to Synthetics Browser Test variables and update docs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1465
* Add MatchingDowntime to monitor schema and with_downtimes parameter to GetMonitor by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1475
* Add auth scopes for the `service_definition` endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1479
* Update documentation for observability pipeline bytes usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1472
* Add option to obfuscate extracted values from Synthetics multistep tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1473
* Add support for GCP STS endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1464
* Add `sort` field to List Stream Widget's request query by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1492
### Changed
* Update spec to change findings limit and security monitoring menu order by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1426
* Require teams_manage scope for creating and deleting teams by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1444
* Remove models for arrays by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1431
* Update team name and handle length restrictions by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1493
### Deprecated
* Deprecate note for Incident Teams endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1450


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.12.0...2.13.0

## 2.12.0 / 2023-04-18

### Fixed
* Fix application_security_host_top99p usage field by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1383
* Mark `resource_type` attribute as required for Confluent Account by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1400
* Fix spec errors caught with prism validation by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1413
* Fix spans/logs custom metrics delete operation responses by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1419
### Added
* Add support for Incident Todo APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1368
* Add supported relations in restriction policy  by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1380
* Add parameter to downtime API for returning creator info by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1382
* Publish the new ingested timeseries metrics for usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1365
* Add tags field to dashboard API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1373
* Add pagination support to SearchIncidents by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1391
* Add service catalog v2.1 schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1387
* Add team API specs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1385
* Add spans metrics API endpoints specification by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1392
* Add universal service monitoring to usage metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1395
* Add a new contact type in service catalog api for schema v2 and v2.1 by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1398
* Add pagination support for the GET service_definitions endpoint by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1403
* Publish logs forwarding fields in summary usage API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1402
* Add compressedJsonDescriptor to Synthetics gRPC tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1401
* Add region field and note about multiregion start by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1386
* Add AP1 support by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1409
* Add support for shared dashboards endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1396
### Deprecated
* Deprecate audit logs usage by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1411


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.11.0...2.12.0

## 2.11.0 / 2023-03-14

### Fixed
* Fix oneOf generation with mixed types including primitives by @nkzou in https://github.com/DataDog/datadog-api-client-python/pull/1374
### Added
* Add restriction policy APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1337
* Support RUM data source in Query API and fix aggregators by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1345
* Add endpoint to get and set on demand concurrency cap for Synthetics by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1341
* Publish IP allowlist APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1330
* Expose Flutter fields to rum product in the meter usage API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1350
* Improve typing coverage on the api_client module by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1347
* Add profiled fargate tasks to usage attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1355
* Add cipipeline stream to ListStreamSource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1321
* Add application_security to security monitoring rule type enum by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1353
* Add `ci_pipelines` enum to `FormulaAndFunctionEventsDataSource` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1363
* Add citest stream to ListStreamSource by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1358
* Add `logs_issue_stream` enum to `ListStreamSource` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1364
* Add support for Incident Integration Metadata APIs by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1356
* Add SLO to GRACE API spec by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1371
* Add audit trail to usage metering API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1370


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.10.0...2.11.0

## 2.10.0 / 2023-02-15

### Fixed
* Set hosts versions as `type any` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1339
### Added
* Add orchestrator section in IP ranges by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1331
* Add Cloud Cost Management fields to Usage Metering endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1335
* Add cloud-cost as a supported query data source by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1327
* Add Cloud Cost And Container Excl Agent Usage Fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1340
* Add SLO status and error budget remaining to search API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1344
* Add `sort` field to SLOListWidgetQuery by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1342


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.9.0...2.10.0

## 2.9.0 / 2023-02-08

### Fixed
* Mark timeseries values as nullable by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1296
* Fix APIs default init by @therve in https://github.com/DataDog/datadog-api-client-python/pull/1303
* Add namespaces attribute and rename excluded_attributes in SDS Public API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1308
* Set macV as `type any` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1323
### Added
* Add Support for Incident Management Search API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1251
* Add TOTP parameters to Synthetics test options by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1291
* Add httpVersion option to Synthetics API tests by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1300
* Add deprecationDate to security monitoring rule response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1301
* Add new group by configuration to list stream widget by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1298
* Add synthetics advanced scheduling by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1282
* Add notification preset enum field to monitor options by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1305
* Add support for Cloudflare integration API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1304
* Add support for Fastly account API by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1233
* Add monitor configuration policies by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1307
* Support is_cspm_enabled field in GCP integrations by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1316
* Add run workflow widget to dashboard schema by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1309
* Add new missing enum values for `aggregation` and `detectionMethod` by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1325
* Add region to estimated cost and historical cost response by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1326
* Add Usage Metering container_excl_agent_usage fields by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1328
* Add event_stream fields to dashboard list stream widget by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1329
### Changed
* Remove indexed logs from Usage Attribution by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1290
* Remove pagination parameter from CI visibility aggregate endpoints by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1295
* Move Service account create from users to service accounts by @api-clients-generation-pipeline in https://github.com/DataDog/datadog-api-client-python/pull/1313


**Full Changelog**: https://github.com/DataDog/datadog-api-client-python/compare/2.8.0...2.9.0

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
