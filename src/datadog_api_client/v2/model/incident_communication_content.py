# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_communication_content_handle import IncidentCommunicationContentHandle


class IncidentCommunicationContent(ModelNormal):
    validations = {
        "status": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_communication_content_handle import IncidentCommunicationContentHandle

        return {
            "grouping_key": (str,),
            "handles": ([IncidentCommunicationContentHandle],),
            "message": (str,),
            "status": (int,),
            "subject": (str,),
        }

    attribute_map = {
        "grouping_key": "grouping_key",
        "handles": "handles",
        "message": "message",
        "status": "status",
        "subject": "subject",
    }

    def __init__(
        self_,
        handles: List[IncidentCommunicationContentHandle],
        message: str,
        grouping_key: Union[str, UnsetType] = unset,
        status: Union[int, UnsetType] = unset,
        subject: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The content of a communication.

        :param grouping_key: A key used for grouping communications.
        :type grouping_key: str, optional

        :param handles: The list of handles the communication is sent to.
        :type handles: [IncidentCommunicationContentHandle]

        :param message: The message body of the communication.
        :type message: str

        :param status: The status code of the communication.
        :type status: int, optional

        :param subject: The subject line of the communication.
        :type subject: str, optional
        """
        if grouping_key is not unset:
            kwargs["grouping_key"] = grouping_key
        if status is not unset:
            kwargs["status"] = status
        if subject is not unset:
            kwargs["subject"] = subject
        super().__init__(kwargs)

        self_.handles = handles
        self_.message = message
