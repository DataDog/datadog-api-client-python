# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_metadata import AiGatewayModelMetadata
    from datadog_api_client.v2.model.ai_gateway_model_source import AiGatewayModelSource
    from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation


class AiGatewayProviderModelEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_metadata import AiGatewayModelMetadata
        from datadog_api_client.v2.model.ai_gateway_model_source import AiGatewayModelSource
        from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation

        return {
            "created_at": (datetime,),
            "enabled": (bool,),
            "id": (str,),
            "metadata": (AiGatewayModelMetadata,),
            "model_id_wire": (str,),
            "provider_id": (int,),
            "source": (AiGatewayModelSource,),
            "supported_operations": ([AiGatewaySupportedOperation],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "enabled": "enabled",
        "id": "id",
        "metadata": "metadata",
        "model_id_wire": "model_id_wire",
        "provider_id": "provider_id",
        "source": "source",
        "supported_operations": "supported_operations",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        enabled: bool,
        id: str,
        model_id_wire: str,
        provider_id: int,
        source: AiGatewayModelSource,
        supported_operations: List[AiGatewaySupportedOperation],
        updated_at: datetime,
        metadata: Union[AiGatewayModelMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provider-specific entry for a canonical model.

        :param created_at: Time when the resource was created.
        :type created_at: datetime

        :param enabled: Whether the resource is enabled.
        :type enabled: bool

        :param id: Resource identifier.
        :type id: str

        :param metadata: Optional, typed enrichment for a model catalog entry. Missing properties remain unknown.
        :type metadata: AiGatewayModelMetadata, optional

        :param model_id_wire: Model identifier sent to the provider.
        :type model_id_wire: str

        :param provider_id: Provider identifier.
        :type provider_id: int

        :param source: How a model catalog entry is managed.
        :type source: AiGatewayModelSource

        :param supported_operations: Operations supported by the model.
        :type supported_operations: [AiGatewaySupportedOperation]

        :param updated_at: Time when the resource was last updated.
        :type updated_at: datetime
        """
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.enabled = enabled
        self_.id = id
        self_.model_id_wire = model_id_wire
        self_.provider_id = provider_id
        self_.source = source
        self_.supported_operations = supported_operations
        self_.updated_at = updated_at
