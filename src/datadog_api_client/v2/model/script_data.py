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
    from datadog_api_client.v2.model.script_data_attributes import ScriptDataAttributes
    from datadog_api_client.v2.model.script_data_type import ScriptDataType


class ScriptData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.script_data_attributes import ScriptDataAttributes
        from datadog_api_client.v2.model.script_data_type import ScriptDataType

        return {
            "attributes": (ScriptDataAttributes,),
            "id": (str,),
            "type": (ScriptDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ScriptDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ScriptDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ScriptData`` object.

        :param attributes: The definition of ``ScriptDataAttributes`` object.
        :type attributes: ScriptDataAttributes, optional

        :param id: The ``data`` ``id``.
        :type id: str, optional

        :param type: The definition of ``ScriptDataType`` object.
        :type type: ScriptDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
