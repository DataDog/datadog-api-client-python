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
    from datadog_api_client.v2.model.deleted_test_response_data_attributes import DeletedTestResponseDataAttributes
    from datadog_api_client.v2.model.deleted_tests_response_type import DeletedTestsResponseType


class DeletedTestResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deleted_test_response_data_attributes import DeletedTestResponseDataAttributes
        from datadog_api_client.v2.model.deleted_tests_response_type import DeletedTestsResponseType

        return {
            "attributes": (DeletedTestResponseDataAttributes,),
            "id": (str,),
            "type": (DeletedTestsResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DeletedTestResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[DeletedTestsResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: DeletedTestResponseDataAttributes, optional

        :param id:
        :type id: str, optional

        :param type:
        :type type: DeletedTestsResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
