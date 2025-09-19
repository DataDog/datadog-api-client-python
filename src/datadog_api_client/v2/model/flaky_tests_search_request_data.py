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
    from datadog_api_client.v2.model.flaky_tests_search_request_attributes import FlakyTestsSearchRequestAttributes
    from datadog_api_client.v2.model.flaky_tests_search_request_data_type import FlakyTestsSearchRequestDataType


class FlakyTestsSearchRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_tests_search_request_attributes import FlakyTestsSearchRequestAttributes
        from datadog_api_client.v2.model.flaky_tests_search_request_data_type import FlakyTestsSearchRequestDataType

        return {
            "attributes": (FlakyTestsSearchRequestAttributes,),
            "type": (FlakyTestsSearchRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[FlakyTestsSearchRequestAttributes, UnsetType] = unset,
        type: Union[FlakyTestsSearchRequestDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API data for flaky tests search request.

        :param attributes: Attributes for the flaky tests search request.
        :type attributes: FlakyTestsSearchRequestAttributes, optional

        :param type: The definition of ``FlakyTestsSearchRequestDataType`` object.
        :type type: FlakyTestsSearchRequestDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
