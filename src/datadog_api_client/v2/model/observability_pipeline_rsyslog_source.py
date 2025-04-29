# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_syslog_source_mode import (
        ObservabilityPipelineSyslogSourceMode,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_rsyslog_source_type import (
        ObservabilityPipelineRsyslogSourceType,
    )


class ObservabilityPipelineRsyslogSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_syslog_source_mode import (
            ObservabilityPipelineSyslogSourceMode,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_rsyslog_source_type import (
            ObservabilityPipelineRsyslogSourceType,
        )

        return {
            "id": (str,),
            "mode": (ObservabilityPipelineSyslogSourceMode,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineRsyslogSourceType,),
        }

    attribute_map = {
        "id": "id",
        "mode": "mode",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        mode: ObservabilityPipelineSyslogSourceMode,
        type: ObservabilityPipelineRsyslogSourceType,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``rsyslog`` source listens for logs over TCP or UDP from an ``rsyslog`` server using the syslog protocol.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param mode: Protocol used by the syslog source to receive messages.
        :type mode: ObservabilityPipelineSyslogSourceMode

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``rsyslog``.
        :type type: ObservabilityPipelineRsyslogSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.mode = mode
        self_.type = type
