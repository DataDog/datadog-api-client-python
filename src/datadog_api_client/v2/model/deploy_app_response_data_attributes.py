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


class DeployAppResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_version_id": (str,),
        }

    attribute_map = {
        "app_version_id": "app_version_id",
    }

    def __init__(self_, app_version_id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``DeployAppResponseDataAttributes`` object.

        :param app_version_id: The ``attributes`` ``app_version_id``.
        :type app_version_id: str, optional
        """
        if app_version_id is not unset:
            kwargs["app_version_id"] = app_version_id
        super().__init__(kwargs)
