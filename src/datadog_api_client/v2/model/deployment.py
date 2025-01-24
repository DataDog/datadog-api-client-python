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
    from datadog_api_client.v2.model.deployment_attributes import DeploymentAttributes
    from datadog_api_client.v2.model.deployment_metadata import DeploymentMetadata
    from datadog_api_client.v2.model.app_deployment_type import AppDeploymentType


class Deployment(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_attributes import DeploymentAttributes
        from datadog_api_client.v2.model.deployment_metadata import DeploymentMetadata
        from datadog_api_client.v2.model.app_deployment_type import AppDeploymentType

        return {
            "attributes": (DeploymentAttributes,),
            "id": (UUID,),
            "meta": (DeploymentMetadata,),
            "type": (AppDeploymentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DeploymentAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        meta: Union[DeploymentMetadata, UnsetType] = unset,
        type: Union[AppDeploymentType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The version of the app that was published.

        :param attributes: The attributes object containing the version ID of the published app.
        :type attributes: DeploymentAttributes, optional

        :param id: The deployment ID.
        :type id: UUID, optional

        :param meta: Metadata object containing the publication creation information.
        :type meta: DeploymentMetadata, optional

        :param type: The deployment type.
        :type type: AppDeploymentType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
