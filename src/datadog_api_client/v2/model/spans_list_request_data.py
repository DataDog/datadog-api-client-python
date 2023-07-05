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
    from datadog_api_client.v2.model.spans_list_request_attributes import SpansListRequestAttributes
    from datadog_api_client.v2.model.spans_list_request_type import SpansListRequestType


class SpansListRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_list_request_attributes import SpansListRequestAttributes
        from datadog_api_client.v2.model.spans_list_request_type import SpansListRequestType

        return {
            "attributes": (SpansListRequestAttributes,),
            "type": (SpansListRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SpansListRequestAttributes, UnsetType] = unset,
        type: Union[SpansListRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object containing the query content.

        :param attributes: The object containing all the query parameters.
        :type attributes: SpansListRequestAttributes, optional

        :param type: The type of resource. The value should always be search_request.
        :type type: SpansListRequestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
