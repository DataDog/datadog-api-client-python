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
    from datadog_api_client.v2.model.deployment_gates_evaluation_request_attributes import (
        DeploymentGatesEvaluationRequestAttributes,
    )
    from datadog_api_client.v2.model.deployment_gates_evaluation_request_data_type import (
        DeploymentGatesEvaluationRequestDataType,
    )


class DeploymentGatesEvaluationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_request_attributes import (
            DeploymentGatesEvaluationRequestAttributes,
        )
        from datadog_api_client.v2.model.deployment_gates_evaluation_request_data_type import (
            DeploymentGatesEvaluationRequestDataType,
        )

        return {
            "attributes": (DeploymentGatesEvaluationRequestAttributes,),
            "type": (DeploymentGatesEvaluationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DeploymentGatesEvaluationRequestAttributes,
        type: DeploymentGatesEvaluationRequestDataType,
        **kwargs,
    ):
        """
        Data for a deployment gate evaluation request.

        :param attributes: Attributes for a deployment gate evaluation request.
        :type attributes: DeploymentGatesEvaluationRequestAttributes

        :param type: JSON:API type for a deployment gate evaluation request.
        :type type: DeploymentGatesEvaluationRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
