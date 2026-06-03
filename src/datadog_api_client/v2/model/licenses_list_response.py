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
    from datadog_api_client.v2.model.licenses_list_response_data import LicensesListResponseData


class LicensesListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.licenses_list_response_data import LicensesListResponseData

        return {
            "data": (LicensesListResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LicensesListResponseData, **kwargs):
        """
        The top-level response object returned by the licenses list endpoint, containing the array of supported SPDX licenses.

        :param data: The data object in a licenses list response, containing the list of SPDX licenses.
        :type data: LicensesListResponseData
        """
        super().__init__(kwargs)

        self_.data = data
