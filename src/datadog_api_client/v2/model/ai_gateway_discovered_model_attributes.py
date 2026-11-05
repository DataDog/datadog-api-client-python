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
    from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation


class AiGatewayDiscoveredModelAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation

        return {
            "display_name": (str,),
            "model_id_wire": (str,),
            "supported_operations": ([AiGatewaySupportedOperation],),
        }

    attribute_map = {
        "display_name": "display_name",
        "model_id_wire": "model_id_wire",
        "supported_operations": "supported_operations",
    }

    def __init__(
        self_,
        model_id_wire: str,
        supported_operations: List[AiGatewaySupportedOperation],
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Model discovered from a provider integration account.

        :param display_name: Human-readable model name.
        :type display_name: str, optional

        :param model_id_wire: Model identifier sent to the provider.
        :type model_id_wire: str

        :param supported_operations: Operations supported by the model.
        :type supported_operations: [AiGatewaySupportedOperation]
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.model_id_wire = model_id_wire
        self_.supported_operations = supported_operations
