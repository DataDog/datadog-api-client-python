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
    from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items_targets_items_type import (
        EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType,
    )


class EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items_targets_items_type import (
            EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType,
        )

        return {
            "id": (str,),
            "type": (EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        type: Union[EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a single escalation target within a step for an escalation policy creation request. Contains ``id`` and ``type``.

        :param id: Specifies the unique identifier for this target.
        :type id: str, optional

        :param type: Specifies the type of escalation target (example ``users`` , ``schedules`` , or ``teams`` ).
        :type type: EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
