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
    from datadog_api_client.v2.model.csm_agents_attributes import CsmAgentsAttributes
    from datadog_api_client.v2.model.csm_agents_type import CSMAgentsType


class CsmAgentData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_agents_attributes import CsmAgentsAttributes
        from datadog_api_client.v2.model.csm_agents_type import CSMAgentsType

        return {
            "attributes": (CsmAgentsAttributes,),
            "id": (str,),
            "type": (CSMAgentsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CsmAgentsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CSMAgentsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Single Agent Data.

        :param attributes: A CSM Agent returned by the API.
        :type attributes: CsmAgentsAttributes, optional

        :param id: The ID of the Agent.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``datadog_agent``.
        :type type: CSMAgentsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
