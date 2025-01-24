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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_relationship_data import DeploymentRelationshipData
    from datadog_api_client.v2.model.deployment_metadata import DeploymentMetadata


class DeploymentRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_relationship_data import DeploymentRelationshipData
        from datadog_api_client.v2.model.deployment_metadata import DeploymentMetadata

        return {
            "data": (DeploymentRelationshipData,),
            "meta": (DeploymentMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[DeploymentRelationshipData, UnsetType] = unset,
        meta: Union[DeploymentMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information pointing to the app's publication status.

        :param data: Data object containing the deployment ID.
        :type data: DeploymentRelationshipData, optional

        :param meta: Metadata object containing the publication creation information.
        :type meta: DeploymentMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
