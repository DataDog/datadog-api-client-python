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
    from datadog_api_client.v2.model.security_agent_investigation_no_run_reason import (
        SecurityAgentInvestigationNoRunReason,
    )


class SecurityAgentInvestigationsListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_investigation_no_run_reason import (
            SecurityAgentInvestigationNoRunReason,
        )

        return {
            "reason": (SecurityAgentInvestigationNoRunReason,),
            "total_count": (int,),
        }

    attribute_map = {
        "reason": "reason",
        "total_count": "total_count",
    }

    def __init__(
        self_, total_count: int, reason: Union[SecurityAgentInvestigationNoRunReason, UnsetType] = unset, **kwargs
    ):
        """
        Metadata of a page of investigations.

        :param reason: Why ``filter[signal_id]`` returned no investigation. Set only on the first page of an empty result. The reason is
            based on the organization's current settings. Poll again only on ``investigation_not_started`` , after the number
            of seconds in the ``Retry-After`` header; treat the others as final for this signal.

            * ``investigation_not_started`` : no investigation has started yet, but one may still start.
            * ``not_investigated`` : no investigation started within an hour of the signal, so none is expected. The signal
              was skipped for a reason this API doesn't report, such as its severity or a rate limit.
            * ``rule_not_enabled`` : the signal's detection rule doesn't have Bits Security Analyst enabled, so no
              investigation starts automatically.
            * ``signal_not_found`` : the ID isn't a signal ID, or no signal with this ID exists in the organization.
            * ``org_not_activated`` : the organization hasn't activated Bits Security Analyst.
        :type reason: SecurityAgentInvestigationNoRunReason, optional

        :param total_count: Without ``filter[signal_id]`` , the number of signals that match the filters. With ``filter[signal_id]`` , the
            number of investigations of that signal. Pages past the last page return 0.
        :type total_count: int
        """
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)

        self_.total_count = total_count
