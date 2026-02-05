# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AssignSeatsUserRequestDataAttributes(ModelNormal):
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

    def __init__(
        self_, product_code: Union[str, UnsetType] = unset, user_uuids: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """


        :param product_code:
        :type product_code: str, optional

        :param user_uuids:
        :type user_uuids: [str], optional
        """
        if product_code is not unset:
            kwargs["product_code"] = product_code
        if user_uuids is not unset:
            kwargs["user_uuids"] = user_uuids
        super().__init__(kwargs)
