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
    from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes_steps_items import (
        EscalationPolicyUpdateRequestDataAttributesStepsItems,
    )


class EscalationPolicyUpdateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes_steps_items import (
            EscalationPolicyUpdateRequestDataAttributesStepsItems,
        )

        return {
            "name": (str,),
            "resolve_page_on_policy_end": (bool,),
            "retries": (int,),
            "steps": ([EscalationPolicyUpdateRequestDataAttributesStepsItems],),
        }

    attribute_map = {
        "name": "name",
        "resolve_page_on_policy_end": "resolve_page_on_policy_end",
        "retries": "retries",
        "steps": "steps",
    }

    def __init__(
        self_,
        name: str,
        steps: List[EscalationPolicyUpdateRequestDataAttributesStepsItems],
        resolve_page_on_policy_end: Union[bool, UnsetType] = unset,
        retries: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the attributes that can be updated for an escalation policy, such as description, name, resolution behavior, retries, and steps.

        :param name: Specifies the name of the escalation policy.
        :type name: str

        :param resolve_page_on_policy_end: Indicates whether the page is automatically resolved when the policy ends.
        :type resolve_page_on_policy_end: bool, optional

        :param retries: Specifies how many times the escalation sequence is retried if there is no response.
        :type retries: int, optional

        :param steps: A list of escalation steps, each defining assignment, escalation timeout, and targets.
        :type steps: [EscalationPolicyUpdateRequestDataAttributesStepsItems]
        """
        if resolve_page_on_policy_end is not unset:
            kwargs["resolve_page_on_policy_end"] = resolve_page_on_policy_end
        if retries is not unset:
            kwargs["retries"] = retries
        super().__init__(kwargs)

        self_.name = name
        self_.steps = steps
