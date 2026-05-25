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
    from datadog_api_client.v2.model.ai_custom_rule_revision_request_attributes import (
        AiCustomRuleRevisionRequestAttributes,
    )
    from datadog_api_client.v2.model.ai_custom_rule_revision_data_type import AiCustomRuleRevisionDataType


class AiCustomRuleRevisionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_rule_revision_request_attributes import (
            AiCustomRuleRevisionRequestAttributes,
        )
        from datadog_api_client.v2.model.ai_custom_rule_revision_data_type import AiCustomRuleRevisionDataType

        return {
            "attributes": (AiCustomRuleRevisionRequestAttributes,),
            "id": (str,),
            "type": (AiCustomRuleRevisionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AiCustomRuleRevisionRequestAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AiCustomRuleRevisionDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request data for creating an AI custom rule revision.

        :param attributes: Attributes for creating an AI custom rule revision.
        :type attributes: AiCustomRuleRevisionRequestAttributes, optional

        :param id: The revision identifier.
        :type id: str, optional

        :param type: AI custom rule revision resource type.
        :type type: AiCustomRuleRevisionDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
