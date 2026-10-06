# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    pass


class CILogItem(ModelNormal):
    validations = {
        "job_id": {
            "min_length": 1,
        },
        "line_number": {
            "inclusive_maximum": 9223372036854775807,
            "inclusive_minimum": 0,
        },
        "message": {
            "min_length": 1,
        },
        "pipeline_unique_id": {
            "min_length": 1,
        },
        "provider_name": {
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        from datadog_api_client.v2.model.ci_log_attribute_value import CILogAttributeValue

        return (CILogAttributeValue,)

    @cached_property
    def openapi_types(_):
        return {
            "ddtags": (str,),
            "job_id": (str,),
            "line_number": (int,),
            "message": (str,),
            "pipeline_unique_id": (str,),
            "provider_name": (str,),
            "section_name": (str,),
            "status": (str,),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "ddtags": "ddtags",
        "job_id": "job_id",
        "line_number": "line_number",
        "message": "message",
        "pipeline_unique_id": "pipeline_unique_id",
        "provider_name": "provider_name",
        "section_name": "section_name",
        "status": "status",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        job_id: str,
        message: str,
        pipeline_unique_id: str,
        ddtags: Union[str, UnsetType] = unset,
        line_number: Union[int, UnsetType] = unset,
        provider_name: Union[str, UnsetType] = unset,
        section_name: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        timestamp: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        A CI job log line.

        :param ddtags: Comma-separated ``key:value`` tags. A job can have up to 256 tags, including repeated keys.
        :type ddtags: str, optional

        :param job_id: The job event's ``resource.id`` , sent through the CI Visibility pipeline API.
        :type job_id: str

        :param line_number: The line number in the job log. Use 0 or 1 for the first line.
        :type line_number: int, optional

        :param message: The non-empty log line message.
        :type message: str

        :param pipeline_unique_id: The ``resource.unique_id`` of the pipeline event, which must also match the job event's
            ``resource.pipeline_unique_id``.
        :type pipeline_unique_id: str

        :param provider_name: The provider name sent with the pipeline event. It defaults to ``custom`` when omitted and, when provided,
            must be non-empty and cannot contain a comma.
        :type provider_name: str, optional

        :param section_name: The provider-defined section containing this log line, used to display collapsible groups of lines in the CI
            job log view.
        :type section_name: str, optional

        :param status: The status of this log line. Any string is accepted. Datadog maps non-empty values to a standard log status.
            See `status mapping <https://docs.datadoghq.com/logs/log_configuration/processors/log_status_remapper/>`_.
        :type status: str, optional

        :param timestamp: The log line time in RFC 3339 format with an explicit timezone. If omitted, the intake time is used. It can
            be at most 18 hours in the past or 12 hours in the future.
        :type timestamp: datetime, optional
        """
        if ddtags is not unset:
            kwargs["ddtags"] = ddtags
        if line_number is not unset:
            kwargs["line_number"] = line_number
        if provider_name is not unset:
            kwargs["provider_name"] = provider_name
        if section_name is not unset:
            kwargs["section_name"] = section_name
        if status is not unset:
            kwargs["status"] = status
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)

        self_.job_id = job_id
        self_.message = message
        self_.pipeline_unique_id = pipeline_unique_id
