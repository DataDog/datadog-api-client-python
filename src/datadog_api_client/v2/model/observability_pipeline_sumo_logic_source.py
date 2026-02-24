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
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_source_type import (
        ObservabilityPipelineSumoLogicSourceType,
    )


class ObservabilityPipelineSumoLogicSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_sumo_logic_source_type import (
            ObservabilityPipelineSumoLogicSourceType,
        )

        return {
            "address_key": (str,),
            "id": (str,),
            "type": (ObservabilityPipelineSumoLogicSourceType,),
        }

    attribute_map = {
        "address_key": "address_key",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ObservabilityPipelineSumoLogicSourceType,
        address_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``sumo_logic`` source receives logs from Sumo Logic collectors.

        **Supported pipeline types:** logs

        :param address_key: Name of the environment variable or secret that holds the listen address for the Sumo Logic receiver.
        :type address_key: str, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param type: The source type. The value should always be ``sumo_logic``.
        :type type: ObservabilityPipelineSumoLogicSourceType
        """
        if address_key is not unset:
            kwargs["address_key"] = address_key
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
