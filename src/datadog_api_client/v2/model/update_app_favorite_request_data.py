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
    from datadog_api_client.v2.model.update_app_favorite_request_data_attributes import (
        UpdateAppFavoriteRequestDataAttributes,
    )
    from datadog_api_client.v2.model.app_favorite_type import AppFavoriteType


class UpdateAppFavoriteRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_favorite_request_data_attributes import (
            UpdateAppFavoriteRequestDataAttributes,
        )
        from datadog_api_client.v2.model.app_favorite_type import AppFavoriteType

        return {
            "attributes": (UpdateAppFavoriteRequestDataAttributes,),
            "type": (AppFavoriteType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UpdateAppFavoriteRequestDataAttributes, UnsetType] = unset,
        type: Union[AppFavoriteType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for updating an app's favorite status.

        :param attributes: Attributes for updating an app's favorite status.
        :type attributes: UpdateAppFavoriteRequestDataAttributes, optional

        :param type: The favorite resource type.
        :type type: AppFavoriteType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
