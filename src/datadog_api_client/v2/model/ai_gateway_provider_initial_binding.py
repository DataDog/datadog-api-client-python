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
    from datadog_api_client.v2.model.ai_gateway_provider_initial_binding_relation import (
        AiGatewayProviderInitialBindingRelation,
    )


class AiGatewayProviderInitialBinding(ModelNormal):
    validations = {
        "principals": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_initial_binding_relation import (
            AiGatewayProviderInitialBindingRelation,
        )

        return {
            "principals": ([str],),
            "relation": (AiGatewayProviderInitialBindingRelation,),
        }

    attribute_map = {
        "principals": "principals",
        "relation": "relation",
    }

    def __init__(self_, principals: List[str], relation: AiGatewayProviderInitialBindingRelation, **kwargs):
        """
        Reserved initial provider access binding. Initial provider sharing is unavailable.

        :param principals: Access principals in type:id form.
        :type principals: [str]

        :param relation: Provider access relation. Editor also grants View.
        :type relation: AiGatewayProviderInitialBindingRelation
        """
        super().__init__(kwargs)

        self_.principals = principals
        self_.relation = relation
