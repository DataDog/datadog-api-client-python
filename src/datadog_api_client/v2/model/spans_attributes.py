# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

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


class SpansAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (
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
            "custom": (
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
            "end_timestamp": (datetime,),
            "env": (str,),
            "host": (str,),
            "ingestion_reason": (str,),
            "parent_id": (str,),
            "resource_hash": (str,),
            "resource_name": (str,),
            "retained_by": (str,),
            "service": (str,),
            "single_span": (bool,),
            "span_id": (str,),
            "start_timestamp": (datetime,),
            "tags": ([str],),
            "trace_id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "custom": "custom",
        "end_timestamp": "end_timestamp",
        "env": "env",
        "host": "host",
        "ingestion_reason": "ingestion_reason",
        "parent_id": "parent_id",
        "resource_hash": "resource_hash",
        "resource_name": "resource_name",
        "retained_by": "retained_by",
        "service": "service",
        "single_span": "single_span",
        "span_id": "span_id",
        "start_timestamp": "start_timestamp",
        "tags": "tags",
        "trace_id": "trace_id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[Dict[str, Any], UnsetType] = unset,
        custom: Union[Dict[str, Any], UnsetType] = unset,
        end_timestamp: Union[datetime, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        ingestion_reason: Union[str, UnsetType] = unset,
        parent_id: Union[str, UnsetType] = unset,
        resource_hash: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        retained_by: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        single_span: Union[bool, UnsetType] = unset,
        span_id: Union[str, UnsetType] = unset,
        start_timestamp: Union[datetime, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        trace_id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON object containing all span attributes and their associated values.

        :param attributes: JSON object of attributes from your span.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param custom: JSON object of custom spans data.
        :type custom: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param end_timestamp: End timestamp of your span.
        :type end_timestamp: datetime, optional

        :param env: Name of the environment from where the spans are being sent.
        :type env: str, optional

        :param host: Name of the machine from where the spans are being sent.
        :type host: str, optional

        :param ingestion_reason: The reason why the span was ingested.
        :type ingestion_reason: str, optional

        :param parent_id: Id of the span that's parent of this span.
        :type parent_id: str, optional

        :param resource_hash: Unique identifier of the resource.
        :type resource_hash: str, optional

        :param resource_name: The name of the resource.
        :type resource_name: str, optional

        :param retained_by: The reason why the span was indexed.
        :type retained_by: str, optional

        :param service: The name of the application or service generating the span events.
            It is used to switch from APM to Logs, so make sure you define the same
            value when you use both products.
        :type service: str, optional

        :param single_span: Whether or not the span was collected as a stand-alone span. Always associated to "single_span" ingestion_reason if true.
        :type single_span: bool, optional

        :param span_id: Id of the span.
        :type span_id: str, optional

        :param start_timestamp: Start timestamp of your span.
        :type start_timestamp: datetime, optional

        :param tags: Array of tags associated with your span.
        :type tags: [str], optional

        :param trace_id: Id of the trace to which the span belongs.
        :type trace_id: str, optional

        :param type: The type of the span.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if custom is not unset:
            kwargs["custom"] = custom
        if end_timestamp is not unset:
            kwargs["end_timestamp"] = end_timestamp
        if env is not unset:
            kwargs["env"] = env
        if host is not unset:
            kwargs["host"] = host
        if ingestion_reason is not unset:
            kwargs["ingestion_reason"] = ingestion_reason
        if parent_id is not unset:
            kwargs["parent_id"] = parent_id
        if resource_hash is not unset:
            kwargs["resource_hash"] = resource_hash
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        if retained_by is not unset:
            kwargs["retained_by"] = retained_by
        if service is not unset:
            kwargs["service"] = service
        if single_span is not unset:
            kwargs["single_span"] = single_span
        if span_id is not unset:
            kwargs["span_id"] = span_id
        if start_timestamp is not unset:
            kwargs["start_timestamp"] = start_timestamp
        if tags is not unset:
            kwargs["tags"] = tags
        if trace_id is not unset:
            kwargs["trace_id"] = trace_id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
