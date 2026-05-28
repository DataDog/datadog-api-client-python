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


class CostTagDescriptionUpsertRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cloud": (str,),
            "description": (str,),
        }

    attribute_map = {
        "cloud": "cloud",
        "description": "description",
    }

    def __init__(self_, description: str, cloud: Union[str, UnsetType] = unset, **kwargs):
        """
        Mutable attributes set when creating or updating a Cloud Cost Management tag key description.

        :param cloud: Cloud provider this description applies to (for example, ``aws`` ). Omit to set the cross-cloud default for the tag key.
        :type cloud: str, optional

        :param description: The human-readable description for the tag key.
        :type description: str
        """
        if cloud is not unset:
            kwargs["cloud"] = cloud
        super().__init__(kwargs)

        self_.description = description
