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
    from datadog_api_client.v2.model.update_app_tags_request_data_attributes import UpdateAppTagsRequestDataAttributes
    from datadog_api_client.v2.model.app_tags_type import AppTagsType


class UpdateAppTagsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_tags_request_data_attributes import (
            UpdateAppTagsRequestDataAttributes,
        )
        from datadog_api_client.v2.model.app_tags_type import AppTagsType

        return {
            "attributes": (UpdateAppTagsRequestDataAttributes,),
            "type": (AppTagsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UpdateAppTagsRequestDataAttributes, UnsetType] = unset,
        type: Union[AppTagsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for replacing an app's tags.

        :param attributes: Attributes for replacing an app's tags.
        :type attributes: UpdateAppTagsRequestDataAttributes, optional

        :param type: The tags resource type.
        :type type: AppTagsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
