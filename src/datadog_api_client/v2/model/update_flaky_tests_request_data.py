# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.update_flaky_tests_request_attributes import UpdateFlakyTestsRequestAttributes
    from datadog_api_client.v2.model.update_flaky_tests_request_data_type import UpdateFlakyTestsRequestDataType


class UpdateFlakyTestsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_flaky_tests_request_attributes import UpdateFlakyTestsRequestAttributes
        from datadog_api_client.v2.model.update_flaky_tests_request_data_type import UpdateFlakyTestsRequestDataType

        return {
            "attributes": (UpdateFlakyTestsRequestAttributes,),
            "type": (UpdateFlakyTestsRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpdateFlakyTestsRequestAttributes, type: UpdateFlakyTestsRequestDataType, **kwargs):
        """
        The JSON:API data for updating flaky test states.

        :param attributes: Attributes for updating flaky test states.
        :type attributes: UpdateFlakyTestsRequestAttributes

        :param type: The definition of ``UpdateFlakyTestsRequestDataType`` object.
        :type type: UpdateFlakyTestsRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
