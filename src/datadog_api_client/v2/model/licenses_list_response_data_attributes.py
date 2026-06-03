# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.licenses_list_response_data_attributes_licenses_items import (
        LicensesListResponseDataAttributesLicensesItems,
    )


class LicensesListResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.licenses_list_response_data_attributes_licenses_items import (
            LicensesListResponseDataAttributesLicensesItems,
        )

        return {
            "licenses": ([LicensesListResponseDataAttributesLicensesItems],),
        }

    attribute_map = {
        "licenses": "licenses",
    }

    def __init__(self_, licenses: List[LicensesListResponseDataAttributesLicensesItems], **kwargs):
        """
        The attributes of the licenses list response, containing the array of SPDX licenses.

        :param licenses: The list of SPDX licenses returned by the API.
        :type licenses: [LicensesListResponseDataAttributesLicensesItems]
        """
        super().__init__(kwargs)

        self_.licenses = licenses
