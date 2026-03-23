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
    from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
        DeploymentGatesEvaluationResultResponseAttributesGateStatus,
    )


class DeploymentGatesRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
            DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        )

        return {
            "dry_run": (bool,),
            "name": (str,),
            "reason": (str,),
            "status": (DeploymentGatesEvaluationResultResponseAttributesGateStatus,),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "name": "name",
        "reason": "reason",
        "status": "status",
    }

    def __init__(
        self_,
        dry_run: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        reason: Union[str, UnsetType] = unset,
        status: Union[DeploymentGatesEvaluationResultResponseAttributesGateStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        The result of a single rule evaluation.

        :param dry_run: Whether this rule was evaluated in dry-run mode.
        :type dry_run: bool, optional

        :param name: The name of the rule.
        :type name: str, optional

        :param reason: The reason for the rule result, if applicable.
        :type reason: str, optional

        :param status: The overall status of the gate evaluation.

            * ``in_progress`` : The evaluation is still running.
            * ``pass`` : All rules passed successfully and the deployment is allowed to proceed.
            * ``fail`` : One or more rules did not pass; the deployment should not proceed.
        :type status: DeploymentGatesEvaluationResultResponseAttributesGateStatus, optional
        """
        if dry_run is not unset:
            kwargs["dry_run"] = dry_run
        if name is not unset:
            kwargs["name"] = name
        if reason is not unset:
            kwargs["reason"] = reason
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
