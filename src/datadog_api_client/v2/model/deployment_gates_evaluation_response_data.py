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
    from datadog_api_client.v2.model.deployment_gates_evaluation_response_attributes import (
        DeploymentGatesEvaluationResponseAttributes,
    )
    from datadog_api_client.v2.model.deployment_gates_evaluation_response_data_type import (
        DeploymentGatesEvaluationResponseDataType,
    )


class DeploymentGatesEvaluationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_response_attributes import (
            DeploymentGatesEvaluationResponseAttributes,
        )
        from datadog_api_client.v2.model.deployment_gates_evaluation_response_data_type import (
            DeploymentGatesEvaluationResponseDataType,
        )

        return {
            "attributes": (DeploymentGatesEvaluationResponseAttributes,),
            "id": (UUID,),
            "type": (DeploymentGatesEvaluationResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DeploymentGatesEvaluationResponseAttributes,
        id: UUID,
        type: DeploymentGatesEvaluationResponseDataType,
        **kwargs,
    ):
        """
        Data for a deployment gate evaluation response.

        :param attributes: Attributes for a deployment gate evaluation response.
        :type attributes: DeploymentGatesEvaluationResponseAttributes

        :param id: The unique identifier of the evaluation response.
        :type id: UUID

        :param type: JSON:API type for a deployment gate evaluation response.
        :type type: DeploymentGatesEvaluationResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
