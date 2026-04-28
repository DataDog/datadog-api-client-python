# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.synthetics_api_multistep_subtests_response import (
    SyntheticsApiMultistepSubtestsResponse,
)
from datadog_api_client.v2.model.synthetics_api_multistep_parent_tests_response import (
    SyntheticsApiMultistepParentTestsResponse,
)
from datadog_api_client.v2.model.synthetics_downtimes_response import SyntheticsDowntimesResponse
from datadog_api_client.v2.model.synthetics_downtime_response import SyntheticsDowntimeResponse
from datadog_api_client.v2.model.synthetics_downtime_request import SyntheticsDowntimeRequest
from datadog_api_client.v2.model.on_demand_concurrency_cap_response import OnDemandConcurrencyCapResponse
from datadog_api_client.v2.model.on_demand_concurrency_cap_attributes import OnDemandConcurrencyCapAttributes
from datadog_api_client.v2.model.synthetics_suite_response import SyntheticsSuiteResponse
from datadog_api_client.v2.model.suite_create_edit_request import SuiteCreateEditRequest
from datadog_api_client.v2.model.deleted_suites_response import DeletedSuitesResponse
from datadog_api_client.v2.model.deleted_suites_request_delete_request import DeletedSuitesRequestDeleteRequest
from datadog_api_client.v2.model.synthetics_suite_search_response import SyntheticsSuiteSearchResponse
from datadog_api_client.v2.model.suite_json_patch_request import SuiteJsonPatchRequest
from datadog_api_client.v2.model.synthetics_test_latest_results_response import SyntheticsTestLatestResultsResponse
from datadog_api_client.v2.model.synthetics_test_result_status import SyntheticsTestResultStatus
from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
from datadog_api_client.v2.model.synthetics_test_result_response import SyntheticsTestResultResponse
from datadog_api_client.v2.model.deleted_tests_response import DeletedTestsResponse
from datadog_api_client.v2.model.deleted_tests_request_delete_request import DeletedTestsRequestDeleteRequest
from datadog_api_client.v2.model.synthetics_fast_test_result import SyntheticsFastTestResult
from datadog_api_client.v2.model.synthetics_network_test_response import SyntheticsNetworkTestResponse
from datadog_api_client.v2.model.synthetics_network_test_edit_request import SyntheticsNetworkTestEditRequest
from datadog_api_client.v2.model.synthetics_poll_test_results_response import SyntheticsPollTestResultsResponse
from datadog_api_client.v2.model.synthetics_test_file_download_response import SyntheticsTestFileDownloadResponse
from datadog_api_client.v2.model.synthetics_test_file_download_request import SyntheticsTestFileDownloadRequest
from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_response import (
    SyntheticsTestFileMultipartPresignedUrlsResponse,
)
from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_request import (
    SyntheticsTestFileMultipartPresignedUrlsRequest,
)
from datadog_api_client.v2.model.synthetics_test_file_abort_multipart_upload_request import (
    SyntheticsTestFileAbortMultipartUploadRequest,
)
from datadog_api_client.v2.model.synthetics_test_file_complete_multipart_upload_request import (
    SyntheticsTestFileCompleteMultipartUploadRequest,
)
from datadog_api_client.v2.model.synthetics_test_parent_suites_response import SyntheticsTestParentSuitesResponse
from datadog_api_client.v2.model.synthetics_test_version_history_response import SyntheticsTestVersionHistoryResponse
from datadog_api_client.v2.model.synthetics_test_version_response import SyntheticsTestVersionResponse
from datadog_api_client.v2.model.global_variable_response import GlobalVariableResponse
from datadog_api_client.v2.model.global_variable_json_patch_request import GlobalVariableJsonPatchRequest


