# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_gate_evaluation_attributes import DeploymentGateEvaluationAttributes
    from datadog_api_client.v2.model.deployment_gate_evaluation_data_type import DeploymentGateEvaluationDataType


class DeploymentGateEvaluationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_evaluation_attributes import DeploymentGateEvaluationAttributes
        from datadog_api_client.v2.model.deployment_gate_evaluation_data_type import DeploymentGateEvaluationDataType

        return {
            "attributes": (DeploymentGateEvaluationAttributes,),
            "id": (UUID,),
            "type": (DeploymentGateEvaluationDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DeploymentGateEvaluationAttributes,
        id: UUID,
        type: DeploymentGateEvaluationDataType,
        **kwargs,
    ):
        """
        JSON:API deployment gate evaluation resource.

        :param attributes: Attributes of a deployment gate evaluation.
        :type attributes: DeploymentGateEvaluationAttributes

        :param id: Deployment gate evaluation UUID.
        :type id: UUID

        :param type: JSON:API type for a deployment gate evaluation.
        :type type: DeploymentGateEvaluationDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
