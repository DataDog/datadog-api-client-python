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
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_fluent_source_type import (
        ObservabilityPipelineFluentSourceType,
    )


class ObservabilityPipelineFluentSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_fluent_source_type import (
            ObservabilityPipelineFluentSourceType,
        )

        return {
            "id": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineFluentSourceType,),
        }

    attribute_map = {
        "id": "id",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ObservabilityPipelineFluentSourceType,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``fluent`` source ingests logs from a Fluentd-compatible service.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param tls: Configuration for enabling TLS encryption.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``fluent``.
        :type type: ObservabilityPipelineFluentSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
