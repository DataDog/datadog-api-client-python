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


class AssignSeatsUserResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assigned_ids": ([str],),
            "product_code": (str,),
        }

    attribute_map = {
        "assigned_ids": "assigned_ids",
        "product_code": "product_code",
    }

    def __init__(
        self_, assigned_ids: Union[List[str], UnsetType] = unset, product_code: Union[str, UnsetType] = unset, **kwargs
    ):
        """


        :param assigned_ids:
        :type assigned_ids: [str], optional

        :param product_code:
        :type product_code: str, optional
        """
        if assigned_ids is not unset:
            kwargs["assigned_ids"] = assigned_ids
        if product_code is not unset:
            kwargs["product_code"] = product_code
        super().__init__(kwargs)
