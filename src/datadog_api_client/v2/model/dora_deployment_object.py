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
    from datadog_api_client.v2.model.dora_deployment_object_attributes import DORADeploymentObjectAttributes
    from datadog_api_client.v2.model.dora_deployment_type import DORADeploymentType


class DORADeploymentObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_object_attributes import DORADeploymentObjectAttributes
        from datadog_api_client.v2.model.dora_deployment_type import DORADeploymentType

        return {
            "attributes": (DORADeploymentObjectAttributes,),
            "id": (str,),
            "type": (DORADeploymentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DORADeploymentObjectAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[DORADeploymentType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A DORA deployment event.

        :param attributes: The attributes of the deployment event.
        :type attributes: DORADeploymentObjectAttributes, optional

        :param id: The ID of the deployment event.
        :type id: str, optional

        :param type: JSON:API type for DORA deployment events.
        :type type: DORADeploymentType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
