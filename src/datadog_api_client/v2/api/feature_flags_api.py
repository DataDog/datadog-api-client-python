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
    UUID,
)
from datadog_api_client.v2.model.list_feature_flags_response import ListFeatureFlagsResponse
from datadog_api_client.v2.model.feature_flag_production_status import FeatureFlagProductionStatus
from datadog_api_client.v2.model.feature_flag_distribution_channel import FeatureFlagDistributionChannel
from datadog_api_client.v2.model.value_type import ValueType
from datadog_api_client.v2.model.feature_flag_staleness_status import FeatureFlagStalenessStatus
from datadog_api_client.v2.model.feature_flag_response import FeatureFlagResponse
from datadog_api_client.v2.model.create_feature_flag_request import CreateFeatureFlagRequest
from datadog_api_client.v2.model.list_environments_response import ListEnvironmentsResponse
from datadog_api_client.v2.model.environment_response import EnvironmentResponse
from datadog_api_client.v2.model.create_environment_request import CreateEnvironmentRequest
from datadog_api_client.v2.model.update_environment_request import UpdateEnvironmentRequest
from datadog_api_client.v2.model.allocation_exposure_schedule_response import AllocationExposureScheduleResponse
from datadog_api_client.v2.model.saved_filter_response import SavedFilterResponse
from datadog_api_client.v2.model.patch_saved_filter_request import PatchSavedFilterRequest
from datadog_api_client.v2.model.update_feature_flag_request import UpdateFeatureFlagRequest
from datadog_api_client.v2.model.allocation_response import AllocationResponse
from datadog_api_client.v2.model.create_allocations_request import CreateAllocationsRequest
from datadog_api_client.v2.model.list_allocations_response import ListAllocationsResponse
from datadog_api_client.v2.model.overwrite_allocations_request import OverwriteAllocationsRequest
from datadog_api_client.v2.model.variant_response import VariantResponse
from datadog_api_client.v2.model.create_variant_request import CreateVariantRequest
from datadog_api_client.v2.model.update_variant_request import UpdateVariantRequest


