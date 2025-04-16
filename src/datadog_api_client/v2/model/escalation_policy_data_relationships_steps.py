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
    from datadog_api_client.v2.model.escalation_policy_data_relationships_steps_data_items import (
        EscalationPolicyDataRelationshipsStepsDataItems,
    )


class EscalationPolicyDataRelationshipsSteps(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_data_relationships_steps_data_items import (
            EscalationPolicyDataRelationshipsStepsDataItems,
        )

        return {
            "data": ([EscalationPolicyDataRelationshipsStepsDataItems],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_, data: Union[List[EscalationPolicyDataRelationshipsStepsDataItems], UnsetType] = unset, **kwargs
    ):
        """
        Defines the relationship to a collection of steps within an escalation policy. Contains an array of step data references.

        :param data: An array of references to the steps defined in this escalation policy.
        :type data: [EscalationPolicyDataRelationshipsStepsDataItems], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
