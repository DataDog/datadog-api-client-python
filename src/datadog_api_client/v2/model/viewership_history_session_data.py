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
    from datadog_api_client.v2.model.viewership_history_session_data_attributes import (
        ViewershipHistorySessionDataAttributes,
    )
    from datadog_api_client.v2.model.viewership_history_session_data_type import ViewershipHistorySessionDataType


class ViewershipHistorySessionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.viewership_history_session_data_attributes import (
            ViewershipHistorySessionDataAttributes,
        )
        from datadog_api_client.v2.model.viewership_history_session_data_type import ViewershipHistorySessionDataType

        return {
            "attributes": (ViewershipHistorySessionDataAttributes,),
            "id": (str,),
            "type": (ViewershipHistorySessionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ViewershipHistorySessionDataType,
        attributes: Union[ViewershipHistorySessionDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: ViewershipHistorySessionDataAttributes, optional

        :param id:
        :type id: str, optional

        :param type: Rum replay session resource type.
        :type type: ViewershipHistorySessionDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
