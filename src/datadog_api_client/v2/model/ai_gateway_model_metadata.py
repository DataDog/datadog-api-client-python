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
    from datadog_api_client.v2.model.ai_gateway_model_capabilities import AiGatewayModelCapabilities
    from datadog_api_client.v2.model.ai_gateway_model_metadata_kind import AiGatewayModelMetadataKind
    from datadog_api_client.v2.model.ai_gateway_model_metadata_lifecycle import AiGatewayModelMetadataLifecycle
    from datadog_api_client.v2.model.ai_gateway_model_limits import AiGatewayModelLimits
    from datadog_api_client.v2.model.ai_gateway_model_modalities import AiGatewayModelModalities
    from datadog_api_client.v2.model.ai_gateway_model_reasoning import AiGatewayModelReasoning
    from datadog_api_client.v2.model.ai_gateway_model_reference_price import AiGatewayModelReferencePrice
    from datadog_api_client.v2.model.ai_gateway_model_metadata_source import AiGatewayModelMetadataSource
    from datadog_api_client.v2.model.ai_gateway_model_metadata_status import AiGatewayModelMetadataStatus


class AiGatewayModelMetadata(ModelNormal):
    validations = {
        "last_updated": {},
        "release_date": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_capabilities import AiGatewayModelCapabilities
        from datadog_api_client.v2.model.ai_gateway_model_metadata_kind import AiGatewayModelMetadataKind
        from datadog_api_client.v2.model.ai_gateway_model_metadata_lifecycle import AiGatewayModelMetadataLifecycle
        from datadog_api_client.v2.model.ai_gateway_model_limits import AiGatewayModelLimits
        from datadog_api_client.v2.model.ai_gateway_model_modalities import AiGatewayModelModalities
        from datadog_api_client.v2.model.ai_gateway_model_reasoning import AiGatewayModelReasoning
        from datadog_api_client.v2.model.ai_gateway_model_reference_price import AiGatewayModelReferencePrice
        from datadog_api_client.v2.model.ai_gateway_model_metadata_source import AiGatewayModelMetadataSource
        from datadog_api_client.v2.model.ai_gateway_model_metadata_status import AiGatewayModelMetadataStatus

        return {
            "capabilities": (AiGatewayModelCapabilities,),
            "description": (str,),
            "display_name": (str,),
            "family": (str,),
            "kind": (AiGatewayModelMetadataKind,),
            "knowledge_cutoff": (str,),
            "last_updated": (str,),
            "lifecycle": (AiGatewayModelMetadataLifecycle,),
            "limits": (AiGatewayModelLimits,),
            "modalities": (AiGatewayModelModalities,),
            "open_weights": (bool,),
            "reasoning": (AiGatewayModelReasoning,),
            "reference_pricing": ([AiGatewayModelReferencePrice],),
            "release_date": (str,),
            "source": (AiGatewayModelMetadataSource,),
            "status": (AiGatewayModelMetadataStatus,),
        }

    attribute_map = {
        "capabilities": "capabilities",
        "description": "description",
        "display_name": "display_name",
        "family": "family",
        "kind": "kind",
        "knowledge_cutoff": "knowledge_cutoff",
        "last_updated": "last_updated",
        "lifecycle": "lifecycle",
        "limits": "limits",
        "modalities": "modalities",
        "open_weights": "open_weights",
        "reasoning": "reasoning",
        "reference_pricing": "reference_pricing",
        "release_date": "release_date",
        "source": "source",
        "status": "status",
    }

    def __init__(
        self_,
        capabilities: AiGatewayModelCapabilities,
        limits: AiGatewayModelLimits,
        modalities: AiGatewayModelModalities,
        source: AiGatewayModelMetadataSource,
        status: AiGatewayModelMetadataStatus,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        family: Union[str, UnsetType] = unset,
        kind: Union[AiGatewayModelMetadataKind, UnsetType] = unset,
        knowledge_cutoff: Union[str, UnsetType] = unset,
        last_updated: Union[str, UnsetType] = unset,
        lifecycle: Union[AiGatewayModelMetadataLifecycle, UnsetType] = unset,
        open_weights: Union[bool, UnsetType] = unset,
        reasoning: Union[AiGatewayModelReasoning, UnsetType] = unset,
        reference_pricing: Union[List[AiGatewayModelReferencePrice], UnsetType] = unset,
        release_date: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Optional, typed enrichment for a model catalog entry. Missing properties remain unknown.

        :param capabilities: Model features reported by the enrichment source. Omitted properties are unknown.
        :type capabilities: AiGatewayModelCapabilities

        :param description: Human-readable model description.
        :type description: str, optional

        :param display_name: Human-readable model name.
        :type display_name: str, optional

        :param family: Model family identifier.
        :type family: str, optional

        :param kind: Primary model kind. Decision models return a choice or score instead of generated text.
        :type kind: AiGatewayModelMetadataKind, optional

        :param knowledge_cutoff: Knowledge cutoff reported by the source.
        :type knowledge_cutoff: str, optional

        :param last_updated: Date the source record was last updated.
        :type last_updated: str, optional

        :param lifecycle: Model lifecycle state.
        :type lifecycle: AiGatewayModelMetadataLifecycle, optional

        :param limits: Token limits reported by the enrichment source.
        :type limits: AiGatewayModelLimits

        :param modalities: Supported model input and output modalities.
        :type modalities: AiGatewayModelModalities

        :param open_weights: Whether model weights are openly available.
        :type open_weights: bool, optional

        :param reasoning: Supported reasoning controls. Absence means controls are unknown or unavailable.
        :type reasoning: AiGatewayModelReasoning, optional

        :param reference_pricing: Provider-specific reference prices from the enrichment source. Omitted for shared canonical-model fallback matches. These do not determine gateway charges.
        :type reference_pricing: [AiGatewayModelReferencePrice], optional

        :param release_date: Model release date.
        :type release_date: str, optional

        :param source: Provenance for model metadata enrichment.
        :type source: AiGatewayModelMetadataSource

        :param status: Completeness of the matched source record. Partial also identifies metadata from a base model for a dated snapshot or from a shared canonical-model fallback.
        :type status: AiGatewayModelMetadataStatus
        """
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if family is not unset:
            kwargs["family"] = family
        if kind is not unset:
            kwargs["kind"] = kind
        if knowledge_cutoff is not unset:
            kwargs["knowledge_cutoff"] = knowledge_cutoff
        if last_updated is not unset:
            kwargs["last_updated"] = last_updated
        if lifecycle is not unset:
            kwargs["lifecycle"] = lifecycle
        if open_weights is not unset:
            kwargs["open_weights"] = open_weights
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if reference_pricing is not unset:
            kwargs["reference_pricing"] = reference_pricing
        if release_date is not unset:
            kwargs["release_date"] = release_date
        super().__init__(kwargs)

        self_.capabilities = capabilities
        self_.limits = limits
        self_.modalities = modalities
        self_.source = source
        self_.status = status
