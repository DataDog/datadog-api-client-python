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


class PatchMaintenanceUpdateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
        }

    attribute_map = {
        "description": "description",
    }

    def __init__(self_, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for editing a maintenance update.

        :param description: The message body of the update.
        :type description: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)