class FeatureFlagsApi:
    """
    Manage feature flags and environments.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._archive_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": (FeatureFlagResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/archive",
                "operation_id": "archive_feature_flag",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_allocations_for_feature_flag_in_environment_endpoint = _Endpoint(
            settings={
                "response_type": (AllocationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/environments/{environment_id}/allocations",
                "operation_id": "create_allocations_for_feature_flag_in_environment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateAllocationsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": (FeatureFlagResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags",
                "operation_id": "create_feature_flag",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateFeatureFlagRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_feature_flags_environment_endpoint = _Endpoint(
            settings={
                "response_type": (EnvironmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/environments",
                "operation_id": "create_feature_flags_environment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateEnvironmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_variant_for_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": (VariantResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/variants",
                "operation_id": "create_variant_for_feature_flag",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (CreateVariantRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_feature_flags_environment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/environments/{environment_id}",
                "operation_id": "delete_feature_flags_environment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_variant_from_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/variants/{variant_id}",
                "operation_id": "delete_variant_from_feature_flag",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "variant_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "variant_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._disable_feature_flag_environment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/environments/{environment_id}/disable",
                "operation_id": "disable_feature_flag_environment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._enable_feature_flag_environment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/environments/{environment_id}/enable",
                "operation_id": "enable_feature_flag_environment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": (FeatureFlagResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}",
                "operation_id": "get_feature_flag",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_feature_flags_environment_endpoint = _Endpoint(
            settings={
                "response_type": (EnvironmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/environments/{environment_id}",
                "operation_id": "get_feature_flags_environment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_saved_filter_endpoint = _Endpoint(
            settings={
                "response_type": (SavedFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/saved-filters/{saved_filter_id}",
                "operation_id": "get_saved_filter",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "saved_filter_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "saved_filter_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_feature_flags_endpoint = _Endpoint(
            settings={
                "response_type": (ListFeatureFlagsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags",
                "operation_id": "list_feature_flags",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "key": {
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "query",
                },
                "is_archived": {
                    "openapi_types": (bool,),
                    "attribute": "is_archived",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
                "tags": {
                    "openapi_types": ([str],),
                    "attribute": "tags",
                    "location": "query",
                    "collection_format": "multi",
                },
                "teams": {
                    "openapi_types": ([str],),
                    "attribute": "teams",
                    "location": "query",
                    "collection_format": "multi",
                },
                "production_status": {
                    "openapi_types": ([FeatureFlagProductionStatus],),
                    "attribute": "production_status",
                    "location": "query",
                    "collection_format": "multi",
                },
                "distribution_channel": {
                    "openapi_types": (FeatureFlagDistributionChannel,),
                    "attribute": "distribution_channel",
                    "location": "query",
                },
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
                    "location": "query",
                },
                "value_type": {
                    "openapi_types": ([ValueType],),
                    "attribute": "value_type",
                    "location": "query",
                    "collection_format": "multi",
                },
                "created_by": {
                    "openapi_types": ([UUID],),
                    "attribute": "created_by",
                    "location": "query",
                    "collection_format": "multi",
                },
                "flag_ids": {
                    "openapi_types": ([UUID],),
                    "attribute": "flag_ids",
                    "location": "query",
                    "collection_format": "multi",
                },
                "staleness_status": {
                    "openapi_types": (FeatureFlagStalenessStatus,),
                    "attribute": "staleness_status",
                    "location": "query",
                },
                "saved_filter_id": {
                    "openapi_types": (UUID,),
                    "attribute": "saved_filter_id",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 50,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_feature_flags_environments_endpoint = _Endpoint(
            settings={
                "response_type": (ListEnvironmentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/environments",
                "operation_id": "list_feature_flags_environments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "name": {
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "query",
                },
                "key": {
                    "openapi_types": (str,),
                    "attribute": "key",
                    "location": "query",
                },
                "dd_env": {
                    "openapi_types": (str,),
                    "attribute": "dd_env",
                    "location": "query",
                },
                "limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "limit",
                    "location": "query",
                },
                "offset": {
                    "validation": {
                        "inclusive_minimum": 0,
                    },
                    "openapi_types": (int,),
                    "attribute": "offset",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._pause_exposure_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (AllocationExposureScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/exposure-schedules/{exposure_schedule_id}/pause",
                "operation_id": "pause_exposure_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "exposure_schedule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._resume_exposure_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (AllocationExposureScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/exposure-schedules/{exposure_schedule_id}/resume",
                "operation_id": "resume_exposure_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "exposure_schedule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._start_exposure_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (AllocationExposureScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/exposure-schedules/{exposure_schedule_id}/start",
                "operation_id": "start_exposure_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "exposure_schedule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._stop_exposure_schedule_endpoint = _Endpoint(
            settings={
                "response_type": (AllocationExposureScheduleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/exposure-schedules/{exposure_schedule_id}/stop",
                "operation_id": "stop_exposure_schedule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "exposure_schedule_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_schedule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._unarchive_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": (FeatureFlagResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/unarchive",
                "operation_id": "unarchive_feature_flag",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_allocations_for_feature_flag_in_environment_endpoint = _Endpoint(
            settings={
                "response_type": (ListAllocationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/environments/{environment_id}/allocations",
                "operation_id": "update_allocations_for_feature_flag_in_environment",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (OverwriteAllocationsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": (FeatureFlagResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}",
                "operation_id": "update_feature_flag",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateFeatureFlagRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_feature_flags_environment_endpoint = _Endpoint(
            settings={
                "response_type": (EnvironmentResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/environments/{environment_id}",
                "operation_id": "update_feature_flags_environment",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "environment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "environment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateEnvironmentRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_saved_filter_attributes_endpoint = _Endpoint(
            settings={
                "response_type": (SavedFilterResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/saved-filters/{saved_filter_id}",
                "operation_id": "update_saved_filter_attributes",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "saved_filter_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "saved_filter_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PatchSavedFilterRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_variant_for_feature_flag_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/feature-flags/{feature_flag_id}/variants/{variant_id}",
                "operation_id": "update_variant_for_feature_flag",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "feature_flag_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "feature_flag_id",
                    "location": "path",
                },
                "variant_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "variant_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateVariantRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def archive_feature_flag(
        self,
        feature_flag_id: UUID,
    ) -> FeatureFlagResponse:
        """Archive a feature flag.

        Archives a feature flag. Archived flags are
        hidden from the main list but remain accessible and can be unarchived.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :rtype: FeatureFlagResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        return self._archive_feature_flag_endpoint.call_with_http_info(**kwargs)

    def create_allocations_for_feature_flag_in_environment(
        self,
        feature_flag_id: UUID,
        environment_id: UUID,
        body: CreateAllocationsRequest,
    ) -> AllocationResponse:
        """Create targeting rules for a flag env.

        Creates a new targeting rule (allocation) for a specific feature flag in a specific environment.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :type body: CreateAllocationsRequest
        :rtype: AllocationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["environment_id"] = environment_id

        kwargs["body"] = body

        return self._create_allocations_for_feature_flag_in_environment_endpoint.call_with_http_info(**kwargs)

    def create_feature_flag(
        self,
        body: CreateFeatureFlagRequest,
    ) -> FeatureFlagResponse:
        """Create a feature flag.

        Creates a new feature flag with variants.

        :type body: CreateFeatureFlagRequest
        :rtype: FeatureFlagResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_feature_flag_endpoint.call_with_http_info(**kwargs)

    def create_feature_flags_environment(
        self,
        body: CreateEnvironmentRequest,
    ) -> EnvironmentResponse:
        """Create an environment.

        Creates a new environment for organizing feature flags.

        :type body: CreateEnvironmentRequest
        :rtype: EnvironmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_feature_flags_environment_endpoint.call_with_http_info(**kwargs)

    def create_variant_for_feature_flag(
        self,
        feature_flag_id: UUID,
        body: CreateVariantRequest,
    ) -> VariantResponse:
        """Add a variant to a feature flag.

        Adds a single new variant to an existing feature flag. This endpoint is
        additive-only: it never modifies existing variants. A request whose ``key``
        already exists on the flag is rejected with ``409 Conflict`` ; a ``value``
        whose type does not match the flag's ``value_type`` is rejected with ``400``.
        The server generates the variant UUID and returns it in the response body;
        callers (for example, the flag-migration tool) need this UUID to reference
        the new variant in subsequent allocation syncs.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :type body: CreateVariantRequest
        :rtype: VariantResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["body"] = body

        return self._create_variant_for_feature_flag_endpoint.call_with_http_info(**kwargs)

    def delete_feature_flags_environment(
        self,
        environment_id: UUID,
    ) -> None:
        """Delete an environment.

        Deletes an environment. This operation cannot be undone.

        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_id"] = environment_id

        return self._delete_feature_flags_environment_endpoint.call_with_http_info(**kwargs)

    def delete_variant_from_feature_flag(
        self,
        feature_flag_id: UUID,
        variant_id: UUID,
    ) -> None:
        """Delete a variant.

        Deletes a variant from a feature flag.

        When backend approvals are enabled and the flag requires approval, this endpoint creates and returns a ``FlagSuggestion`` with ``201 Created`` instead of deleting the variant immediately. If a pending suggestion already exists for this flag's variant property, the endpoint returns ``409 Conflict``.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :param variant_id: The ID of the variant.
        :type variant_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["variant_id"] = variant_id

        return self._delete_variant_from_feature_flag_endpoint.call_with_http_info(**kwargs)

    def disable_feature_flag_environment(
        self,
        feature_flag_id: UUID,
        environment_id: UUID,
    ) -> None:
        """Disable a feature flag in an environment.

        Disable a feature flag in a specific environment.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["environment_id"] = environment_id

        return self._disable_feature_flag_environment_endpoint.call_with_http_info(**kwargs)

    def enable_feature_flag_environment(
        self,
        feature_flag_id: UUID,
        environment_id: UUID,
    ) -> None:
        """Enable a feature flag in an environment.

        Enable a feature flag in a specific environment.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["environment_id"] = environment_id

        return self._enable_feature_flag_environment_endpoint.call_with_http_info(**kwargs)

    def get_feature_flag(
        self,
        feature_flag_id: UUID,
    ) -> FeatureFlagResponse:
        """Get a feature flag.

        Returns the details of a specific feature flag
        including variants and environment status.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :rtype: FeatureFlagResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        return self._get_feature_flag_endpoint.call_with_http_info(**kwargs)

    def get_feature_flags_environment(
        self,
        environment_id: UUID,
    ) -> EnvironmentResponse:
        """Get an environment.

        Returns the details of a specific environment.

        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :rtype: EnvironmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_id"] = environment_id

        return self._get_feature_flags_environment_endpoint.call_with_http_info(**kwargs)

    def get_saved_filter(
        self,
        saved_filter_id: UUID,
    ) -> SavedFilterResponse:
        """Get a saved filter.

        Returns a saved filter by ID, including its full targeting rules, conditions, and values.
        Supports both saved lists and saved rules. Targeting rules are combined with OR,
        and conditions within each rule are combined with AND.
        Returns the stored filter definition rather than evaluating it against users or organizations.
        Archived filters can be retrieved. Filters that are deleted or belong to another organization return a not found error.

        :param saved_filter_id: The ID of the saved filter.
        :type saved_filter_id: UUID
        :rtype: SavedFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["saved_filter_id"] = saved_filter_id

        return self._get_saved_filter_endpoint.call_with_http_info(**kwargs)

    def list_feature_flags(
        self,
        *,
        key: Union[str, UnsetType] = unset,
        is_archived: Union[bool, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        production_status: Union[List[FeatureFlagProductionStatus], UnsetType] = unset,
        distribution_channel: Union[FeatureFlagDistributionChannel, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        value_type: Union[List[ValueType], UnsetType] = unset,
        created_by: Union[List[UUID], UnsetType] = unset,
        flag_ids: Union[List[UUID], UnsetType] = unset,
        staleness_status: Union[FeatureFlagStalenessStatus, UnsetType] = unset,
        saved_filter_id: Union[UUID, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
    ) -> ListFeatureFlagsResponse:
        """List feature flags.

        Returns a paginated list of feature flags for the organization.
        Supports filtering by key, tags, teams, SDK availability, production status, and other flag properties.
        Use ``page[limit]`` and ``page[offset]`` to paginate, or follow the ``next`` link in the response.

        :param key: Filter feature flags by an exact, case-sensitive key. Use ``search`` for partial matching.
        :type key: str, optional
        :param is_archived: Filter by archived status. If ``true`` , return only archived flags. If ``false`` , return only flags that are not archived. If omitted, return both.
        :type is_archived: bool, optional
        :param limit: Deprecated alias for ``page[limit]``. Use ``page[limit]`` for new requests. Used only when ``page[limit]`` is absent. When both parameters are omitted, the server defaults to ``25``. Values that exceed ``50`` are set to ``50`` ; non-positive or empty values use the server default.
        :type limit: int, optional
        :param offset: Deprecated alias for ``page[offset]``. Used only when ``page[offset]`` is absent. Defaults to ``0``. Negative or empty values are set to ``0``.
        :type offset: int, optional
        :param tags: Filter by exact tag values using repeated parameters, such as ``tags=env:prod&tags=purpose:sitemap``. A flag must have all ordinary tags. Values of the form ``team:<handle>`` match any selected team and are combined with ``teams`` into one set. The result must match all ordinary tags, any selected team, and all other filters. Empty values are ignored.
        :type tags: [str], optional
        :param teams: Filter by team handles without the ``team:`` prefix. Use repeated parameters to filter by multiple team handles, such as ``teams=checkout&teams=payments``. A flag must belong to at least one selected team. Team handles from ``teams`` and ``team:<handle>`` values from tags are treated as a single set and combined with ordinary tags and other filters using AND logic. Duplicate handles do not duplicate results. Unknown handles do not match any flags. Empty handles, surrounding white space, or using the ``team:`` prefix return a bad request error. Response tags are unchanged.
        :type teams: [str], optional
        :param production_status: Filter by status across production environments. Use repeated parameters to match any selected status. ``ENABLED`` matches at least one enabled production environment without a variant override. ``OVERRIDDEN`` matches at least one enabled production environment with a variant override. ``DISABLED`` matches flags whose associated production environments are all disabled. A flag can match both ``ENABLED`` and ``OVERRIDDEN`` in different environments. Flags without associated production environments do not match. This does not filter by a specific environment. Unknown values do not match any status.
        :type production_status: [FeatureFlagProductionStatus], optional
        :param distribution_channel: Filter by SDK availability. ``CLIENT`` returns flags with channel ``CLIENT`` or ``ALL``. ``SERVER`` returns flags with channel ``SERVER`` or ``ALL``. ``ALL`` , an empty value, or omission applies no channel restriction; it does not select only flags whose channel is ``ALL``. Values are case-insensitive and surrounding white space is ignored. Invalid values return a bad request error.
        :type distribution_channel: FeatureFlagDistributionChannel, optional
        :param search: Case-insensitive substring search on flag names, keys, and tag names. Combined with all other filters. An empty value applies no search restriction.
        :type search: str, optional
        :param value_type: Filter by variant value types using repeated parameters. A flag must match at least one selected type. Empty values are ignored. Invalid types return a bad request error.
        :type value_type: [ValueType], optional
        :param created_by: Filter by creator UUIDs using repeated parameters. A flag must match at least one creator. Empty values are ignored. Invalid UUIDs return a bad request error.
        :type created_by: [UUID], optional
        :param flag_ids: Filter by feature flag UUIDs using repeated parameters. A flag must match at least one ID and all other filters. Duplicate IDs return each flag once. Unknown IDs and IDs from other organizations do not match any flags. Empty or invalid UUIDs return a bad request error. Pagination still applies.
        :type flag_ids: [UUID], optional
        :param staleness_status: Filter by the computed staleness status: ``ACTIVE`` , ``STALE`` , or ``PERMANENT``. Values are case-insensitive and surrounding white space is ignored. An empty value or omission applies no restriction. Invalid values return a bad request error. Read the computed result from ``staleness_details.staleness_status`` , not the legacy ``staleness_status`` response field.
        :type staleness_status: FeatureFlagStalenessStatus, optional
        :param saved_filter_id: Filter to flags that reference this saved filter in their targeting conditions. An empty value or omission applies no restriction. An invalid UUID returns a bad request error.
        :type saved_filter_id: UUID, optional
        :param sort: Sort by ``name`` , ``updated_at`` , ``created_at`` , or ``evaluations``. Use a comma-separated list for multiple sort fields and prefix a field with ``-`` for descending order. The default is ``updated_at`` descending. When favorites are enabled, the authenticated user's favorite flags take precedence over the selected ordering. Unknown fields return a bad request error.
        :type sort: str, optional
        :param page_limit: Maximum number of flags to return. Defaults to ``25`` and is capped at ``50``. Values that exceed ``50`` are set to ``50``. Non-positive or empty values use the default. A non-integer value returns a bad request error. Takes precedence over ``limit`` when both are present. Pagination applies even when no pagination parameters are supplied.
        :type page_limit: int, optional
        :param page_offset: Number of matching flags to skip before returning results. Defaults to ``0``. Negative or empty values are set to ``0``. A non-integer value returns a bad request error. Takes precedence over ``offset`` when both are present.
        :type page_offset: int, optional
        :rtype: ListFeatureFlagsResponse
        """
        kwargs: Dict[str, Any] = {}
        if key is not unset:
            kwargs["key"] = key

        if is_archived is not unset:
            kwargs["is_archived"] = is_archived

        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        if tags is not unset:
            kwargs["tags"] = tags

        if teams is not unset:
            kwargs["teams"] = teams

        if production_status is not unset:
            kwargs["production_status"] = production_status

        if distribution_channel is not unset:
            kwargs["distribution_channel"] = distribution_channel

        if search is not unset:
            kwargs["search"] = search

        if value_type is not unset:
            kwargs["value_type"] = value_type

        if created_by is not unset:
            kwargs["created_by"] = created_by

        if flag_ids is not unset:
            kwargs["flag_ids"] = flag_ids

        if staleness_status is not unset:
            kwargs["staleness_status"] = staleness_status

        if saved_filter_id is not unset:
            kwargs["saved_filter_id"] = saved_filter_id

        if sort is not unset:
            kwargs["sort"] = sort

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        return self._list_feature_flags_endpoint.call_with_http_info(**kwargs)

    def list_feature_flags_environments(
        self,
        *,
        name: Union[str, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        dd_env: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> ListEnvironmentsResponse:
        """List environments.

        Returns a list of environments for the organization.
        Supports filtering by name, key, and DD_ENV.

        :param name: Filter environments by name (partial matching).
        :type name: str, optional
        :param key: Filter environments by key (partial matching).
        :type key: str, optional
        :param dd_env: Filter environments by queries that contain the provided DD_ENV value.
        :type dd_env: str, optional
        :param limit: Maximum number of results to return.
        :type limit: int, optional
        :param offset: Number of results to skip.
        :type offset: int, optional
        :rtype: ListEnvironmentsResponse
        """
        kwargs: Dict[str, Any] = {}
        if name is not unset:
            kwargs["name"] = name

        if key is not unset:
            kwargs["key"] = key

        if dd_env is not unset:
            kwargs["dd_env"] = dd_env

        if limit is not unset:
            kwargs["limit"] = limit

        if offset is not unset:
            kwargs["offset"] = offset

        return self._list_feature_flags_environments_endpoint.call_with_http_info(**kwargs)

    def pause_exposure_schedule(
        self,
        exposure_schedule_id: UUID,
    ) -> AllocationExposureScheduleResponse:
        """Pause a progressive rollout.

        Pauses a progressive rollout while preserving rollout state.

        :param exposure_schedule_id: The ID of the exposure schedule.
        :type exposure_schedule_id: UUID
        :rtype: AllocationExposureScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_schedule_id"] = exposure_schedule_id

        return self._pause_exposure_schedule_endpoint.call_with_http_info(**kwargs)

    def resume_exposure_schedule(
        self,
        exposure_schedule_id: UUID,
    ) -> AllocationExposureScheduleResponse:
        """Resume a progressive rollout.

        Resumes progression for a previously paused progressive rollout.

        :param exposure_schedule_id: The ID of the exposure schedule.
        :type exposure_schedule_id: UUID
        :rtype: AllocationExposureScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_schedule_id"] = exposure_schedule_id

        return self._resume_exposure_schedule_endpoint.call_with_http_info(**kwargs)

    def start_exposure_schedule(
        self,
        exposure_schedule_id: UUID,
    ) -> AllocationExposureScheduleResponse:
        """Start a progressive rollout.

        Starts a progressive rollout and begins progression.

        :param exposure_schedule_id: The ID of the exposure schedule.
        :type exposure_schedule_id: UUID
        :rtype: AllocationExposureScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_schedule_id"] = exposure_schedule_id

        return self._start_exposure_schedule_endpoint.call_with_http_info(**kwargs)

    def stop_exposure_schedule(
        self,
        exposure_schedule_id: UUID,
    ) -> AllocationExposureScheduleResponse:
        """Stop a progressive rollout.

        Stops a progressive rollout and marks it as aborted.

        :param exposure_schedule_id: The ID of the exposure schedule.
        :type exposure_schedule_id: UUID
        :rtype: AllocationExposureScheduleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_schedule_id"] = exposure_schedule_id

        return self._stop_exposure_schedule_endpoint.call_with_http_info(**kwargs)

    def unarchive_feature_flag(
        self,
        feature_flag_id: UUID,
    ) -> FeatureFlagResponse:
        """Unarchive a feature flag.

        Unarchives a previously archived feature flag,
        making it visible in the main list again.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :rtype: FeatureFlagResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        return self._unarchive_feature_flag_endpoint.call_with_http_info(**kwargs)

    def update_allocations_for_feature_flag_in_environment(
        self,
        feature_flag_id: UUID,
        environment_id: UUID,
        body: OverwriteAllocationsRequest,
    ) -> ListAllocationsResponse:
        """Update targeting rules for a flag.

        Updates targeting rules (allocations) for a specific feature flag in a specific environment.
        This operation replaces the existing allocation set with the request payload.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :type body: OverwriteAllocationsRequest
        :rtype: ListAllocationsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["environment_id"] = environment_id

        kwargs["body"] = body

        return self._update_allocations_for_feature_flag_in_environment_endpoint.call_with_http_info(**kwargs)

    def update_feature_flag(
        self,
        feature_flag_id: UUID,
        body: UpdateFeatureFlagRequest,
    ) -> FeatureFlagResponse:
        """Update a feature flag.

        Updates an existing feature flag's metadata such as
         name and description. Does not modify targeting rules or allocations.

        To change the owning team, update ``tags`` and include a tag of the form
        ``team:<team-handle>`` in the array. ``tags`` is a full replacement of the
        existing tag set (including any ``team:`` tag), so include every tag you
        want to keep, not just the ones you're adding.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :type body: UpdateFeatureFlagRequest
        :rtype: FeatureFlagResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["body"] = body

        return self._update_feature_flag_endpoint.call_with_http_info(**kwargs)

    def update_feature_flags_environment(
        self,
        environment_id: UUID,
        body: UpdateEnvironmentRequest,
    ) -> EnvironmentResponse:
        """Update an environment.

        Updates an existing environment's metadata such as
         name and description.

        :param environment_id: The ID of the environment.
        :type environment_id: UUID
        :type body: UpdateEnvironmentRequest
        :rtype: EnvironmentResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["environment_id"] = environment_id

        kwargs["body"] = body

        return self._update_feature_flags_environment_endpoint.call_with_http_info(**kwargs)

    def update_saved_filter_attributes(
        self,
        saved_filter_id: UUID,
        body: PatchSavedFilterRequest,
    ) -> SavedFilterResponse:
        """Patch a saved filter.

        Partially updates a saved filter. Supports both ``LIST`` and ``RULES`` filters.
        Supply at least one of ``name`` , ``description`` , or ``targeting_rules``. Omitted or null fields
        are preserved. Supplying ``targeting_rules`` replaces the entire collection and propagates
        changes to every feature flag that references the saved filter.
        Metadata-only updates do not require edit permission or approval on those feature flags.
        Rule updates require edit permission on all consumer flags and are rejected when approval
        is required, unless the caller has the ``feature_flag_approvals_override`` permission.
        The optional ``last_updated_at`` field detects stale updates. It does not set the update time.

        :param saved_filter_id: The ID of the saved filter.
        :type saved_filter_id: UUID
        :type body: PatchSavedFilterRequest
        :rtype: SavedFilterResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["saved_filter_id"] = saved_filter_id

        kwargs["body"] = body

        return self._update_saved_filter_attributes_endpoint.call_with_http_info(**kwargs)

    def update_variant_for_feature_flag(
        self,
        feature_flag_id: UUID,
        variant_id: UUID,
        body: UpdateVariantRequest,
    ) -> None:
        """Update a variant.

        Updates the name and value of an existing variant on a feature flag.

        When backend approvals are enabled and the flag requires approval, this endpoint creates and returns a ``FlagSuggestion`` with ``201 Created`` instead of applying the change immediately. Use the returned suggestion ``id`` to approve or reject the change. If a pending suggestion already exists for this flag's variant property, the endpoint returns ``409 Conflict``.

        :param feature_flag_id: The ID of the feature flag.
        :type feature_flag_id: UUID
        :param variant_id: The ID of the variant.
        :type variant_id: UUID
        :type body: UpdateVariantRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["feature_flag_id"] = feature_flag_id

        kwargs["variant_id"] = variant_id

        kwargs["body"] = body

        return self._update_variant_for_feature_flag_endpoint.call_with_http_info(**kwargs)
