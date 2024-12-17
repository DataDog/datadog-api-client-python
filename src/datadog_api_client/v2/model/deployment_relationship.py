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
    from datadog_api_client.v2.model.deployment_relationship_meta import DeploymentRelationshipMeta


class DeploymentRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_relationship_data import DeploymentRelationshipData
        from datadog_api_client.v2.model.deployment_relationship_meta import DeploymentRelationshipMeta

        return {
            "data": (DeploymentRelationshipData,),
            "meta": (DeploymentRelationshipMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[DeploymentRelationshipData, UnsetType] = unset,
        meta: Union[DeploymentRelationshipMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``DeploymentRelationship`` object.

        :param data: The definition of ``DeploymentRelationshipData`` object.
        :type data: DeploymentRelationshipData, optional

        :param meta: The definition of ``DeploymentRelationshipMeta`` object.
        :type meta: DeploymentRelationshipMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
