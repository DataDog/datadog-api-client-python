# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UnassignSeatsUserRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "product_code": (str,),
            "user_uuids": ([str],),
        }

    attribute_map = {
        "product_code": "product_code",
        "user_uuids": "user_uuids",
    }

    def __init__(self_, product_code: str, user_uuids: List[str], **kwargs):
        """


        :param product_code: The product code for which to unassign seats.
        :type product_code: str

        :param user_uuids: The list of user IDs to unassign seats from.
        :type user_uuids: [str]
        """
        super().__init__(kwargs)

        self_.product_code = product_code
        self_.user_uuids = user_uuids
