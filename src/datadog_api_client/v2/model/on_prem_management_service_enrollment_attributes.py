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
    from datadog_api_client.v2.model.on_prem_management_service_enrollment_attributes_runner_modes_items import (
        OnPremManagementServiceEnrollmentAttributesRunnerModesItems,
    )


class OnPremManagementServiceEnrollmentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_enrollment_attributes_runner_modes_items import (
            OnPremManagementServiceEnrollmentAttributesRunnerModesItems,
        )

        return {
            "actions_allowlist": ([str],),
            "runner_host": (str,),
            "runner_modes": ([OnPremManagementServiceEnrollmentAttributesRunnerModesItems],),
            "runner_name": (str,),
        }

    attribute_map = {
        "actions_allowlist": "actions_allowlist",
        "runner_host": "runner_host",
        "runner_modes": "runner_modes",
        "runner_name": "runner_name",
    }

    def __init__(
        self_,
        actions_allowlist: List[str],
        runner_modes: List[OnPremManagementServiceEnrollmentAttributesRunnerModesItems],
        runner_name: str,
        runner_host: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an enrollment.

        :param actions_allowlist: List of allowed actions for the runner.
        :type actions_allowlist: [str]

        :param runner_host: The hostname for the runner. Required when push mode is enabled.
        :type runner_host: str, optional

        :param runner_modes: The modes the runner should operate in.
        :type runner_modes: [OnPremManagementServiceEnrollmentAttributesRunnerModesItems]

        :param runner_name: The name of the on-prem runner.
        :type runner_name: str
        """
        if runner_host is not unset:
            kwargs["runner_host"] = runner_host
        super().__init__(kwargs)

        self_.actions_allowlist = actions_allowlist
        self_.runner_modes = runner_modes
        self_.runner_name = runner_name
