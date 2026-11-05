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
    from datadog_api_client.v2.model.security_agent_investigation_mitigation_action import (
        SecurityAgentInvestigationMitigationAction,
    )


class SecurityAgentInvestigationMitigationSuggestion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_mitigation_action import (
            SecurityAgentInvestigationMitigationAction,
        )

        return {
            "actions": ([SecurityAgentInvestigationMitigationAction],),
            "id": (str,),
            "rationale": (str,),
            "recommended": (bool,),
            "scope_note": (str,),
            "step": (int,),
            "title": (str,),
        }

    attribute_map = {
        "actions": "actions",
        "id": "id",
        "rationale": "rationale",
        "recommended": "recommended",
        "scope_note": "scope_note",
        "step": "step",
        "title": "title",
    }

    def __init__(
        self_,
        id: str,
        rationale: str,
        recommended: bool,
        step: int,
        title: str,
        actions: Union[List[SecurityAgentInvestigationMitigationAction], UnsetType] = unset,
        scope_note: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A suggested mitigation.

        :param actions: Actions that apply the mitigation.
        :type actions: [SecurityAgentInvestigationMitigationAction], optional

        :param id: ID of the mitigation.
        :type id: str

        :param rationale: Why the mitigation is suggested.
        :type rationale: str

        :param recommended: Whether the mitigation is recommended.
        :type recommended: bool

        :param scope_note: What the mitigation applies to.
        :type scope_note: str, optional

        :param step: Order in which to apply the mitigation, starting at 1.
        :type step: int

        :param title: Title of the mitigation.
        :type title: str
        """
        if actions is not unset:
            kwargs["actions"] = actions
        if scope_note is not unset:
            kwargs["scope_note"] = scope_note
        super().__init__(kwargs)

        self_.id = id
        self_.rationale = rationale
        self_.recommended = recommended
        self_.step = step
        self_.title = title
