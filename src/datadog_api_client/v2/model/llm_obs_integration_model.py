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
    from datadog_api_client.v2.model.llm_obs_integration_model_region_prefix_overrides import (
        LLMObsIntegrationModelRegionPrefixOverrides,
    )


class LLMObsIntegrationModel(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_integration_model_region_prefix_overrides import (
            LLMObsIntegrationModelRegionPrefixOverrides,
        )

        return {
            "has_access": (bool,),
            "id": (str,),
            "integration": (str,),
            "integration_display_name": (str,),
            "json_schema": (bool,),
            "model_display_name": (str,),
            "model_id": (str,),
            "provider": (str,),
            "provider_display_name": (str,),
            "region_prefix_overrides": (LLMObsIntegrationModelRegionPrefixOverrides,),
        }

    attribute_map = {
        "has_access": "has_access",
        "id": "id",
        "integration": "integration",
        "integration_display_name": "integration_display_name",
        "json_schema": "json_schema",
        "model_display_name": "model_display_name",
        "model_id": "model_id",
        "provider": "provider",
        "provider_display_name": "provider_display_name",
        "region_prefix_overrides": "region_prefix_overrides",
    }

    def __init__(
        self_,
        has_access: bool,
        id: str,
        integration: str,
        integration_display_name: str,
        json_schema: bool,
        model_display_name: str,
        model_id: str,
        provider: str,
        provider_display_name: str,
        region_prefix_overrides: Union[LLMObsIntegrationModelRegionPrefixOverrides, UnsetType] = unset,
        **kwargs,
    ):
        """
        A model available for a given LLM provider integration and account.

        :param has_access: Whether the account has access to this model.
        :type has_access: bool

        :param id: Unique identifier for the model entry.
        :type id: str

        :param integration: The name of the LLM provider integration.
        :type integration: str

        :param integration_display_name: Human-readable name of the LLM provider integration.
        :type integration_display_name: str

        :param json_schema: Whether the model supports structured output via JSON schema.
        :type json_schema: bool

        :param model_display_name: Human-readable model name.
        :type model_display_name: str

        :param model_id: Provider-specific model identifier used in inference calls.
        :type model_id: str

        :param provider: The underlying model provider.
        :type provider: str

        :param provider_display_name: Human-readable name of the underlying model provider.
        :type provider_display_name: str

        :param region_prefix_overrides: Map of region-specific model ID prefix overrides.
        :type region_prefix_overrides: LLMObsIntegrationModelRegionPrefixOverrides, optional
        """
        if region_prefix_overrides is not unset:
            kwargs["region_prefix_overrides"] = region_prefix_overrides
        super().__init__(kwargs)

        self_.has_access = has_access
        self_.id = id
        self_.integration = integration
        self_.integration_display_name = integration_display_name
        self_.json_schema = json_schema
        self_.model_display_name = model_display_name
        self_.model_id = model_id
        self_.provider = provider
        self_.provider_display_name = provider_display_name
