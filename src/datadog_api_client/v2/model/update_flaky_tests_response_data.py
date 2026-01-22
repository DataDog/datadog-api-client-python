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
    from datadog_api_client.v2.model.update_flaky_tests_response_attributes import UpdateFlakyTestsResponseAttributes
    from datadog_api_client.v2.model.update_flaky_tests_response_data_type import UpdateFlakyTestsResponseDataType


class UpdateFlakyTestsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_flaky_tests_response_attributes import (
            UpdateFlakyTestsResponseAttributes,
        )
        from datadog_api_client.v2.model.update_flaky_tests_response_data_type import UpdateFlakyTestsResponseDataType

        return {
            "attributes": (UpdateFlakyTestsResponseAttributes,),
            "id": (str,),
            "type": (UpdateFlakyTestsResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UpdateFlakyTestsResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[UpdateFlakyTestsResponseDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary of the update operations. Tells whether a test succeeded or failed to be updated.

        :param attributes: Attributes for the update flaky test state response.
        :type attributes: UpdateFlakyTestsResponseAttributes, optional

        :param id: The ID of the response.
        :type id: str, optional

        :param type: The definition of ``UpdateFlakyTestsResponseDataType`` object.
        :type type: UpdateFlakyTestsResponseDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
