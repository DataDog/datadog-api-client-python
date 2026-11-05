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
    from datadog_api_client.v2.model.ai_gateway_provider_resource import AiGatewayProviderResource
    from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_resource import AiGatewayModelCatalogEntryResource


class AiGatewayProviderResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_resource import AiGatewayProviderResource
        from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_resource import (
            AiGatewayModelCatalogEntryResource,
        )

        return {
            "data": (AiGatewayProviderResource,),
            "included": ([AiGatewayModelCatalogEntryResource],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: AiGatewayProviderResource,
        included: Union[List[AiGatewayModelCatalogEntryResource], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing one AI Gateway provider.

        :param data: AI Gateway provider resource.
        :type data: AiGatewayProviderResource

        :param included: Model catalog entries created with the provider.
        :type included: [AiGatewayModelCatalogEntryResource], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
