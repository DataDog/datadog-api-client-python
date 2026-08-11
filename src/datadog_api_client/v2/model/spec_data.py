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
    from datadog_api_client.v2.model.spec_attributes import SpecAttributes
    from datadog_api_client.v2.model.spec_type import SpecType


class SpecData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spec_attributes import SpecAttributes
        from datadog_api_client.v2.model.spec_type import SpecType

        return {
            "attributes": (SpecAttributes,),
            "id": (str,),
            "type": (SpecType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: SpecType,
        attributes: Union[SpecAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single API spec resource.

        :param attributes: Attributes of an API spec.
        :type attributes: SpecAttributes, optional

        :param id: The unique identifier of the spec.
        :type id: str, optional

        :param type: Type of the spec resource.
        :type type: SpecType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
