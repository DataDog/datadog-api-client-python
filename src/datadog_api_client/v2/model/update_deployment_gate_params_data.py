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
    from datadog_api_client.v2.model.update_deployment_gate_params_data_attributes import (
        UpdateDeploymentGateParamsDataAttributes,
    )
    from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType


class UpdateDeploymentGateParamsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_deployment_gate_params_data_attributes import (
            UpdateDeploymentGateParamsDataAttributes,
        )
        from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType

        return {
            "attributes": (UpdateDeploymentGateParamsDataAttributes,),
            "id": (str,),
            "type": (DeploymentGateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: UpdateDeploymentGateParamsDataAttributes, id: str, type: DeploymentGateDataType, **kwargs
    ):
        """
        Parameters for updating a deployment gate.

        :param attributes: Attributes for updating a deployment gate.
        :type attributes: UpdateDeploymentGateParamsDataAttributes

        :param id: Unique identifier of the deployment gate.
        :type id: str

        :param type: Deployment gate resource type.
        :type type: DeploymentGateDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
