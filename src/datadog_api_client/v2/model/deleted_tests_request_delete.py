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
    from datadog_api_client.v2.model.deleted_tests_request_delete_attributes import DeletedTestsRequestDeleteAttributes
    from datadog_api_client.v2.model.deleted_tests_request_type import DeletedTestsRequestType


class DeletedTestsRequestDelete(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deleted_tests_request_delete_attributes import (
            DeletedTestsRequestDeleteAttributes,
        )
        from datadog_api_client.v2.model.deleted_tests_request_type import DeletedTestsRequestType

        return {
            "attributes": (DeletedTestsRequestDeleteAttributes,),
            "id": (str,),
            "type": (DeletedTestsRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: DeletedTestsRequestDeleteAttributes,
        id: Union[str, UnsetType] = unset,
        type: Union[DeletedTestsRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: DeletedTestsRequestDeleteAttributes

        :param id:
        :type id: str, optional

        :param type:
        :type type: DeletedTestsRequestType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.attributes = attributes
