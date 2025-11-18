# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DeploymentRuleResponseDataAttributesUpdatedBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "id": "id",
        "name": "name",
    }

    def __init__(self_, id: str, handle: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Information about the user who updated the deployment rule.

        :param handle: The handle of the user who updated the deployment rule.
        :type handle: str, optional

        :param id: The ID of the user who updated the deployment rule.
        :type id: str

        :param name: The name of the user who updated the deployment rule.
        :type name: str, optional
        """
        if handle is not unset:
            kwargs["handle"] = handle
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.id = id
