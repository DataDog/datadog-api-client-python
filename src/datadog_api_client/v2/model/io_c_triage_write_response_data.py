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
    from datadog_api_client.v2.model.io_c_triage_write_response_attributes import IoCTriageWriteResponseAttributes


class IoCTriageWriteResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_triage_write_response_attributes import IoCTriageWriteResponseAttributes

        return {
            "attributes": (IoCTriageWriteResponseAttributes,),
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
        attributes: Union[IoCTriageWriteResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object of the triage write response.

        :param attributes: Attributes of a created or updated triage state.
        :type attributes: IoCTriageWriteResponseAttributes, optional

        :param id: Unique identifier for the triage state record.
        :type id: str, optional

        :param type: Triage state resource type.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
