# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
        DeploymentGatesEvaluationResultResponseAttributesGateStatus,
    )
    from datadog_api_client.v2.model.deployment_gates_rule_response import DeploymentGatesRuleResponse


class DeploymentGatesEvaluationResultResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
            DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        )
        from datadog_api_client.v2.model.deployment_gates_rule_response import DeploymentGatesRuleResponse

        return {
            "dry_run": (bool,),
            "evaluation_id": (str,),
            "evaluation_url": (str,),
            "gate_id": (UUID,),
            "gate_status": (DeploymentGatesEvaluationResultResponseAttributesGateStatus,),
            "rules": ([DeploymentGatesRuleResponse],),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "evaluation_id": "evaluation_id",
        "evaluation_url": "evaluation_url",
        "gate_id": "gate_id",
        "gate_status": "gate_status",
        "rules": "rules",
    }

    def __init__(
        self_,
        dry_run: bool,
        evaluation_id: str,
        evaluation_url: str,
        gate_id: UUID,
        gate_status: DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        rules: List[DeploymentGatesRuleResponse],
        **kwargs,
    ):
        """
        Attributes for a deployment gate evaluation result response.

        :param dry_run: Whether the gate was evaluated in dry-run mode.
        :type dry_run: bool

        :param evaluation_id: The unique identifier of the gate evaluation.
        :type evaluation_id: str

        :param evaluation_url: A URL to view the evaluation details in the Datadog UI.
        :type evaluation_url: str

        :param gate_id: The unique identifier of the deployment gate.
        :type gate_id: UUID

        :param gate_status: The overall status of the gate evaluation.

            * ``in_progress`` : The evaluation is still running.
            * ``pass`` : All rules passed successfully and the deployment is allowed to proceed.
            * ``fail`` : One or more rules did not pass; the deployment should not proceed.
        :type gate_status: DeploymentGatesEvaluationResultResponseAttributesGateStatus

        :param rules: The results of individual rule evaluations.
        :type rules: [DeploymentGatesRuleResponse]
        """
        super().__init__(kwargs)

        self_.dry_run = dry_run
        self_.evaluation_id = evaluation_id
        self_.evaluation_url = evaluation_url
        self_.gate_id = gate_id
        self_.gate_status = gate_status
        self_.rules = rules