class SyntheticsApi:
    """
    Synthetic tests use simulated requests and actions so you can monitor the availability and performance of systems and applications. Datadog supports the following types of synthetic tests:

    * `API tests <https://docs.datadoghq.com/synthetics/api_tests/>`_
    * `Browser tests <https://docs.datadoghq.com/synthetics/browser_tests>`_
    * `Network Path tests <https://docs.datadoghq.com/synthetics/network_path_tests/>`_
    * `Mobile Application tests <https://docs.datadoghq.com/synthetics/mobile_app_testing>`_
      You can use the Datadog API to create, manage, and organize tests and test suites programmatically.
      For more information, see the `Synthetic Monitoring documentation <https://docs.datadoghq.com/synthetics/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._abort_test_file_multipart_upload_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/files/multipart-upload-abort",
                "operation_id": "abort_test_file_multipart_upload",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsTestFileAbortMultipartUploadRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._add_test_to_synthetics_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsDowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes/{downtime_id}/tests/{test_id}",
                "operation_id": "add_test_to_synthetics_downtime",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "test_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "test_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._complete_test_file_multipart_upload_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/files/multipart-upload-complete",
                "operation_id": "complete_test_file_multipart_upload",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsTestFileCompleteMultipartUploadRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_synthetics_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsDowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes",
                "operation_id": "create_synthetics_downtime",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsDowntimeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_synthetics_network_test_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsNetworkTestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/network",
                "operation_id": "create_synthetics_network_test",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsNetworkTestEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_synthetics_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites",
                "operation_id": "create_synthetics_suite",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SuiteCreateEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_synthetics_downtime_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes/{downtime_id}",
                "operation_id": "delete_synthetics_downtime",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_synthetics_suites_endpoint = _Endpoint(
            settings={
                "response_type": (DeletedSuitesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/bulk-delete",
                "operation_id": "delete_synthetics_suites",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DeletedSuitesRequestDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_synthetics_tests_endpoint = _Endpoint(
            settings={
                "response_type": (DeletedTestsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/bulk-delete",
                "operation_id": "delete_synthetics_tests",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DeletedTestsRequestDeleteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._edit_synthetics_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/{public_id}",
                "operation_id": "edit_synthetics_suite",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SuiteCreateEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_api_multistep_subtest_parents_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsApiMultistepParentTestsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/api-multistep/subtests/{public_id}/parents",
                "operation_id": "get_api_multistep_subtest_parents",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_api_multistep_subtests_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsApiMultistepSubtestsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/api-multistep/subtests/{public_id}",
                "operation_id": "get_api_multistep_subtests",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_on_demand_concurrency_cap_endpoint = _Endpoint(
            settings={
                "response_type": (OnDemandConcurrencyCapResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/settings/on_demand_concurrency_cap",
                "operation_id": "get_on_demand_concurrency_cap",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_browser_test_result_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestResultResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/browser/{public_id}/results/{result_id}",
                "operation_id": "get_synthetics_browser_test_result",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "result_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "result_id",
                    "location": "path",
                },
                "event_id": {
                    "openapi_types": (str,),
                    "attribute": "event_id",
                    "location": "query",
                },
                "timestamp": {
                    "openapi_types": (int,),
                    "attribute": "timestamp",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsDowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes/{downtime_id}",
                "operation_id": "get_synthetics_downtime",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_fast_test_result_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsFastTestResult,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/fast/{id}",
                "operation_id": "get_synthetics_fast_test_result",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_network_test_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsNetworkTestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/network/{public_id}",
                "operation_id": "get_synthetics_network_test",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/{public_id}",
                "operation_id": "get_synthetics_suite",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_test_result_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestResultResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/results/{result_id}",
                "operation_id": "get_synthetics_test_result",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "result_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "result_id",
                    "location": "path",
                },
                "event_id": {
                    "openapi_types": (str,),
                    "attribute": "event_id",
                    "location": "query",
                },
                "timestamp": {
                    "openapi_types": (int,),
                    "attribute": "timestamp",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_synthetics_test_version_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestVersionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/version_history/{version_number}",
                "operation_id": "get_synthetics_test_version",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "version_number": {
                    "required": True,
                    "openapi_types": (int,),
                    "attribute": "version_number",
                    "location": "path",
                },
                "include_change_metadata": {
                    "openapi_types": (bool,),
                    "attribute": "include_change_metadata",
                    "location": "query",
                },
                "only_check_existence": {
                    "openapi_types": (bool,),
                    "attribute": "only_check_existence",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_test_file_download_url_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestFileDownloadResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/files/download",
                "operation_id": "get_test_file_download_url",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsTestFileDownloadRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_test_file_multipart_presigned_urls_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestFileMultipartPresignedUrlsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/files/multipart-presigned-urls",
                "operation_id": "get_test_file_multipart_presigned_urls",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsTestFileMultipartPresignedUrlsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_test_parent_suites_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestParentSuitesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/parent-suites",
                "operation_id": "get_test_parent_suites",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_synthetics_browser_test_latest_results_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestLatestResultsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/browser/{public_id}/results",
                "operation_id": "list_synthetics_browser_test_latest_results",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "from_ts": {
                    "openapi_types": (int,),
                    "attribute": "from_ts",
                    "location": "query",
                },
                "to_ts": {
                    "openapi_types": (int,),
                    "attribute": "to_ts",
                    "location": "query",
                },
                "status": {
                    "openapi_types": (SyntheticsTestResultStatus,),
                    "attribute": "status",
                    "location": "query",
                },
                "run_type": {
                    "openapi_types": (SyntheticsTestResultRunType,),
                    "attribute": "runType",
                    "location": "query",
                },
                "probe_dc": {
                    "openapi_types": ([str],),
                    "attribute": "probe_dc",
                    "location": "query",
                    "collection_format": "multi",
                },
                "device_id": {
                    "openapi_types": ([str],),
                    "attribute": "device_id",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_synthetics_downtimes_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsDowntimesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes",
                "operation_id": "list_synthetics_downtimes",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_test_ids": {
                    "openapi_types": (str,),
                    "attribute": "filter[test_ids]",
                    "location": "query",
                },
                "filter_active": {
                    "openapi_types": (str,),
                    "attribute": "filter[active]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_synthetics_test_latest_results_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestLatestResultsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/results",
                "operation_id": "list_synthetics_test_latest_results",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "from_ts": {
                    "openapi_types": (int,),
                    "attribute": "from_ts",
                    "location": "query",
                },
                "to_ts": {
                    "openapi_types": (int,),
                    "attribute": "to_ts",
                    "location": "query",
                },
                "status": {
                    "openapi_types": (SyntheticsTestResultStatus,),
                    "attribute": "status",
                    "location": "query",
                },
                "run_type": {
                    "openapi_types": (SyntheticsTestResultRunType,),
                    "attribute": "runType",
                    "location": "query",
                },
                "probe_dc": {
                    "openapi_types": ([str],),
                    "attribute": "probe_dc",
                    "location": "query",
                    "collection_format": "multi",
                },
                "device_id": {
                    "openapi_types": ([str],),
                    "attribute": "device_id",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_synthetics_test_versions_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsTestVersionHistoryResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/{public_id}/version_history",
                "operation_id": "list_synthetics_test_versions",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "last_version_number": {
                    "openapi_types": (int,),
                    "attribute": "last_version_number",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 50,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._patch_global_variable_endpoint = _Endpoint(
            settings={
                "response_type": (GlobalVariableResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/variables/{variable_id}/jsonpatch",
                "operation_id": "patch_global_variable",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "variable_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "variable_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GlobalVariableJsonPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._patch_test_suite_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/{public_id}/jsonpatch",
                "operation_id": "patch_test_suite",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SuiteJsonPatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._poll_synthetics_test_results_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsPollTestResultsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/poll_results",
                "operation_id": "poll_synthetics_test_results",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "result_ids": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "result_ids",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._remove_test_from_synthetics_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsDowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes/{downtime_id}/tests/{test_id}",
                "operation_id": "remove_test_from_synthetics_downtime",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "test_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "test_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_suites_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsSuiteSearchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/suites/search",
                "operation_id": "search_suites",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "facets_only": {
                    "openapi_types": (bool,),
                    "attribute": "facets_only",
                    "location": "query",
                },
                "start": {
                    "openapi_types": (int,),
                    "attribute": "start",
                    "location": "query",
                },
                "count": {
                    "openapi_types": (int,),
                    "attribute": "count",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._set_on_demand_concurrency_cap_endpoint = _Endpoint(
            settings={
                "response_type": (OnDemandConcurrencyCapResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/settings/on_demand_concurrency_cap",
                "operation_id": "set_on_demand_concurrency_cap",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OnDemandConcurrencyCapAttributes,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_synthetics_downtime_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsDowntimeResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/synthetics/downtimes/{downtime_id}",
                "operation_id": "update_synthetics_downtime",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "downtime_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "downtime_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsDowntimeRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_synthetics_network_test_endpoint = _Endpoint(
            settings={
                "response_type": (SyntheticsNetworkTestResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/synthetics/tests/network/{public_id}",
                "operation_id": "update_synthetics_network_test",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "public_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SyntheticsNetworkTestEditRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def abort_test_file_multipart_upload(
        self,
        public_id: str,
        body: SyntheticsTestFileAbortMultipartUploadRequest,
    ) -> None:
        """Abort a multipart upload of a test file.

        Abort an in-progress multipart file upload for a Synthetic test. This cancels the upload
        and releases any storage used by already-uploaded parts.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :type body: SyntheticsTestFileAbortMultipartUploadRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._abort_test_file_multipart_upload_endpoint.call_with_http_info(**kwargs)

    def add_test_to_synthetics_downtime(
        self,
        downtime_id: str,
        test_id: str,
    ) -> SyntheticsDowntimeResponse:
        """Add a test to a Synthetics downtime.

        Associate a Synthetics test with a downtime.

        :param downtime_id: The ID of the downtime.
        :type downtime_id: str
        :param test_id: The public ID of the Synthetics test to associate with the downtime.
        :type test_id: str
        :rtype: SyntheticsDowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        kwargs["test_id"] = test_id

        return self._add_test_to_synthetics_downtime_endpoint.call_with_http_info(**kwargs)

    def complete_test_file_multipart_upload(
        self,
        public_id: str,
        body: SyntheticsTestFileCompleteMultipartUploadRequest,
    ) -> None:
        """Complete a multipart upload of a test file.

        Complete a multipart file upload for a Synthetic test. Call this endpoint after all parts
        have been uploaded using the presigned URLs obtained from the multipart presigned URLs endpoint.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :type body: SyntheticsTestFileCompleteMultipartUploadRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._complete_test_file_multipart_upload_endpoint.call_with_http_info(**kwargs)

    def create_synthetics_downtime(
        self,
        body: SyntheticsDowntimeRequest,
    ) -> SyntheticsDowntimeResponse:
        """Create a Synthetics downtime.

        Create a new Synthetics downtime.

        :type body: SyntheticsDowntimeRequest
        :rtype: SyntheticsDowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_synthetics_downtime_endpoint.call_with_http_info(**kwargs)

    def create_synthetics_network_test(
        self,
        body: SyntheticsNetworkTestEditRequest,
    ) -> SyntheticsNetworkTestResponse:
        """Create a Network Path test.

        :type body: SyntheticsNetworkTestEditRequest
        :rtype: SyntheticsNetworkTestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_synthetics_network_test_endpoint.call_with_http_info(**kwargs)

    def create_synthetics_suite(
        self,
        body: SuiteCreateEditRequest,
    ) -> SyntheticsSuiteResponse:
        """Create a test suite.

        :type body: SuiteCreateEditRequest
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_synthetics_suite_endpoint.call_with_http_info(**kwargs)

    def delete_synthetics_downtime(
        self,
        downtime_id: str,
    ) -> None:
        """Delete a Synthetics downtime.

        Delete a Synthetics downtime by its ID.

        :param downtime_id: The ID of the downtime to delete.
        :type downtime_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        return self._delete_synthetics_downtime_endpoint.call_with_http_info(**kwargs)

    def delete_synthetics_suites(
        self,
        body: DeletedSuitesRequestDeleteRequest,
    ) -> DeletedSuitesResponse:
        """Bulk delete suites.

        :type body: DeletedSuitesRequestDeleteRequest
        :rtype: DeletedSuitesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_synthetics_suites_endpoint.call_with_http_info(**kwargs)

    def delete_synthetics_tests(
        self,
        body: DeletedTestsRequestDeleteRequest,
    ) -> DeletedTestsResponse:
        """Bulk delete tests.

        :type body: DeletedTestsRequestDeleteRequest
        :rtype: DeletedTestsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._delete_synthetics_tests_endpoint.call_with_http_info(**kwargs)

    def edit_synthetics_suite(
        self,
        public_id: str,
        body: SuiteCreateEditRequest,
    ) -> SyntheticsSuiteResponse:
        """Edit a test suite.

        :param public_id: The public ID of the suite to edit.
        :type public_id: str
        :param body: New suite details to be saved.
        :type body: SuiteCreateEditRequest
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._edit_synthetics_suite_endpoint.call_with_http_info(**kwargs)

    def get_api_multistep_subtest_parents(
        self,
        public_id: str,
    ) -> SyntheticsApiMultistepParentTestsResponse:
        """Get parent tests for a subtest.

        Get the list of API multistep tests that include a given subtest,
        along with their monitor status.

        :param public_id: The public ID of the subtest.
        :type public_id: str
        :rtype: SyntheticsApiMultistepParentTestsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        return self._get_api_multistep_subtest_parents_endpoint.call_with_http_info(**kwargs)

    def get_api_multistep_subtests(
        self,
        public_id: str,
    ) -> SyntheticsApiMultistepSubtestsResponse:
        """Get available subtests for a multistep test.

        Get the list of API tests that can be added as subtests to a given API multistep test.
        The current test is excluded from the list since a test cannot be a subtest of itself.

        :param public_id: The public ID of the API multistep test.
        :type public_id: str
        :rtype: SyntheticsApiMultistepSubtestsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        return self._get_api_multistep_subtests_endpoint.call_with_http_info(**kwargs)

    def get_on_demand_concurrency_cap(
        self,
    ) -> OnDemandConcurrencyCapResponse:
        """Get the on-demand concurrency cap.

        Get the on-demand concurrency cap.

        :rtype: OnDemandConcurrencyCapResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_on_demand_concurrency_cap_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_browser_test_result(
        self,
        public_id: str,
        result_id: str,
        *,
        event_id: Union[str, UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
    ) -> SyntheticsTestResultResponse:
        """Get a browser test result.

        Get a specific full result from a given Synthetic browser test.

        :param public_id: The public ID of the Synthetic browser test to which the target result belongs.
        :type public_id: str
        :param result_id: The ID of the result to get.
        :type result_id: str
        :param event_id: The event ID used to look up the result in the event store.
        :type event_id: str, optional
        :param timestamp: Timestamp in seconds to look up the result.
        :type timestamp: int, optional
        :rtype: SyntheticsTestResultResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["result_id"] = result_id

        if event_id is not unset:
            kwargs["event_id"] = event_id

        if timestamp is not unset:
            kwargs["timestamp"] = timestamp

        return self._get_synthetics_browser_test_result_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_downtime(
        self,
        downtime_id: str,
    ) -> SyntheticsDowntimeResponse:
        """Get a Synthetics downtime.

        Get a Synthetics downtime by its ID.

        :param downtime_id: The ID of the downtime to retrieve.
        :type downtime_id: str
        :rtype: SyntheticsDowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        return self._get_synthetics_downtime_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_fast_test_result(
        self,
        id: str,
    ) -> SyntheticsFastTestResult:
        """Get a fast test result.

        :param id: The UUID of the fast test to retrieve the result for.
        :type id: str
        :rtype: SyntheticsFastTestResult
        """
        kwargs: Dict[str, Any] = {}
        kwargs["id"] = id

        return self._get_synthetics_fast_test_result_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_network_test(
        self,
        public_id: str,
    ) -> SyntheticsNetworkTestResponse:
        """Get a Network Path test.

        :param public_id: The public ID of the Network Path test to get details from.
        :type public_id: str
        :rtype: SyntheticsNetworkTestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        return self._get_synthetics_network_test_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_suite(
        self,
        public_id: str,
    ) -> SyntheticsSuiteResponse:
        """Get a suite.

        :param public_id: The public ID of the suite to get details from.
        :type public_id: str
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        return self._get_synthetics_suite_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_test_result(
        self,
        public_id: str,
        result_id: str,
        *,
        event_id: Union[str, UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
    ) -> SyntheticsTestResultResponse:
        """Get a test result.

        Get a specific full result from a given Synthetic test.

        :param public_id: The public ID of the Synthetic test to which the target result belongs.
        :type public_id: str
        :param result_id: The ID of the result to get.
        :type result_id: str
        :param event_id: The event ID used to look up the result in the event store.
        :type event_id: str, optional
        :param timestamp: Timestamp in seconds to look up the result.
        :type timestamp: int, optional
        :rtype: SyntheticsTestResultResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["result_id"] = result_id

        if event_id is not unset:
            kwargs["event_id"] = event_id

        if timestamp is not unset:
            kwargs["timestamp"] = timestamp

        return self._get_synthetics_test_result_endpoint.call_with_http_info(**kwargs)

    def get_synthetics_test_version(
        self,
        public_id: str,
        version_number: int,
        *,
        include_change_metadata: Union[bool, UnsetType] = unset,
        only_check_existence: Union[bool, UnsetType] = unset,
    ) -> SyntheticsTestVersionResponse:
        """Get a specific version of a test.

        Get a specific version of a Synthetic test by its version number.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :param version_number: The version number to retrieve.
        :type version_number: int
        :param include_change_metadata: If ``true`` , include change metadata in the response.
        :type include_change_metadata: bool, optional
        :param only_check_existence: If ``true`` , only check whether the version exists without returning its full payload.
            Returns an empty object if the version exists, or 404 if not.
        :type only_check_existence: bool, optional
        :rtype: SyntheticsTestVersionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["version_number"] = version_number

        if include_change_metadata is not unset:
            kwargs["include_change_metadata"] = include_change_metadata

        if only_check_existence is not unset:
            kwargs["only_check_existence"] = only_check_existence

        return self._get_synthetics_test_version_endpoint.call_with_http_info(**kwargs)

    def get_test_file_download_url(
        self,
        public_id: str,
        body: SyntheticsTestFileDownloadRequest,
    ) -> SyntheticsTestFileDownloadResponse:
        """Get a presigned URL for downloading a test file.

        Get a presigned URL to download a file attached to a Synthetic test.
        The returned URL is temporary and expires after a short period.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :type body: SyntheticsTestFileDownloadRequest
        :rtype: SyntheticsTestFileDownloadResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._get_test_file_download_url_endpoint.call_with_http_info(**kwargs)

    def get_test_file_multipart_presigned_urls(
        self,
        public_id: str,
        body: SyntheticsTestFileMultipartPresignedUrlsRequest,
    ) -> SyntheticsTestFileMultipartPresignedUrlsResponse:
        """Get presigned URLs for uploading a test file.

        Get presigned URLs for uploading a file to a Synthetic test using multipart upload.
        Returns the presigned URLs for each part along with the bucket key that references the file.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :type body: SyntheticsTestFileMultipartPresignedUrlsRequest
        :rtype: SyntheticsTestFileMultipartPresignedUrlsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._get_test_file_multipart_presigned_urls_endpoint.call_with_http_info(**kwargs)

    def get_test_parent_suites(
        self,
        public_id: str,
    ) -> SyntheticsTestParentSuitesResponse:
        """Get parent suites for a test.

        Get the list of parent suites and their status for a given Synthetic test.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :rtype: SyntheticsTestParentSuitesResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        return self._get_test_parent_suites_endpoint.call_with_http_info(**kwargs)

    def list_synthetics_browser_test_latest_results(
        self,
        public_id: str,
        *,
        from_ts: Union[int, UnsetType] = unset,
        to_ts: Union[int, UnsetType] = unset,
        status: Union[SyntheticsTestResultStatus, UnsetType] = unset,
        run_type: Union[SyntheticsTestResultRunType, UnsetType] = unset,
        probe_dc: Union[List[str], UnsetType] = unset,
        device_id: Union[List[str], UnsetType] = unset,
    ) -> SyntheticsTestLatestResultsResponse:
        """Get a browser test's latest results.

        Get the latest result summaries for a given Synthetic browser test.

        :param public_id: The public ID of the Synthetic browser test for which to search results.
        :type public_id: str
        :param from_ts: Timestamp in milliseconds from which to start querying results.
        :type from_ts: int, optional
        :param to_ts: Timestamp in milliseconds up to which to query results.
        :type to_ts: int, optional
        :param status: Filter results by status.
        :type status: SyntheticsTestResultStatus, optional
        :param run_type: Filter results by run type.
        :type run_type: SyntheticsTestResultRunType, optional
        :param probe_dc: Locations for which to query results.
        :type probe_dc: [str], optional
        :param device_id: Device IDs for which to query results.
        :type device_id: [str], optional
        :rtype: SyntheticsTestLatestResultsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        if from_ts is not unset:
            kwargs["from_ts"] = from_ts

        if to_ts is not unset:
            kwargs["to_ts"] = to_ts

        if status is not unset:
            kwargs["status"] = status

        if run_type is not unset:
            kwargs["run_type"] = run_type

        if probe_dc is not unset:
            kwargs["probe_dc"] = probe_dc

        if device_id is not unset:
            kwargs["device_id"] = device_id

        return self._list_synthetics_browser_test_latest_results_endpoint.call_with_http_info(**kwargs)

    def list_synthetics_downtimes(
        self,
        *,
        filter_test_ids: Union[str, UnsetType] = unset,
        filter_active: Union[str, UnsetType] = unset,
    ) -> SyntheticsDowntimesResponse:
        """List Synthetics downtimes.

        Get a list of all Synthetics downtimes for your organization.

        :param filter_test_ids: Comma-separated list of Synthetics test public IDs to filter downtimes by.
        :type filter_test_ids: str, optional
        :param filter_active: If set to ``true`` , return only downtimes that are currently active.
        :type filter_active: str, optional
        :rtype: SyntheticsDowntimesResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_test_ids is not unset:
            kwargs["filter_test_ids"] = filter_test_ids

        if filter_active is not unset:
            kwargs["filter_active"] = filter_active

        return self._list_synthetics_downtimes_endpoint.call_with_http_info(**kwargs)

    def list_synthetics_test_latest_results(
        self,
        public_id: str,
        *,
        from_ts: Union[int, UnsetType] = unset,
        to_ts: Union[int, UnsetType] = unset,
        status: Union[SyntheticsTestResultStatus, UnsetType] = unset,
        run_type: Union[SyntheticsTestResultRunType, UnsetType] = unset,
        probe_dc: Union[List[str], UnsetType] = unset,
        device_id: Union[List[str], UnsetType] = unset,
    ) -> SyntheticsTestLatestResultsResponse:
        """Get a test's latest results.

        Get the latest result summaries for a given Synthetic test.

        :param public_id: The public ID of the Synthetic test for which to search results.
        :type public_id: str
        :param from_ts: Timestamp in milliseconds from which to start querying results.
        :type from_ts: int, optional
        :param to_ts: Timestamp in milliseconds up to which to query results.
        :type to_ts: int, optional
        :param status: Filter results by status.
        :type status: SyntheticsTestResultStatus, optional
        :param run_type: Filter results by run type.
        :type run_type: SyntheticsTestResultRunType, optional
        :param probe_dc: Locations for which to query results.
        :type probe_dc: [str], optional
        :param device_id: Device IDs for which to query results.
        :type device_id: [str], optional
        :rtype: SyntheticsTestLatestResultsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        if from_ts is not unset:
            kwargs["from_ts"] = from_ts

        if to_ts is not unset:
            kwargs["to_ts"] = to_ts

        if status is not unset:
            kwargs["status"] = status

        if run_type is not unset:
            kwargs["run_type"] = run_type

        if probe_dc is not unset:
            kwargs["probe_dc"] = probe_dc

        if device_id is not unset:
            kwargs["device_id"] = device_id

        return self._list_synthetics_test_latest_results_endpoint.call_with_http_info(**kwargs)

    def list_synthetics_test_versions(
        self,
        public_id: str,
        *,
        last_version_number: Union[int, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
    ) -> SyntheticsTestVersionHistoryResponse:
        """Get version history of a test.

        Get the paginated version history for a Synthetic test.

        :param public_id: The public ID of the Synthetic test.
        :type public_id: str
        :param last_version_number: The version number of the last item from the previous page. Omit to get the first page.
        :type last_version_number: int, optional
        :param limit: Maximum number of version records to return per page.
        :type limit: int, optional
        :rtype: SyntheticsTestVersionHistoryResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        if last_version_number is not unset:
            kwargs["last_version_number"] = last_version_number

        if limit is not unset:
            kwargs["limit"] = limit

        return self._list_synthetics_test_versions_endpoint.call_with_http_info(**kwargs)

    def patch_global_variable(
        self,
        variable_id: str,
        body: GlobalVariableJsonPatchRequest,
    ) -> GlobalVariableResponse:
        """Patch a global variable.

        Patch a global variable using JSON Patch (RFC 6902).
        This endpoint allows partial updates to a global variable by specifying only the fields to modify.

        Common operations include:

        * Replace field values: ``{"op": "replace", "path": "/name", "value": "new_name"}``
        * Update nested values: ``{"op": "replace", "path": "/value/value", "value": "new_value"}``
        * Add/update tags: ``{"op": "add", "path": "/tags/-", "value": "new_tag"}``
        * Remove fields: ``{"op": "remove", "path": "/description"}``

        :param variable_id: The ID of the global variable.
        :type variable_id: str
        :param body: JSON Patch document with operations to apply.
        :type body: GlobalVariableJsonPatchRequest
        :rtype: GlobalVariableResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["variable_id"] = variable_id

        kwargs["body"] = body

        return self._patch_global_variable_endpoint.call_with_http_info(**kwargs)

    def patch_test_suite(
        self,
        public_id: str,
        body: SuiteJsonPatchRequest,
    ) -> SyntheticsSuiteResponse:
        """Patch a test suite.

        Patch a Synthetic test suite using JSON Patch (RFC 6902).
        Use partial updates to modify only specific fields of a test suite.

        Common operations include:

        * Replace field values: ``{"op": "replace", "path": "/name", "value": "new_name"}``
        * Add/update tags: ``{"op": "add", "path": "/tags/-", "value": "new_tag"}``
        * Remove fields: ``{"op": "remove", "path": "/message"}``

        :param public_id: The public ID of the Synthetic test suite to patch.
        :type public_id: str
        :param body: JSON Patch document with operations to apply.
        :type body: SuiteJsonPatchRequest
        :rtype: SyntheticsSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._patch_test_suite_endpoint.call_with_http_info(**kwargs)

    def poll_synthetics_test_results(
        self,
        result_ids: str,
    ) -> SyntheticsPollTestResultsResponse:
        """Poll for test results.

        Poll for test results given a list of result IDs. This is typically used after
        triggering tests with CI/CD to retrieve results once they are available.

        :param result_ids: A JSON-encoded array of result IDs to poll for.
        :type result_ids: str
        :rtype: SyntheticsPollTestResultsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["result_ids"] = result_ids

        return self._poll_synthetics_test_results_endpoint.call_with_http_info(**kwargs)

    def remove_test_from_synthetics_downtime(
        self,
        downtime_id: str,
        test_id: str,
    ) -> SyntheticsDowntimeResponse:
        """Remove a test from a Synthetics downtime.

        Disassociate a Synthetics test from a downtime.

        :param downtime_id: The ID of the downtime.
        :type downtime_id: str
        :param test_id: The public ID of the Synthetics test to disassociate from the downtime.
        :type test_id: str
        :rtype: SyntheticsDowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        kwargs["test_id"] = test_id

        return self._remove_test_from_synthetics_downtime_endpoint.call_with_http_info(**kwargs)

    def search_suites(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        facets_only: Union[bool, UnsetType] = unset,
        start: Union[int, UnsetType] = unset,
        count: Union[int, UnsetType] = unset,
    ) -> SyntheticsSuiteSearchResponse:
        """Search test suites.

        Search for test suites.

        :param query: The search query.
        :type query: str, optional
        :param sort: The sort order for the results (e.g., ``name,asc`` or ``name,desc`` ).
        :type sort: str, optional
        :param facets_only: If true, return only facets instead of full test details.
        :type facets_only: bool, optional
        :param start: The offset from which to start returning results.
        :type start: int, optional
        :param count: The maximum number of results to return.
        :type count: int, optional
        :rtype: SyntheticsSuiteSearchResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if sort is not unset:
            kwargs["sort"] = sort

        if facets_only is not unset:
            kwargs["facets_only"] = facets_only

        if start is not unset:
            kwargs["start"] = start

        if count is not unset:
            kwargs["count"] = count

        return self._search_suites_endpoint.call_with_http_info(**kwargs)

    def set_on_demand_concurrency_cap(
        self,
        body: OnDemandConcurrencyCapAttributes,
    ) -> OnDemandConcurrencyCapResponse:
        """Save new value for on-demand concurrency cap.

        Save new value for on-demand concurrency cap.

        :param body: .
        :type body: OnDemandConcurrencyCapAttributes
        :rtype: OnDemandConcurrencyCapResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._set_on_demand_concurrency_cap_endpoint.call_with_http_info(**kwargs)

    def update_synthetics_downtime(
        self,
        downtime_id: str,
        body: SyntheticsDowntimeRequest,
    ) -> SyntheticsDowntimeResponse:
        """Update a Synthetics downtime.

        Update a Synthetics downtime by its ID.

        :param downtime_id: The ID of the downtime to update.
        :type downtime_id: str
        :type body: SyntheticsDowntimeRequest
        :rtype: SyntheticsDowntimeResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["downtime_id"] = downtime_id

        kwargs["body"] = body

        return self._update_synthetics_downtime_endpoint.call_with_http_info(**kwargs)

    def update_synthetics_network_test(
        self,
        public_id: str,
        body: SyntheticsNetworkTestEditRequest,
    ) -> SyntheticsNetworkTestResponse:
        """Edit a Network Path test.

        :param public_id: The public ID of the Network Path test to edit.
        :type public_id: str
        :param body: New Network Path test details to be saved.
        :type body: SyntheticsNetworkTestEditRequest
        :rtype: SyntheticsNetworkTestResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_id"] = public_id

        kwargs["body"] = body

        return self._update_synthetics_network_test_endpoint.call_with_http_info(**kwargs)
