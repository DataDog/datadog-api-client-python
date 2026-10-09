# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_gate_rule_evaluation_configuration import (
        DeploymentGateRuleEvaluationConfiguration,
    )
    from datadog_api_client.v2.model.deployment_gate_rule_failures import DeploymentGateRuleFailures
    from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
        DeploymentGatesEvaluationResultResponseAttributesGateStatus,
    )
    from datadog_api_client.v2.model.deployment_gate_rule_evaluation_type import DeploymentGateRuleEvaluationType


class DeploymentGateRuleEvaluationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_rule_evaluation_configuration import (
            DeploymentGateRuleEvaluationConfiguration,
        )
        from datadog_api_client.v2.model.deployment_gate_rule_failures import DeploymentGateRuleFailures
        from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
            DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        )
        from datadog_api_client.v2.model.deployment_gate_rule_evaluation_type import DeploymentGateRuleEvaluationType

        return {
            "configuration": (DeploymentGateRuleEvaluationConfiguration,),
            "dry_run": (bool,),
            "duration_seconds": (int, none_type),
            "env": (str,),
            "evaluation_id": (UUID,),
            "failures": (DeploymentGateRuleFailures,),
            "finished_at": (datetime, none_type),
            "gate_dry_run": (bool,),
            "gate_evaluation_id": (UUID,),
            "gate_id": (UUID, none_type),
            "identifier": (str,),
            "name": (str,),
            "reason": (str,),
            "rule_id": (UUID, none_type),
            "service": (str,),
            "started_at": (datetime,),
            "status": (DeploymentGatesEvaluationResultResponseAttributesGateStatus,),
            "type": (DeploymentGateRuleEvaluationType,),
            "version": (str,),
        }

    attribute_map = {
        "configuration": "configuration",
        "dry_run": "dry_run",
        "duration_seconds": "duration_seconds",
        "env": "env",
        "evaluation_id": "evaluation_id",
        "failures": "failures",
        "finished_at": "finished_at",
        "gate_dry_run": "gate_dry_run",
        "gate_evaluation_id": "gate_evaluation_id",
        "gate_id": "gate_id",
        "identifier": "identifier",
        "name": "name",
        "reason": "reason",
        "rule_id": "rule_id",
        "service": "service",
        "started_at": "started_at",
        "status": "status",
        "type": "type",
        "version": "version",
    }

    def __init__(
        self_,
        configuration: DeploymentGateRuleEvaluationConfiguration,
        dry_run: bool,
        duration_seconds: Union[int, none_type],
        env: str,
        evaluation_id: UUID,
        failures: DeploymentGateRuleFailures,
        finished_at: Union[datetime, none_type],
        gate_dry_run: bool,
        gate_evaluation_id: UUID,
        gate_id: Union[UUID, none_type],
        identifier: str,
        name: str,
        reason: str,
        rule_id: Union[UUID, none_type],
        service: str,
        started_at: datetime,
        status: DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        type: DeploymentGateRuleEvaluationType,
        version: str,
        **kwargs,
    ):
        """
        Attributes of a deployment gate rule evaluation.

        :param configuration: Evaluated rule configuration. Fields depend on rule type and unset fields are omitted.
            Monitor rules can include ``duration`` , ``query`` , ``monitor_ids`` , ``warmup`` , ``fail_on_no_groups_found`` , and ``fail_on_no_data``.
            Faulty deployment detection rules can include ``duration`` , ``allowed_resources`` , and ``excluded_resources``.
        :type configuration: DeploymentGateRuleEvaluationConfiguration

        :param dry_run: Whether this rule is non-enforcing. A failed dry-run rule is ignored when computing the gate outcome. Independent of ``gate_dry_run``.
        :type dry_run: bool

        :param duration_seconds: Rule evaluation duration in seconds. Null while it is in progress.
        :type duration_seconds: int, none_type

        :param env: Evaluated environment.
        :type env: str

        :param evaluation_id: Rule evaluation UUID. Matches the resource ``id``.
        :type evaluation_id: UUID

        :param failures: Rule failure details.
        :type failures: DeploymentGateRuleFailures

        :param finished_at: Time the rule evaluation finished. Null while it is in progress.
        :type finished_at: datetime, none_type

        :param gate_dry_run: Whether the parent gate is dry-run. A failed dry-run gate blocks but does not stop deployment. Independent of rule-level ``dry_run``.
        :type gate_dry_run: bool

        :param gate_evaluation_id: Deployment gate evaluation UUID.
        :type gate_evaluation_id: UUID

        :param gate_id: Configured deployment gate UUID. Null for just-in-time evaluations.
        :type gate_id: UUID, none_type

        :param identifier: Deployment gate identifier.
        :type identifier: str

        :param name: Rule name.
        :type name: str

        :param reason: Reason for the rule result.
        :type reason: str

        :param rule_id: Configured deployment rule UUID. Null for just-in-time rules.
        :type rule_id: UUID, none_type

        :param service: Evaluated service.
        :type service: str

        :param started_at: Time the rule evaluation started.
        :type started_at: datetime

        :param status: The recorded result of a gate or rule evaluation.

            * ``in_progress`` : The evaluation is still running.
            * ``pass`` : All rules passed successfully.
            * ``fail`` : One or more rules did not pass.
        :type status: DeploymentGatesEvaluationResultResponseAttributesGateStatus

        :param type: Type of deployment gate rule.
        :type type: DeploymentGateRuleEvaluationType

        :param version: Evaluated deployment version. Empty when no version was provided.
        :type version: str
        """
        super().__init__(kwargs)

        self_.configuration = configuration
        self_.dry_run = dry_run
        self_.duration_seconds = duration_seconds
        self_.env = env
        self_.evaluation_id = evaluation_id
        self_.failures = failures
        self_.finished_at = finished_at
        self_.gate_dry_run = gate_dry_run
        self_.gate_evaluation_id = gate_evaluation_id
        self_.gate_id = gate_id
        self_.identifier = identifier
        self_.name = name
        self_.reason = reason
        self_.rule_id = rule_id
        self_.service = service
        self_.started_at = started_at
        self_.status = status
        self_.type = type
        self_.version = version
