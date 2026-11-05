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
    from datadog_api_client.v2.model.security_agent_investigation_attributes import SecurityAgentInvestigationAttributes
    from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType


class SecurityAgentInvestigationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_attributes import (
            SecurityAgentInvestigationAttributes,
        )
        from datadog_api_client.v2.model.security_agent_investigation_type import SecurityAgentInvestigationType

        return {
            "attributes": (SecurityAgentInvestigationAttributes,),
            "id": (str,),
            "type": (SecurityAgentInvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: SecurityAgentInvestigationType,
        attributes: Union[SecurityAgentInvestigationAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        An investigation and its content. ``attributes`` is absent when ``fields[investigations]`` is empty or lists
        only attributes the investigation doesn't have.

        :param attributes: Attributes of an investigation. When ``fields[investigations]`` is set, only listed attributes are returned.
            Attributes the investigation doesn't have yet are absent.
        :type attributes: SecurityAgentInvestigationAttributes, optional

        :param id: The ID of the investigation.
        :type id: str

        :param type: Type of the investigation resource.
        :type type: SecurityAgentInvestigationType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
