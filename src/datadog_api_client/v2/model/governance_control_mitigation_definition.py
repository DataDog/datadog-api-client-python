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
    from datadog_api_client.v2.model.governance_control_parameter_definition import GovernanceControlParameterDefinition


class GovernanceControlMitigationDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_parameter_definition import (
            GovernanceControlParameterDefinition,
        )

        return {
            "action_verb": (str,),
            "description": (str,),
            "execution_modes": ([str],),
            "feature_flags": ([str],),
            "id": (str,),
            "manual_mitigation_warning": (str,),
            "permissions": ([str],),
            "requires_ai": (bool,),
            "supported_parameters": ([GovernanceControlParameterDefinition],),
            "title": (str,),
        }

    attribute_map = {
        "action_verb": "action_verb",
        "description": "description",
        "execution_modes": "execution_modes",
        "feature_flags": "feature_flags",
        "id": "id",
        "manual_mitigation_warning": "manual_mitigation_warning",
        "permissions": "permissions",
        "requires_ai": "requires_ai",
        "supported_parameters": "supported_parameters",
        "title": "title",
    }

    def __init__(
        self_,
        action_verb: str,
        description: str,
        feature_flags: List[str],
        id: str,
        manual_mitigation_warning: str,
        permissions: List[str],
        requires_ai: bool,
        supported_parameters: List[GovernanceControlParameterDefinition],
        title: str,
        execution_modes: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of a mitigation available for a control.

        :param action_verb: The verb describing the mitigation action, such as ``revoke`` or ``delete``.
        :type action_verb: str

        :param description: A human-readable description of the mitigation.
        :type description: str

        :param execution_modes: The execution modes the mitigation supports, such as ``manual`` or ``automatic``.
        :type execution_modes: [str], optional

        :param feature_flags: The feature flags that gate the mitigation.
        :type feature_flags: [str]

        :param id: The unique identifier of the mitigation.
        :type id: str

        :param manual_mitigation_warning: A warning shown to the user before applying the mitigation manually.
        :type manual_mitigation_warning: str

        :param permissions: The permissions required to apply the mitigation.
        :type permissions: [str]

        :param requires_ai: Whether the mitigation requires AI to be enabled.
        :type requires_ai: bool

        :param supported_parameters: An array of parameter definitions.
        :type supported_parameters: [GovernanceControlParameterDefinition]

        :param title: A short, human-readable name for the mitigation.
        :type title: str
        """
        if execution_modes is not unset:
            kwargs["execution_modes"] = execution_modes
        super().__init__(kwargs)

        self_.action_verb = action_verb
        self_.description = description
        self_.feature_flags = feature_flags
        self_.id = id
        self_.manual_mitigation_warning = manual_mitigation_warning
        self_.permissions = permissions
        self_.requires_ai = requires_ai
        self_.supported_parameters = supported_parameters
        self_.title = title
