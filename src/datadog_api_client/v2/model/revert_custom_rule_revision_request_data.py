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
    from datadog_api_client.v2.model.revert_custom_rule_revision_request_data_attributes import (
        RevertCustomRuleRevisionRequestDataAttributes,
    )
    from datadog_api_client.v2.model.revert_custom_rule_revision_data_type import RevertCustomRuleRevisionDataType


class RevertCustomRuleRevisionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.revert_custom_rule_revision_request_data_attributes import (
            RevertCustomRuleRevisionRequestDataAttributes,
        )
        from datadog_api_client.v2.model.revert_custom_rule_revision_data_type import RevertCustomRuleRevisionDataType

        return {
            "attributes": (RevertCustomRuleRevisionRequestDataAttributes,),
            "id": (str,),
            "type": (RevertCustomRuleRevisionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RevertCustomRuleRevisionRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[RevertCustomRuleRevisionDataType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: RevertCustomRuleRevisionRequestDataAttributes, optional

        :param id: Request identifier
        :type id: str, optional

        :param type: Request type
        :type type: RevertCustomRuleRevisionDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
