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
    from datadog_api_client.v2.model.ai_gateway_model_group_binding_relation import AiGatewayModelGroupBindingRelation


class AiGatewayModelGroupBinding(ModelNormal):
    validations = {
        "principals": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_group_binding_relation import (
            AiGatewayModelGroupBindingRelation,
        )

        return {
            "principals": ([str],),
            "relation": (AiGatewayModelGroupBindingRelation,),
        }

    attribute_map = {
        "principals": "principals",
        "relation": "relation",
    }

    def __init__(self_, principals: List[str], relation: AiGatewayModelGroupBindingRelation, **kwargs):
        """
        Initial access binding for an AI Gateway model group.

        :param principals: Principals granted the relation.
        :type principals: [str]

        :param relation: Access relation granted on a model group.
        :type relation: AiGatewayModelGroupBindingRelation
        """
        super().__init__(kwargs)

        self_.principals = principals
        self_.relation = relation
