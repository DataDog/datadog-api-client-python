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
    from datadog_api_client.v2.model.entity_response_included_related_oncall_escalation_item import (
        EntityResponseIncludedRelatedOncallEscalationItem,
    )


class EntityResponseIncludedRelatedOncallAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_included_related_oncall_escalation_item import (
            EntityResponseIncludedRelatedOncallEscalationItem,
        )

        return {
            "escalations": ([EntityResponseIncludedRelatedOncallEscalationItem],),
            "provider": (str,),
        }

    attribute_map = {
        "escalations": "escalations",
        "provider": "provider",
    }

    def __init__(
        self_,
        escalations: Union[List[EntityResponseIncludedRelatedOncallEscalationItem], UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included related oncall attributes.

        :param escalations: Oncall escalations.
        :type escalations: [EntityResponseIncludedRelatedOncallEscalationItem], optional

        :param provider: Oncall provider.
        :type provider: str, optional
        """
        if escalations is not unset:
            kwargs["escalations"] = escalations
        if provider is not unset:
            kwargs["provider"] = provider
        super().__init__(kwargs)
