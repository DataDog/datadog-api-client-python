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
    from datadog_api_client.v2.model.dora_deployment_type import DORADeploymentType


class DORADeploymentResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dora_deployment_type import DORADeploymentType

        return {
            "id": (str,),
            "type": (DORADeploymentType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: Union[DORADeploymentType, UnsetType] = unset, **kwargs):
        """
        The JSON:API data.

        :param id: The ID of the received DORA deployment event.
        :type id: str

        :param type: JSON:API type for DORA deployment events.
        :type type: DORADeploymentType, optional
        """
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.id = id
