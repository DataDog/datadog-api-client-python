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
    from datadog_api_client.v2.model.pipeline_tls import PipelineTls
    from datadog_api_client.v2.model.pipeline_datadog_agent_source_type import PipelineDatadogAgentSourceType


class PipelineDatadogAgentSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pipeline_tls import PipelineTls
        from datadog_api_client.v2.model.pipeline_datadog_agent_source_type import PipelineDatadogAgentSourceType

        return {
            "id": (str,),
            "tls": (PipelineTls,),
            "type": (PipelineDatadogAgentSourceType,),
        }

    attribute_map = {
        "id": "id",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: PipelineDatadogAgentSourceType, tls: Union[PipelineTls, UnsetType] = unset, **kwargs
    ):
        """
        The ``datadog_agent`` source collects logs from the Datadog Agent.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param tls: Configuration for enabling TLS encryption.
        :type tls: PipelineTls, optional

        :param type: The source type. The value should always be ``datadog_agent``.
        :type type: PipelineDatadogAgentSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
