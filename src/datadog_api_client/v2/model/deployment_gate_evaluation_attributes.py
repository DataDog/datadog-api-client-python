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
    from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
        DeploymentGatesEvaluationResultResponseAttributesGateStatus,
    )


class DeploymentGateEvaluationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes_gate_status import (
            DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        )

        return {
            "dry_run": (bool,),
            "duration_seconds": (int, none_type),
            "env": (str,),
            "evaluation_id": (UUID,),
            "finished_at": (datetime, none_type),
            "gate_id": (UUID, none_type),
            "identifier": (str,),
            "service": (str,),
            "started_at": (datetime,),
            "status": (DeploymentGatesEvaluationResultResponseAttributesGateStatus,),
            "version": (str,),
        }

    attribute_map = {
        "dry_run": "dry_run",
        "duration_seconds": "duration_seconds",
        "env": "env",
        "evaluation_id": "evaluation_id",
        "finished_at": "finished_at",
        "gate_id": "gate_id",
        "identifier": "identifier",
        "service": "service",
        "started_at": "started_at",
        "status": "status",
        "version": "version",
    }

    def __init__(
        self_,
        dry_run: bool,
        duration_seconds: Union[int, none_type],
        env: str,
        evaluation_id: UUID,
        finished_at: Union[datetime, none_type],
        gate_id: Union[UUID, none_type],
        identifier: str,
        service: str,
        started_at: datetime,
        status: DeploymentGatesEvaluationResultResponseAttributesGateStatus,
        version: str,
        **kwargs,
    ):
        """
        Attributes of a deployment gate evaluation.

        :param dry_run: Whether this evaluation used gate-level dry run.
        :type dry_run: bool

        :param duration_seconds: Evaluation duration in seconds. Null while it is in progress.
        :type duration_seconds: int, none_type

        :param env: Deployment environment evaluated by the gate.
        :type env: str

        :param evaluation_id: Gate evaluation UUID. Matches the resource ``id``.
        :type evaluation_id: UUID

        :param finished_at: Time the evaluation finished. Null while it is in progress.
        :type finished_at: datetime, none_type

        :param gate_id: Configured deployment gate UUID. Null for just-in-time evaluations.
        :type gate_id: UUID, none_type

        :param identifier: Deployment gate identifier.
        :type identifier: str

        :param service: Service evaluated by the deployment gate.
        :type service: str

        :param started_at: Time the evaluation started.
        :type started_at: datetime

        :param status: The recorded result of a gate or rule evaluation.

            * ``in_progress`` : The evaluation is still running.
            * ``pass`` : All rules passed successfully.
            * ``fail`` : One or more rules did not pass.
        :type status: DeploymentGatesEvaluationResultResponseAttributesGateStatus

        :param version: Evaluated deployment version. Empty when no version was provided.
        :type version: str
        """
        super().__init__(kwargs)

        self_.dry_run = dry_run
        self_.duration_seconds = duration_seconds
        self_.env = env
        self_.evaluation_id = evaluation_id
        self_.finished_at = finished_at
        self_.gate_id = gate_id
        self_.identifier = identifier
        self_.service = service
        self_.started_at = started_at
        self_.status = status
        self_.version = version
