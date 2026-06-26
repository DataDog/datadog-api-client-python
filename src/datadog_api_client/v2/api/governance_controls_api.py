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
)
from datadog_api_client.v2.model.governance_controls_response import GovernanceControlsResponse
from datadog_api_client.v2.model.governance_control_response import GovernanceControlResponse
from datadog_api_client.v2.model.governance_control_update_request import GovernanceControlUpdateRequest
from datadog_api_client.v2.model.governance_control_detections_response import GovernanceControlDetectionsResponse
from datadog_api_client.v2.model.governance_control_detection_response import GovernanceControlDetectionResponse
from datadog_api_client.v2.model.governance_control_detection_update_request import (
    GovernanceControlDetectionUpdateRequest,
)
from datadog_api_client.v2.model.control_notification_settings_response import ControlNotificationSettingsResponse
from datadog_api_client.v2.model.control_notification_settings_update_request import (
    ControlNotificationSettingsUpdateRequest,
)
from datadog_api_client.v2.model.governance_mitigation_request import GovernanceMitigationRequest


class GovernanceControlsApi:
    """
    Governance Controls pair a detection definition with an organization's detection, notification,
    and mitigation configuration within the Governance Console. Each control reports how a class of
    governance issue (such as unused API keys or unqueried metrics) is detected and remediated, along
    with counts of active and mitigated detections.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_governance_mitigation_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/mitigate",
                "operation_id": "create_governance_mitigation",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (GovernanceMitigationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_governance_control_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}",
                "operation_id": "get_governance_control",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_governance_control_detection_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlDetectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}/detections/{detection_id}",
                "operation_id": "get_governance_control_detection",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
                "detection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_governance_control_notification_settings_endpoint = _Endpoint(
            settings={
                "response_type": (ControlNotificationSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}/notification_settings",
                "operation_id": "get_governance_control_notification_settings",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_governance_control_detections_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlDetectionsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}/detections",
                "operation_id": "list_governance_control_detections",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
                "filter_state": {
                    "openapi_types": (str,),
                    "attribute": "filter[state]",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_number": {
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_governance_controls_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control",
                "operation_id": "list_governance_controls",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_governance_control_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}",
                "operation_id": "update_governance_control",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GovernanceControlUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_governance_control_detection_endpoint = _Endpoint(
            settings={
                "response_type": (GovernanceControlDetectionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}/detections/{detection_id}",
                "operation_id": "update_governance_control_detection",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
                "detection_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GovernanceControlDetectionUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_governance_control_notification_settings_endpoint = _Endpoint(
            settings={
                "response_type": (ControlNotificationSettingsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/governance/control/{detection_type}/notification_settings",
                "operation_id": "update_governance_control_notification_settings",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "detection_type": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "detection_type",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ControlNotificationSettingsUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_governance_mitigation(
        self,
        body: GovernanceMitigationRequest,
    ) -> None:
        """Mitigate governance detections.

        Apply a mitigation to a set of governance detections of a given detection type. When the
        mitigation type is omitted, the control's configured mitigation is used. The request is
        accepted for asynchronous processing.

        :type body: GovernanceMitigationRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_governance_mitigation_endpoint.call_with_http_info(**kwargs)

    def get_governance_control(
        self,
        detection_type: str,
    ) -> GovernanceControlResponse:
        """Get a governance control.

        Retrieve a single governance control by its detection type, including the organization's current
        detection, notification, and mitigation configuration and detection counts.

        :param detection_type: The detection type that identifies the control, for example ``unused_api_keys``.
        :type detection_type: str
        :rtype: GovernanceControlResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        return self._get_governance_control_endpoint.call_with_http_info(**kwargs)

    def get_governance_control_detection(
        self,
        detection_type: str,
        detection_id: str,
    ) -> GovernanceControlDetectionResponse:
        """Get a governance control detection.

        Retrieve a single detection produced by the governance control with the given detection type.

        :param detection_type: The detection type that identifies the control; for example, ``unused_api_keys``.
        :type detection_type: str
        :param detection_id: The unique identifier of the detection.
        :type detection_id: str
        :rtype: GovernanceControlDetectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        kwargs["detection_id"] = detection_id

        return self._get_governance_control_detection_endpoint.call_with_http_info(**kwargs)

    def get_governance_control_notification_settings(
        self,
        detection_type: str,
    ) -> ControlNotificationSettingsResponse:
        """Get governance control notification settings.

        Retrieve the notification settings for the governance control with the given detection type,
        including, for each supported event type, whether notifications are enabled and which
        destinations receive them.

        :param detection_type: The detection type that identifies the control; for example, ``unused_api_keys``.
        :type detection_type: str
        :rtype: ControlNotificationSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        return self._get_governance_control_notification_settings_endpoint.call_with_http_info(**kwargs)

    def list_governance_control_detections(
        self,
        detection_type: str,
        *,
        filter_state: Union[str, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> GovernanceControlDetectionsResponse:
        """List governance control detections.

        Retrieve the detections produced by the governance control with the given detection type.
        Results can be filtered by state and free-text query, sorted, and paginated.

        :param detection_type: The detection type that identifies the control; for example, ``unused_api_keys``.
        :type detection_type: str
        :param filter_state: Restrict the results to detections in the given state.
        :type filter_state: str, optional
        :param filter_query: Restrict the results to detections matching the given free-text query.
        :type filter_query: str, optional
        :param sort: The attribute to sort detections by. Prefix with ``-`` for descending order.
        :type sort: str, optional
        :param page_number: The zero-based index of the page to return; the first page is 0.
        :type page_number: int, optional
        :param page_size: The number of detections to return per page.
        :type page_size: int, optional
        :rtype: GovernanceControlDetectionsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        if filter_state is not unset:
            kwargs["filter_state"] = filter_state

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if sort is not unset:
            kwargs["sort"] = sort

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_governance_control_detections_endpoint.call_with_http_info(**kwargs)

    def list_governance_controls(
        self,
    ) -> GovernanceControlsResponse:
        """List governance controls.

        Retrieve the list of governance controls configured for the organization. Each control pairs a
        detection definition with the organization's current detection, notification, and mitigation
        configuration, along with counts of active and mitigated detections.

        :rtype: GovernanceControlsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_governance_controls_endpoint.call_with_http_info(**kwargs)

    def update_governance_control(
        self,
        detection_type: str,
        body: GovernanceControlUpdateRequest,
    ) -> GovernanceControlResponse:
        """Update a governance control.

        Update the detection, notification, and mitigation configuration of a governance control. Only
        the attributes present in the request are modified. Changing the mitigation type or its
        parameters may require additional permissions.

        :param detection_type: The detection type that identifies the control, for example ``unused_api_keys``.
        :type detection_type: str
        :type body: GovernanceControlUpdateRequest
        :rtype: GovernanceControlResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        kwargs["body"] = body

        return self._update_governance_control_endpoint.call_with_http_info(**kwargs)

    def update_governance_control_detection(
        self,
        detection_type: str,
        detection_id: str,
        body: GovernanceControlDetectionUpdateRequest,
    ) -> GovernanceControlDetectionResponse:
        """Update a governance control detection.

        Update a detection produced by the governance control with the given detection type. Only the
        attributes present in the request are modified, allowing a detection to be acknowledged as an
        exception, reopened, reassigned, or deferred for mitigation.

        :param detection_type: The detection type that identifies the control; for example, ``unused_api_keys``.
        :type detection_type: str
        :param detection_id: The unique identifier of the detection.
        :type detection_id: str
        :type body: GovernanceControlDetectionUpdateRequest
        :rtype: GovernanceControlDetectionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        kwargs["detection_id"] = detection_id

        kwargs["body"] = body

        return self._update_governance_control_detection_endpoint.call_with_http_info(**kwargs)

    def update_governance_control_notification_settings(
        self,
        detection_type: str,
        body: ControlNotificationSettingsUpdateRequest,
    ) -> ControlNotificationSettingsResponse:
        """Update governance control notification settings.

        Replace the notification settings for the governance control with the given detection type,
        setting, for each supported event type, whether notifications are enabled and which
        destinations receive them.

        :param detection_type: The detection type that identifies the control; for example, ``unused_api_keys``.
        :type detection_type: str
        :type body: ControlNotificationSettingsUpdateRequest
        :rtype: ControlNotificationSettingsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["detection_type"] = detection_type

        kwargs["body"] = body

        return self._update_governance_control_notification_settings_endpoint.call_with_http_info(**kwargs)
