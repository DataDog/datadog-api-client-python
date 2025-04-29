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
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_syslog_ng_destination_type import (
        ObservabilityPipelineSyslogNgDestinationType,
    )


class ObservabilityPipelineSyslogNgDestination(ModelNormal):
    validations = {
        "keepalive": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_syslog_ng_destination_type import (
            ObservabilityPipelineSyslogNgDestinationType,
        )

        return {
            "id": (str,),
            "inputs": ([str],),
            "keepalive": (int,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineSyslogNgDestinationType,),
        }

    attribute_map = {
        "id": "id",
        "inputs": "inputs",
        "keepalive": "keepalive",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineSyslogNgDestinationType,
        keepalive: Union[int, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``syslog_ng`` destination forwards logs to an external ``syslog-ng`` server over TCP or UDP using the syslog protocol.

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param keepalive: Optional socket keepalive duration in milliseconds.
        :type keepalive: int, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. The value should always be ``syslog_ng``.
        :type type: ObservabilityPipelineSyslogNgDestinationType
        """
        if keepalive is not unset:
            kwargs["keepalive"] = keepalive
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
