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
    from datadog_api_client.v2.model.io_c_explorer_list_response_attributes import IoCExplorerListResponseAttributes


class IoCExplorerListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_explorer_list_response_attributes import IoCExplorerListResponseAttributes

        return {
            "attributes": (IoCExplorerListResponseAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[IoCExplorerListResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        IoC Explorer list response data object.

        :param attributes: Attributes of the IoC Explorer list response.
        :type attributes: IoCExplorerListResponseAttributes, optional

        :param id: Unique identifier for the response.
        :type id: str, optional

        :param type: Response type identifier.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
