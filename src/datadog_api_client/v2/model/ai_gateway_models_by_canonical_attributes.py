# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_provider_model_entry import AiGatewayProviderModelEntry


class AiGatewayModelsByCanonicalAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_model_entry import AiGatewayProviderModelEntry

        return {
            "model_id_canonical": (str,),
            "providers": ([AiGatewayProviderModelEntry],),
        }

    attribute_map = {
        "model_id_canonical": "model_id_canonical",
        "providers": "providers",
    }

    def __init__(self_, model_id_canonical: str, providers: List[AiGatewayProviderModelEntry], **kwargs):
        """
        Provider entries grouped under one canonical model ID.

        :param model_id_canonical: Provider-independent model identifier.
        :type model_id_canonical: str

        :param providers:
        :type providers: [AiGatewayProviderModelEntry]
        """
        super().__init__(kwargs)

        self_.model_id_canonical = model_id_canonical
        self_.providers = providers
