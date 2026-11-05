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


class AiGatewayModelInput(ModelNormal):
    validations = {
        "model_id_canonical": {
            "max_length": 256,
            "min_length": 1,
        },
        "model_id_wire": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation

        return {
            "model_id_canonical": (str,),
            "model_id_wire": (str,),
            "supported_operations": ([AiGatewaySupportedOperation],),
        }

    attribute_map = {
        "model_id_canonical": "model_id_canonical",
        "model_id_wire": "model_id_wire",
        "supported_operations": "supported_operations",
    }

    def __init__(
        self_,
        model_id_canonical: str,
        model_id_wire: str,
        supported_operations: Union[List[AiGatewaySupportedOperation], UnsetType] = unset,
        **kwargs,
    ):
        """
        Manually managed model definition supplied when creating a provider or catalog entry.

        :param model_id_canonical: Provider-independent model identifier.
        :type model_id_canonical: str

        :param model_id_wire: Model identifier sent to the provider.
        :type model_id_wire: str

        :param supported_operations: Operations supported by the model.
        :type supported_operations: [AiGatewaySupportedOperation], optional
        """
        if supported_operations is not unset:
            kwargs["supported_operations"] = supported_operations
        super().__init__(kwargs)

        self_.model_id_canonical = model_id_canonical
        self_.model_id_wire = model_id_wire
