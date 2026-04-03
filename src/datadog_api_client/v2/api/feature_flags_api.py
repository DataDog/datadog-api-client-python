# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.list_feature_flags_response import ListFeatureFlagsResponse
from datadog_api_client.v2.model.feature_flag_response import FeatureFlagResponse
from datadog_api_client.v2.model.create_feature_flag_request import CreateFeatureFlagRequest
from datadog_api_client.v2.model.list_environments_response import ListEnvironmentsResponse
from datadog_api_client.v2.model.environment_response import EnvironmentResponse
from datadog_api_client.v2.model.create_environment_request import CreateEnvironmentRequest
from datadog_api_client.v2.model.update_environment_request import UpdateEnvironmentRequest
from datadog_api_client.v2.model.allocation_exposure_schedule_response import AllocationExposureScheduleResponse
from datadog_api_client.v2.model.update_feature_flag_request import UpdateFeatureFlagRequest
from datadog_api_client.v2.model.allocation_response import AllocationResponse
from datadog_api_client.v2.model.create_allocations_request import CreateAllocationsRequest
from datadog_api_client.v2.model.list_allocations_response import ListAllocationsResponse
from datadog_api_client.v2.model.overwrite_allocations_request import OverwriteAllocationsRequest


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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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

        self._delete_feature_flags_environment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
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

        self._disable_feature_flag_environment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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

        self._list_feature_flags_endpoint = _Endpoint(
            settings={
                "response_type": (ListFeatureFlagsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_feature_flags_environments_endpoint = _Endpoint(
            settings={
                "response_type": (ListEnvironmentsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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
                "auth": ["apiKeyAuth", "appKeyAuth"],
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

    def list_feature_flags(
        self,
        *,
        key: Union[str, UnsetType] = unset,
        is_archived: Union[bool, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> ListFeatureFlagsResponse:
        """List feature flags.

        Returns a list of feature flags for the organization.
        Supports filtering by key and archived status.

        :param key: Filter feature flags by key (partial matching).
        :type key: str, optional
        :param is_archived: Filter by archived status.
        :type is_archived: bool, optional
        :param limit: Maximum number of results to return.
        :type limit: int, optional
        :param offset: Number of results to skip.
        :type offset: int, optional
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

        return self._list_feature_flags_endpoint.call_with_http_info(**kwargs)

    def list_feature_flags_environments(
        self,
        *,
        name: Union[str, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        offset: Union[int, UnsetType] = unset,
    ) -> ListEnvironmentsResponse:
        """List environments.

        Returns a list of environments for the organization.
        Supports filtering by name and key.

        :param name: Filter environments by name (partial matching).
        :type name: str, optional
        :param key: Filter environments by key (partial matching).
        :type key: str, optional
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
