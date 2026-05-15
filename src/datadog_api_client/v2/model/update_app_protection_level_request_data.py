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
    from datadog_api_client.v2.model.update_app_protection_level_request_data_attributes import (
        UpdateAppProtectionLevelRequestDataAttributes,
    )
    from datadog_api_client.v2.model.app_protection_level_type import AppProtectionLevelType


class UpdateAppProtectionLevelRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_protection_level_request_data_attributes import (
            UpdateAppProtectionLevelRequestDataAttributes,
        )
        from datadog_api_client.v2.model.app_protection_level_type import AppProtectionLevelType

        return {
            "attributes": (UpdateAppProtectionLevelRequestDataAttributes,),
            "type": (AppProtectionLevelType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UpdateAppProtectionLevelRequestDataAttributes, UnsetType] = unset,
        type: Union[AppProtectionLevelType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for updating an app's publication protection level.

        :param attributes: Attributes for updating an app's publication protection level.
        :type attributes: UpdateAppProtectionLevelRequestDataAttributes, optional

        :param type: The protection-level resource type.
        :type type: AppProtectionLevelType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
