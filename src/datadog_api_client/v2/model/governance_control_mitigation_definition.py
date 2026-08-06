# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_control_parameter_definition import GovernanceControlParameterDefinition


class GovernanceControlMitigationDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_parameter_definition import (
            GovernanceControlParameterDefinition,
        )

        return {
            "description": (str,),
            "execution_modes": ([str],),
            "id": (str,),
            "permissions": ([str],),
            "supported_parameters": ([GovernanceControlParameterDefinition],),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "execution_modes": "execution_modes",
        "id": "id",
        "permissions": "permissions",
        "supported_parameters": "supported_parameters",
        "title": "title",
    }

    def __init__(
        self_,
        description: str,
        execution_modes: List[str],
        id: str,
        permissions: List[str],
        supported_parameters: List[GovernanceControlParameterDefinition],
        title: str,
        **kwargs,
    ):
        """
        The definition of a mitigation available for a control.

        :param description: A human-readable description of the mitigation.
        :type description: str

        :param execution_modes: The execution modes the mitigation supports, such as ``manual`` or ``automatic``.
        :type execution_modes: [str]

        :param id: The unique identifier of the mitigation.
        :type id: str

        :param permissions: The permissions required to apply the mitigation.
        :type permissions: [str]

        :param supported_parameters: An array of parameter definitions.
        :type supported_parameters: [GovernanceControlParameterDefinition]

        :param title: A short, human-readable name for the mitigation.
        :type title: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.execution_modes = execution_modes
        self_.id = id
        self_.permissions = permissions
        self_.supported_parameters = supported_parameters
        self_.title = title
