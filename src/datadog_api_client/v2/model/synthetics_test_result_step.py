# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_step_assertion_result import (
        SyntheticsTestResultStepAssertionResult,
    )
    from datadog_api_client.v2.model.synthetics_test_result_assertion_result import SyntheticsTestResultAssertionResult
    from datadog_api_client.v2.model.synthetics_test_result_bounds import SyntheticsTestResultBounds
    from datadog_api_client.v2.model.synthetics_test_result_browser_error import SyntheticsTestResultBrowserError
    from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys
    from datadog_api_client.v2.model.synthetics_test_result_cdn_resource import SyntheticsTestResultCdnResource
    from datadog_api_client.v2.model.synthetics_test_result_step_element_updates import (
        SyntheticsTestResultStepElementUpdates,
    )
    from datadog_api_client.v2.model.synthetics_test_result_variable import SyntheticsTestResultVariable
    from datadog_api_client.v2.model.synthetics_test_result_failure import SyntheticsTestResultFailure
    from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
    from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo
    from datadog_api_client.v2.model.synthetics_test_result_rum_context import SyntheticsTestResultRumContext
    from datadog_api_client.v2.model.synthetics_test_result_sub_step import SyntheticsTestResultSubStep
    from datadog_api_client.v2.model.synthetics_test_result_sub_test import SyntheticsTestResultSubTest
    from datadog_api_client.v2.model.synthetics_test_result_tab import SyntheticsTestResultTab
    from datadog_api_client.v2.model.synthetics_test_result_variables import SyntheticsTestResultVariables
    from datadog_api_client.v2.model.synthetics_test_result_vitals_metrics import SyntheticsTestResultVitalsMetrics
    from datadog_api_client.v2.model.synthetics_test_result_warning import SyntheticsTestResultWarning


class SyntheticsTestResultStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_step_assertion_result import (
            SyntheticsTestResultStepAssertionResult,
        )
        from datadog_api_client.v2.model.synthetics_test_result_assertion_result import (
            SyntheticsTestResultAssertionResult,
        )
        from datadog_api_client.v2.model.synthetics_test_result_bounds import SyntheticsTestResultBounds
        from datadog_api_client.v2.model.synthetics_test_result_browser_error import SyntheticsTestResultBrowserError
        from datadog_api_client.v2.model.synthetics_test_result_bucket_keys import SyntheticsTestResultBucketKeys
        from datadog_api_client.v2.model.synthetics_test_result_cdn_resource import SyntheticsTestResultCdnResource
        from datadog_api_client.v2.model.synthetics_test_result_step_element_updates import (
            SyntheticsTestResultStepElementUpdates,
        )
        from datadog_api_client.v2.model.synthetics_test_result_variable import SyntheticsTestResultVariable
        from datadog_api_client.v2.model.synthetics_test_result_failure import SyntheticsTestResultFailure
        from datadog_api_client.v2.model.synthetics_test_result_request_info import SyntheticsTestResultRequestInfo
        from datadog_api_client.v2.model.synthetics_test_result_response_info import SyntheticsTestResultResponseInfo
        from datadog_api_client.v2.model.synthetics_test_result_rum_context import SyntheticsTestResultRumContext
        from datadog_api_client.v2.model.synthetics_test_result_sub_step import SyntheticsTestResultSubStep
        from datadog_api_client.v2.model.synthetics_test_result_sub_test import SyntheticsTestResultSubTest
        from datadog_api_client.v2.model.synthetics_test_result_tab import SyntheticsTestResultTab
        from datadog_api_client.v2.model.synthetics_test_result_variables import SyntheticsTestResultVariables
        from datadog_api_client.v2.model.synthetics_test_result_vitals_metrics import SyntheticsTestResultVitalsMetrics
        from datadog_api_client.v2.model.synthetics_test_result_warning import SyntheticsTestResultWarning

        return {
            "allow_failure": (bool,),
            "api_test": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "assertion_result": (SyntheticsTestResultStepAssertionResult,),
            "assertions": ([SyntheticsTestResultAssertionResult],),
            "blocked_requests_urls": ([str],),
            "bounds": (SyntheticsTestResultBounds,),
            "browser_errors": ([SyntheticsTestResultBrowserError],),
            "bucket_keys": (SyntheticsTestResultBucketKeys,),
            "cdn_resources": ([SyntheticsTestResultCdnResource],),
            "click_type": (str,),
            "compressed_json_descriptor": (str,),
            "config": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "description": (str,),
            "duration": (float,),
            "element_description": (str,),
            "element_updates": (SyntheticsTestResultStepElementUpdates,),
            "extracted_value": (SyntheticsTestResultVariable,),
            "failure": (SyntheticsTestResultFailure,),
            "http_results": ([SyntheticsTestResultAssertionResult],),
            "id": (str,),
            "is_critical": (bool,),
            "javascript_custom_assertion_code": (bool,),
            "locate_element_duration": (float,),
            "name": (str,),
            "request": (SyntheticsTestResultRequestInfo,),
            "response": (SyntheticsTestResultResponseInfo,),
            "retries": ([SyntheticsTestResultStep],),
            "retry_count": (int,),
            "rum_context": (SyntheticsTestResultRumContext,),
            "started_at": (int,),
            "status": (str,),
            "sub_step": (SyntheticsTestResultSubStep,),
            "sub_test": (SyntheticsTestResultSubTest,),
            "subtype": (str,),
            "tabs": ([SyntheticsTestResultTab],),
            "timings": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "tunnel": (bool,),
            "type": (str,),
            "url": (str,),
            "value": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "variables": (SyntheticsTestResultVariables,),
            "vitals_metrics": ([SyntheticsTestResultVitalsMetrics],),
            "warnings": ([SyntheticsTestResultWarning],),
        }

    attribute_map = {
        "allow_failure": "allow_failure",
        "api_test": "api_test",
        "assertion_result": "assertion_result",
        "assertions": "assertions",
        "blocked_requests_urls": "blocked_requests_urls",
        "bounds": "bounds",
        "browser_errors": "browser_errors",
        "bucket_keys": "bucket_keys",
        "cdn_resources": "cdn_resources",
        "click_type": "click_type",
        "compressed_json_descriptor": "compressed_json_descriptor",
        "config": "config",
        "description": "description",
        "duration": "duration",
        "element_description": "element_description",
        "element_updates": "element_updates",
        "extracted_value": "extracted_value",
        "failure": "failure",
        "http_results": "http_results",
        "id": "id",
        "is_critical": "is_critical",
        "javascript_custom_assertion_code": "javascript_custom_assertion_code",
        "locate_element_duration": "locate_element_duration",
        "name": "name",
        "request": "request",
        "response": "response",
        "retries": "retries",
        "retry_count": "retry_count",
        "rum_context": "rum_context",
        "started_at": "started_at",
        "status": "status",
        "sub_step": "sub_step",
        "sub_test": "sub_test",
        "subtype": "subtype",
        "tabs": "tabs",
        "timings": "timings",
        "tunnel": "tunnel",
        "type": "type",
        "url": "url",
        "value": "value",
        "variables": "variables",
        "vitals_metrics": "vitals_metrics",
        "warnings": "warnings",
    }

    def __init__(
        self_,
        allow_failure: Union[bool, UnsetType] = unset,
        api_test: Union[Dict[str, Any], UnsetType] = unset,
        assertion_result: Union[SyntheticsTestResultStepAssertionResult, UnsetType] = unset,
        assertions: Union[List[SyntheticsTestResultAssertionResult], UnsetType] = unset,
        blocked_requests_urls: Union[List[str], UnsetType] = unset,
        bounds: Union[SyntheticsTestResultBounds, UnsetType] = unset,
        browser_errors: Union[List[SyntheticsTestResultBrowserError], UnsetType] = unset,
        bucket_keys: Union[SyntheticsTestResultBucketKeys, UnsetType] = unset,
        cdn_resources: Union[List[SyntheticsTestResultCdnResource], UnsetType] = unset,
        click_type: Union[str, UnsetType] = unset,
        compressed_json_descriptor: Union[str, UnsetType] = unset,
        config: Union[Dict[str, Any], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        duration: Union[float, UnsetType] = unset,
        element_description: Union[str, UnsetType] = unset,
        element_updates: Union[SyntheticsTestResultStepElementUpdates, UnsetType] = unset,
        extracted_value: Union[SyntheticsTestResultVariable, UnsetType] = unset,
        failure: Union[SyntheticsTestResultFailure, UnsetType] = unset,
        http_results: Union[List[SyntheticsTestResultAssertionResult], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_critical: Union[bool, UnsetType] = unset,
        javascript_custom_assertion_code: Union[bool, UnsetType] = unset,
        locate_element_duration: Union[float, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        request: Union[SyntheticsTestResultRequestInfo, UnsetType] = unset,
        response: Union[SyntheticsTestResultResponseInfo, UnsetType] = unset,
        retries: Union[List[SyntheticsTestResultStep], UnsetType] = unset,
        retry_count: Union[int, UnsetType] = unset,
        rum_context: Union[SyntheticsTestResultRumContext, UnsetType] = unset,
        started_at: Union[int, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        sub_step: Union[SyntheticsTestResultSubStep, UnsetType] = unset,
        sub_test: Union[SyntheticsTestResultSubTest, UnsetType] = unset,
        subtype: Union[str, UnsetType] = unset,
        tabs: Union[List[SyntheticsTestResultTab], UnsetType] = unset,
        timings: Union[Dict[str, Any], UnsetType] = unset,
        tunnel: Union[bool, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        value: Union[Any, UnsetType] = unset,
        variables: Union[SyntheticsTestResultVariables, UnsetType] = unset,
        vitals_metrics: Union[List[SyntheticsTestResultVitalsMetrics], UnsetType] = unset,
        warnings: Union[List[SyntheticsTestResultWarning], UnsetType] = unset,
        **kwargs,
    ):
        """
        A step result from a browser, mobile, or multistep API test.

        :param allow_failure: Whether the test continues when this step fails.
        :type allow_failure: bool, optional

        :param api_test: Inner API test definition for browser ``runApiTest`` steps.
        :type api_test: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param assertion_result: Assertion result for a browser or mobile step.
        :type assertion_result: SyntheticsTestResultStepAssertionResult, optional

        :param assertions: Assertion results produced by the step.
        :type assertions: [SyntheticsTestResultAssertionResult], optional

        :param blocked_requests_urls: URLs of requests blocked during the step.
        :type blocked_requests_urls: [str], optional

        :param bounds: Bounding box of an element on the page.
        :type bounds: SyntheticsTestResultBounds, optional

        :param browser_errors: Browser errors captured during the step.
        :type browser_errors: [SyntheticsTestResultBrowserError], optional

        :param bucket_keys: Storage bucket keys for artifacts produced during a step or test.
        :type bucket_keys: SyntheticsTestResultBucketKeys, optional

        :param cdn_resources: CDN resources encountered during the step.
        :type cdn_resources: [SyntheticsTestResultCdnResource], optional

        :param click_type: Click type performed in a browser step.
        :type click_type: str, optional

        :param compressed_json_descriptor: Compressed JSON descriptor for the step (internal format).
        :type compressed_json_descriptor: str, optional

        :param config: Request configuration executed by this step (API test steps).
        :type config: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param description: Human-readable description of the step.
        :type description: str, optional

        :param duration: Duration of the step in milliseconds.
        :type duration: float, optional

        :param element_description: Description of the element interacted with by the step.
        :type element_description: str, optional

        :param element_updates: Element locator updates produced during a step.
        :type element_updates: SyntheticsTestResultStepElementUpdates, optional

        :param extracted_value: A variable used or extracted during a test.
        :type extracted_value: SyntheticsTestResultVariable, optional

        :param failure: Details about the failure of a Synthetic test.
        :type failure: SyntheticsTestResultFailure, optional

        :param http_results: HTTP results produced by an MCP step.
        :type http_results: [SyntheticsTestResultAssertionResult], optional

        :param id: Identifier of the step.
        :type id: str, optional

        :param is_critical: Whether this step is critical for the test outcome.
        :type is_critical: bool, optional

        :param javascript_custom_assertion_code: Whether the step uses a custom JavaScript assertion.
        :type javascript_custom_assertion_code: bool, optional

        :param locate_element_duration: Time taken to locate the element in milliseconds.
        :type locate_element_duration: float, optional

        :param name: Name of the step.
        :type name: str, optional

        :param request: Details of the outgoing request made during the test execution.
        :type request: SyntheticsTestResultRequestInfo, optional

        :param response: Details of the response received during the test execution.
        :type response: SyntheticsTestResultResponseInfo, optional

        :param retries: Retry results for the step.
        :type retries: [SyntheticsTestResultStep], optional

        :param retry_count: Number of times this step was retried.
        :type retry_count: int, optional

        :param rum_context: RUM application context associated with a step or sub-test.
        :type rum_context: SyntheticsTestResultRumContext, optional

        :param started_at: Unix timestamp (ms) of when the step started.
        :type started_at: int, optional

        :param status: Status of the step (for example, ``passed`` , ``failed`` ).
        :type status: str, optional

        :param sub_step: Information about a sub-step in a nested test execution.
        :type sub_step: SyntheticsTestResultSubStep, optional

        :param sub_test: Information about a sub-test played from a parent browser test.
        :type sub_test: SyntheticsTestResultSubTest, optional

        :param subtype: Subtype of the step.
        :type subtype: str, optional

        :param tabs: Browser tabs involved in the step.
        :type tabs: [SyntheticsTestResultTab], optional

        :param timings: Timing breakdown of the step execution.
        :type timings: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tunnel: Whether the step was executed through a Synthetics tunnel.
        :type tunnel: bool, optional

        :param type: Type of the step (for example, ``click`` , ``assertElementContent`` , ``runApiTest`` ).
        :type type: str, optional

        :param url: URL associated with the step (for navigation steps).
        :type url: str, optional

        :param value: Step value. Its type depends on the step type.
        :type value: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param variables: Variables captured during a test step.
        :type variables: SyntheticsTestResultVariables, optional

        :param vitals_metrics: Web vitals metrics captured during the step.
        :type vitals_metrics: [SyntheticsTestResultVitalsMetrics], optional

        :param warnings: Warnings emitted during the step.
        :type warnings: [SyntheticsTestResultWarning], optional
        """
        if allow_failure is not unset:
            kwargs["allow_failure"] = allow_failure
        if api_test is not unset:
            kwargs["api_test"] = api_test
        if assertion_result is not unset:
            kwargs["assertion_result"] = assertion_result
        if assertions is not unset:
            kwargs["assertions"] = assertions
        if blocked_requests_urls is not unset:
            kwargs["blocked_requests_urls"] = blocked_requests_urls
        if bounds is not unset:
            kwargs["bounds"] = bounds
        if browser_errors is not unset:
            kwargs["browser_errors"] = browser_errors
        if bucket_keys is not unset:
            kwargs["bucket_keys"] = bucket_keys
        if cdn_resources is not unset:
            kwargs["cdn_resources"] = cdn_resources
        if click_type is not unset:
            kwargs["click_type"] = click_type
        if compressed_json_descriptor is not unset:
            kwargs["compressed_json_descriptor"] = compressed_json_descriptor
        if config is not unset:
            kwargs["config"] = config
        if description is not unset:
            kwargs["description"] = description
        if duration is not unset:
            kwargs["duration"] = duration
        if element_description is not unset:
            kwargs["element_description"] = element_description
        if element_updates is not unset:
            kwargs["element_updates"] = element_updates
        if extracted_value is not unset:
            kwargs["extracted_value"] = extracted_value
        if failure is not unset:
            kwargs["failure"] = failure
        if http_results is not unset:
            kwargs["http_results"] = http_results
        if id is not unset:
            kwargs["id"] = id
        if is_critical is not unset:
            kwargs["is_critical"] = is_critical
        if javascript_custom_assertion_code is not unset:
            kwargs["javascript_custom_assertion_code"] = javascript_custom_assertion_code
        if locate_element_duration is not unset:
            kwargs["locate_element_duration"] = locate_element_duration
        if name is not unset:
            kwargs["name"] = name
        if request is not unset:
            kwargs["request"] = request
        if response is not unset:
            kwargs["response"] = response
        if retries is not unset:
            kwargs["retries"] = retries
        if retry_count is not unset:
            kwargs["retry_count"] = retry_count
        if rum_context is not unset:
            kwargs["rum_context"] = rum_context
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        if sub_step is not unset:
            kwargs["sub_step"] = sub_step
        if sub_test is not unset:
            kwargs["sub_test"] = sub_test
        if subtype is not unset:
            kwargs["subtype"] = subtype
        if tabs is not unset:
            kwargs["tabs"] = tabs
        if timings is not unset:
            kwargs["timings"] = timings
        if tunnel is not unset:
            kwargs["tunnel"] = tunnel
        if type is not unset:
            kwargs["type"] = type
        if url is not unset:
            kwargs["url"] = url
        if value is not unset:
            kwargs["value"] = value
        if variables is not unset:
            kwargs["variables"] = variables
        if vitals_metrics is not unset:
            kwargs["vitals_metrics"] = vitals_metrics
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)
