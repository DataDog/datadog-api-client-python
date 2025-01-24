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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_deployment_type import AppDeploymentType


class DeploymentRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_deployment_type import AppDeploymentType

        return {
            "id": (UUID,),
            "type": (AppDeploymentType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: Union[UUID, UnsetType] = unset, type: Union[AppDeploymentType, UnsetType] = unset, **kwargs
    ):
        """
        Data object containing the deployment ID.

        :param id: The deployment ID.
        :type id: UUID, optional

        :param type: The deployment type.
        :type type: AppDeploymentType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
