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
from datadog_api_client.v2.model.security_agent_investigations_list_response import (
    SecurityAgentInvestigationsListResponse,
)
from datadog_api_client.v2.model.security_agent_investigation_counts_response import (
    SecurityAgentInvestigationCountsResponse,
)
from datadog_api_client.v2.model.security_agent_investigation_count_field import SecurityAgentInvestigationCountField
from datadog_api_client.v2.model.security_agent_investigation_response import SecurityAgentInvestigationResponse
from datadog_api_client.v2.model.security_agent_investigation_field import SecurityAgentInvestigationField


class BitsSecurityAnalystApi:
    """
    Use the Bits Security Analyst endpoints to find the investigations of your Cloud SIEM signals, read an
    investigation's verdict and findings, and count investigations.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._count_security_agent_investigations_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityAgentInvestigationCountsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/security_agent/investigations/count",
                "operation_id": "count_security_agent_investigations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "field": {
                    "required": True,
                    "openapi_types": (SecurityAgentInvestigationCountField,),
                    "attribute": "field",
                    "location": "query",
                },
                "filter_title": {
                    "openapi_types": (str,),
                    "attribute": "filter[title]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (str,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (str,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "filter_verdict": {
                    "openapi_types": (str,),
                    "attribute": "filter[verdict]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule_id]",
                    "location": "query",
                },
                "filter_rule_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule_type]",
                    "location": "query",
                },
                "filter_signal_severity": {
                    "openapi_types": (str,),
                    "attribute": "filter[signal_severity]",
                    "location": "query",
                },
                "filter_signal_source": {
                    "openapi_types": (str,),
                    "attribute": "filter[signal_source]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "filter_entity": {
                    "openapi_types": (str,),
                    "attribute": "filter[entity]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_security_agent_investigation_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityAgentInvestigationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/security_agent/investigations/{investigation_id}",
                "operation_id": "get_security_agent_investigation",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "investigation_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "investigation_id",
                    "location": "path",
                },
                "fields_investigations": {
                    "openapi_types": ([SecurityAgentInvestigationField],),
                    "attribute": "fields[investigations]",
                    "location": "query",
                    "collection_format": "csv",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_security_agent_investigations_endpoint = _Endpoint(
            settings={
                "response_type": (SecurityAgentInvestigationsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/security_monitoring/security_agent/investigations",
                "operation_id": "list_security_agent_investigations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_signal_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[signal_id]",
                    "location": "query",
                },
                "filter_title": {
                    "openapi_types": (str,),
                    "attribute": "filter[title]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (str,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (str,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "filter_verdict": {
                    "openapi_types": (str,),
                    "attribute": "filter[verdict]",
                    "location": "query",
                },
                "filter_state": {
                    "openapi_types": (str,),
                    "attribute": "filter[state]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule_id]",
                    "location": "query",
                },
                "filter_rule_type": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule_type]",
                    "location": "query",
                },
                "filter_signal_severity": {
                    "openapi_types": (str,),
                    "attribute": "filter[signal_severity]",
                    "location": "query",
                },
                "filter_signal_source": {
                    "openapi_types": (str,),
                    "attribute": "filter[signal_source]",
                    "location": "query",
                },
                "filter_tags": {
                    "openapi_types": (str,),
                    "attribute": "filter[tags]",
                    "location": "query",
                },
                "filter_entity": {
                    "openapi_types": (str,),
                    "attribute": "filter[entity]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_number": {
                    "validation": {
                        "inclusive_minimum": 1,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[number]",
                    "location": "query",
                },
                "page_size": {
                    "validation": {
                        "inclusive_maximum": 100,
                        "inclusive_minimum": 1,
                    },
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

    def count_security_agent_investigations(
        self,
        field: SecurityAgentInvestigationCountField,
        *,
        filter_title: Union[str, UnsetType] = unset,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        filter_verdict: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_type: Union[str, UnsetType] = unset,
        filter_signal_severity: Union[str, UnsetType] = unset,
        filter_signal_source: Union[str, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_entity: Union[str, UnsetType] = unset,
    ) -> SecurityAgentInvestigationCountsResponse:
        """Count Bits Security Analyst investigations.

        Count completed Bits Security Analyst investigations by the values of one field. Buckets are sorted by
        ascending count. With ``field=entity`` or ``field=signal_source`` , an investigation counts in the bucket of
        each of its entities or sources.

        :param field: Field to count completed investigations by.
        :type field: SecurityAgentInvestigationCountField
        :param filter_title: Only investigations whose signal title contains this text, case-insensitive.
        :type filter_title: str, optional
        :param filter_from: Only investigations last updated at or after this time, as RFC 3339 or milliseconds since the epoch.
        :type filter_from: str, optional
        :param filter_to: Only investigations last updated at or before this time, as RFC 3339 or milliseconds since the epoch.
        :type filter_to: str, optional
        :param filter_verdict: Only investigations with one of these verdicts: ``benign`` , ``suspicious`` , or ``malicious``.
            Comma-separated values; an investigation matches any of them.
        :type filter_verdict: str, optional
        :param filter_rule_id: Only investigations of signals from one of these detection rule IDs. Comma-separated values; an
            investigation matches any of them.
        :type filter_rule_id: str, optional
        :param filter_rule_type: Only investigations of signals from detection rules of one of these types, as returned by the count with
            ``field=rule_type``. Comma-separated values; an investigation matches any of them.
        :type filter_rule_type: str, optional
        :param filter_signal_severity: Only investigations of signals with one of these severities: ``info`` , ``low`` , ``medium`` , ``high`` , or ``critical``.
            Comma-separated values; an investigation matches any of them.
        :type filter_signal_severity: str, optional
        :param filter_signal_source: Only investigations of signals from one of these sources, as returned by the count with
            ``field=signal_source``. Comma-separated values; an investigation matches any of them.
        :type filter_signal_source: str, optional
        :param filter_tags: Only investigations whose signal has all of these tags, written ``key:value``. Comma-separated values; an
            investigation must have every one of them.
        :type filter_tags: str, optional
        :param filter_entity: Only investigations whose signal has all of these entities. Write each entity as ``attribute:value`` , matching the
            values returned by the count endpoint with ``field=entity``. Comma-separated values; an investigation must have
            every one of them.
        :type filter_entity: str, optional
        :rtype: SecurityAgentInvestigationCountsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["field"] = field

        if filter_title is not unset:
            kwargs["filter_title"] = filter_title

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_verdict is not unset:
            kwargs["filter_verdict"] = filter_verdict

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_type is not unset:
            kwargs["filter_rule_type"] = filter_rule_type

        if filter_signal_severity is not unset:
            kwargs["filter_signal_severity"] = filter_signal_severity

        if filter_signal_source is not unset:
            kwargs["filter_signal_source"] = filter_signal_source

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_entity is not unset:
            kwargs["filter_entity"] = filter_entity

        return self._count_security_agent_investigations_endpoint.call_with_http_info(**kwargs)

    def get_security_agent_investigation(
        self,
        investigation_id: str,
        *,
        fields_investigations: Union[List[SecurityAgentInvestigationField], UnsetType] = unset,
    ) -> SecurityAgentInvestigationResponse:
        """Get a Bits Security Analyst investigation.

        Get a Bits Security Analyst investigation by its ID, with its verdict, conclusion, evidence, steps, and
        response suggestions. While the investigation is running, the response has a ``Retry-After`` header.

        :param investigation_id: The ID of the investigation, as returned by the list.
        :type investigation_id: str
        :param fields_investigations: Attributes to return, comma-separated. Defaults to all attributes.
        :type fields_investigations: [SecurityAgentInvestigationField], optional
        :rtype: SecurityAgentInvestigationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["investigation_id"] = investigation_id

        if fields_investigations is not unset:
            kwargs["fields_investigations"] = fields_investigations

        return self._get_security_agent_investigation_endpoint.call_with_http_info(**kwargs)

    def list_security_agent_investigations(
        self,
        *,
        filter_signal_id: Union[str, UnsetType] = unset,
        filter_title: Union[str, UnsetType] = unset,
        filter_from: Union[str, UnsetType] = unset,
        filter_to: Union[str, UnsetType] = unset,
        filter_verdict: Union[str, UnsetType] = unset,
        filter_state: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_type: Union[str, UnsetType] = unset,
        filter_signal_severity: Union[str, UnsetType] = unset,
        filter_signal_source: Union[str, UnsetType] = unset,
        filter_tags: Union[str, UnsetType] = unset,
        filter_entity: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        page_number: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
    ) -> SecurityAgentInvestigationsListResponse:
        """List Bits Security Analyst investigations.

        List Bits Security Analyst investigations.

        Without ``filter[signal_id]`` , returns the latest investigation of each signal, filtered, sorted, and paginated.
        With ``filter[signal_id]`` , returns every investigation of that signal, newest first. When the signal has no
        investigation, the first page carries ``meta.reason`` , which says why.

        :param filter_signal_id: List every investigation of this signal, newest first. Accepts the signal ID in its V1 form, which starts
            with ``AQ`` , or in its longer V3 form, which starts with ``Aw``. Investigations carry the V1 form, so their
            ``signal_id`` can differ from the ID you pass. Can't be combined with other filters or with ``sort``.
        :type filter_signal_id: str, optional
        :param filter_title: Only investigations whose signal title contains this text, case-insensitive.
        :type filter_title: str, optional
        :param filter_from: Only investigations last updated at or after this time, as RFC 3339 or milliseconds since the epoch.
        :type filter_from: str, optional
        :param filter_to: Only investigations last updated at or before this time, as RFC 3339 or milliseconds since the epoch.
        :type filter_to: str, optional
        :param filter_verdict: Only investigations with one of these verdicts: ``benign`` , ``suspicious`` , or ``malicious``.
            Comma-separated values; an investigation matches any of them.
        :type filter_verdict: str, optional
        :param filter_state: Only investigations in one of these states: ``investigating`` or ``completed``. Investigations reported as
            ``failed`` match ``investigating``. Comma-separated values; an investigation matches any of them.
        :type filter_state: str, optional
        :param filter_rule_id: Only investigations of signals from one of these detection rule IDs. Comma-separated values; an
            investigation matches any of them.
        :type filter_rule_id: str, optional
        :param filter_rule_type: Only investigations of signals from detection rules of one of these types, as returned by the count with
            ``field=rule_type``. Comma-separated values; an investigation matches any of them.
        :type filter_rule_type: str, optional
        :param filter_signal_severity: Only investigations of signals with one of these severities: ``info`` , ``low`` , ``medium`` , ``high`` , or ``critical``.
            Comma-separated values; an investigation matches any of them.
        :type filter_signal_severity: str, optional
        :param filter_signal_source: Only investigations of signals from one of these sources, as returned by the count with
            ``field=signal_source``. Comma-separated values; an investigation matches any of them.
        :type filter_signal_source: str, optional
        :param filter_tags: Only investigations whose signal has all of these tags, written ``key:value``. Comma-separated values; an
            investigation must have every one of them.
        :type filter_tags: str, optional
        :param filter_entity: Only investigations whose signal has all of these entities. Write each entity as ``attribute:value`` , matching the
            values returned by the count endpoint with ``field=entity``. Comma-separated values; an investigation must have
            every one of them.
        :type filter_entity: str, optional
        :param sort: Sort field, prefixed with ``-`` for descending: ``updated_at`` , ``severity`` , ``verdict`` , ``rule_id`` , or ``signal_title``.
            Defaults to ``-updated_at``. ``verdict`` sorts by severity ( ``benign`` , ``suspicious`` , ``malicious`` ), so ``-verdict`` puts
            ``malicious`` first.
        :type sort: str, optional
        :param page_number: Page number, starting at 1.
        :type page_number: int, optional
        :param page_size: Number of investigations per page.
        :type page_size: int, optional
        :rtype: SecurityAgentInvestigationsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_signal_id is not unset:
            kwargs["filter_signal_id"] = filter_signal_id

        if filter_title is not unset:
            kwargs["filter_title"] = filter_title

        if filter_from is not unset:
            kwargs["filter_from"] = filter_from

        if filter_to is not unset:
            kwargs["filter_to"] = filter_to

        if filter_verdict is not unset:
            kwargs["filter_verdict"] = filter_verdict

        if filter_state is not unset:
            kwargs["filter_state"] = filter_state

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_type is not unset:
            kwargs["filter_rule_type"] = filter_rule_type

        if filter_signal_severity is not unset:
            kwargs["filter_signal_severity"] = filter_signal_severity

        if filter_signal_source is not unset:
            kwargs["filter_signal_source"] = filter_signal_source

        if filter_tags is not unset:
            kwargs["filter_tags"] = filter_tags

        if filter_entity is not unset:
            kwargs["filter_entity"] = filter_entity

        if sort is not unset:
            kwargs["sort"] = sort

        if page_number is not unset:
            kwargs["page_number"] = page_number

        if page_size is not unset:
            kwargs["page_size"] = page_size

        return self._list_security_agent_investigations_endpoint.call_with_http_info(**kwargs)
