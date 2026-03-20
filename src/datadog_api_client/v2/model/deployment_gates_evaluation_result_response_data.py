# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes import (
        DeploymentGatesEvaluationResultResponseAttributes,
    )
    from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_data_type import (
        DeploymentGatesEvaluationResultResponseDataType,
    )


class DeploymentGatesEvaluationResultResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_attributes import (
            DeploymentGatesEvaluationResultResponseAttributes,
        )
        from datadog_api_client.v2.model.deployment_gates_evaluation_result_response_data_type import (
            DeploymentGatesEvaluationResultResponseDataType,
        )

        return {
            "attributes": (DeploymentGatesEvaluationResultResponseAttributes,),
            "id": (str,),
            "type": (DeploymentGatesEvaluationResultResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DeploymentGatesEvaluationResultResponseAttributes,
        id: str,
        type: DeploymentGatesEvaluationResultResponseDataType,
        **kwargs,
    ):
        """
        Data for a deployment gate evaluation result response.

        :param attributes: Attributes for a deployment gate evaluation result response.
        :type attributes: DeploymentGatesEvaluationResultResponseAttributes

        :param id: The unique identifier of the evaluation.
        :type id: str

        :param type: JSON:API type for a deployment gate evaluation result response.
        :type type: DeploymentGatesEvaluationResultResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
