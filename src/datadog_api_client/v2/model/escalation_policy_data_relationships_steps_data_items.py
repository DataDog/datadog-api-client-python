# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.escalation_policy_data_relationships_steps_data_items_type import (
        EscalationPolicyDataRelationshipsStepsDataItemsType,
    )


class EscalationPolicyDataRelationshipsStepsDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_data_relationships_steps_data_items_type import (
            EscalationPolicyDataRelationshipsStepsDataItemsType,
        )

        return {
            "id": (str,),
            "type": (EscalationPolicyDataRelationshipsStepsDataItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: EscalationPolicyDataRelationshipsStepsDataItemsType, **kwargs):
        """
        Defines a relationship to a single step within an escalation policy. Contains the step's ``id`` and ``type``.

        :param id: Specifies the unique identifier for the step resource.
        :type id: str

        :param type: Indicates that the resource is of type ``steps``.
        :type type: EscalationPolicyDataRelationshipsStepsDataItemsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
