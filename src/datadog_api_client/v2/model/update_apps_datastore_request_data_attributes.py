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


class UpdateAppsDatastoreRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
    }

    def __init__(self_, description: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes that can be updated on a datastore.

        :param description: A human-readable description about the datastore.
        :type description: str, optional

        :param name: The display name of the datastore.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
