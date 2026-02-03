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
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_state import (
        SecurityMonitoringSignalInvestigationState,
    )
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_step import (
        SecurityMonitoringSignalInvestigationStep,
    )


class SecurityMonitoringSignalInvestigationResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_state import (
            SecurityMonitoringSignalInvestigationState,
        )
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_step import (
            SecurityMonitoringSignalInvestigationStep,
        )

        return {
            "investigation_id": (str,),
            "rule_id": (str,),
            "signal_id": (str,),
            "state": (SecurityMonitoringSignalInvestigationState,),
            "step": (SecurityMonitoringSignalInvestigationStep,),
        }

    attribute_map = {
        "investigation_id": "investigation_id",
        "rule_id": "rule_id",
        "signal_id": "signal_id",
        "state": "state",
        "step": "step",
    }

    def __init__(
        self_,
        investigation_id: str,
        rule_id: str,
        signal_id: str,
        state: Union[SecurityMonitoringSignalInvestigationState, UnsetType] = unset,
        step: Union[SecurityMonitoringSignalInvestigationStep, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a signal investigation response.

        :param investigation_id: The unique ID of the investigation.
        :type investigation_id: str

        :param rule_id: The ID of the rule that triggered the signal.
        :type rule_id: str

        :param signal_id: The unique ID of the security signal.
        :type signal_id: str

        :param state: The state of the investigation.
        :type state: SecurityMonitoringSignalInvestigationState, optional

        :param step: Information about an investigation step.
        :type step: SecurityMonitoringSignalInvestigationStep, optional
        """
        if state is not unset:
            kwargs["state"] = state
        if step is not unset:
            kwargs["step"] = step
        super().__init__(kwargs)

        self_.investigation_id = investigation_id
        self_.rule_id = rule_id
        self_.signal_id = signal_id
