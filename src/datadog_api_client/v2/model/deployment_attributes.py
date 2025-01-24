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
    UUID,
)


class DeploymentAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_version_id": (UUID,),
        }

    attribute_map = {
        "app_version_id": "app_version_id",
    }

    def __init__(self_, app_version_id: Union[UUID, UnsetType] = unset, **kwargs):
        """
        The attributes object containing the version ID of the published app.

        :param app_version_id: The version ID of the app that was published. For an unpublished app, this is always the nil UUID ( ``00000000-0000-0000-0000-000000000000`` ).
        :type app_version_id: UUID, optional
        """
        if app_version_id is not unset:
            kwargs["app_version_id"] = app_version_id
        super().__init__(kwargs)
