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
    from datadog_api_client.v2.model.deployment_relationship import DeploymentRelationship


class ListAppsResponseDataItemsRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_relationship import DeploymentRelationship

        return {
            "deployment": (DeploymentRelationship,),
        }

    attribute_map = {
        "deployment": "deployment",
    }

    def __init__(self_, deployment: Union[DeploymentRelationship, UnsetType] = unset, **kwargs):
        """
        The app's publication information.

        :param deployment: Information pointing to the app's publication status.
        :type deployment: DeploymentRelationship, optional
        """
        if deployment is not unset:
            kwargs["deployment"] = deployment
        super().__init__(kwargs)
