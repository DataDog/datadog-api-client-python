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
    from datadog_api_client.v2.model.deployment_gate_response_data_attributes import (
        DeploymentGateResponseDataAttributes,
    )
    from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType


class DeploymentGateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_response_data_attributes import (
            DeploymentGateResponseDataAttributes,
        )
        from datadog_api_client.v2.model.deployment_gate_data_type import DeploymentGateDataType

        return {
            "attributes": (DeploymentGateResponseDataAttributes,),
            "id": (str,),
            "type": (DeploymentGateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: DeploymentGateResponseDataAttributes, id: str, type: DeploymentGateDataType, **kwargs
    ):
        """
        Data for a deployment gate.

        :param attributes: Basic information about a deployment gate.
        :type attributes: DeploymentGateResponseDataAttributes

        :param id: Unique identifier of the deployment gate.
        :type id: str

        :param type: Deployment gate resource type.
        :type type: DeploymentGateDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
