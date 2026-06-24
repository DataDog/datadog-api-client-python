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
    from datadog_api_client.v2.model.governance_control_update_attributes import GovernanceControlUpdateAttributes
    from datadog_api_client.v2.model.governance_control_resource_type import GovernanceControlResourceType


class GovernanceControlUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_update_attributes import GovernanceControlUpdateAttributes
        from datadog_api_client.v2.model.governance_control_resource_type import GovernanceControlResourceType

        return {
            "attributes": (GovernanceControlUpdateAttributes,),
            "id": (str,),
            "type": (GovernanceControlResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: GovernanceControlResourceType,
        attributes: Union[GovernanceControlUpdateAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data of a governance control update request.

        :param attributes: The attributes of a governance control that can be updated. Only the attributes present in the request are modified.
        :type attributes: GovernanceControlUpdateAttributes, optional

        :param id: The unique identifier of the control.
        :type id: str, optional

        :param type: JSON:API resource type for a governance control.
        :type type: GovernanceControlResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
