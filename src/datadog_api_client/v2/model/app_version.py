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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_version_attributes import AppVersionAttributes
    from datadog_api_client.v2.model.app_version_type import AppVersionType


class AppVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_version_attributes import AppVersionAttributes
        from datadog_api_client.v2.model.app_version_type import AppVersionType

        return {
            "attributes": (AppVersionAttributes,),
            "id": (UUID,),
            "type": (AppVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AppVersionAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        type: Union[AppVersionType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A version of an app.

        :param attributes: Attributes describing an app version.
        :type attributes: AppVersionAttributes, optional

        :param id: The ID of the app version.
        :type id: UUID, optional

        :param type: The app-version resource type.
        :type type: AppVersionType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
