# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IoCGeoLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "city": (str,),
            "country_code": (str,),
            "country_name": (str,),
        }

    attribute_map = {
        "city": "city",
        "country_code": "country_code",
        "country_name": "country_name",
    }

    def __init__(
        self_,
        city: Union[str, UnsetType] = unset,
        country_code: Union[str, UnsetType] = unset,
        country_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Geographic location information for an IP indicator.

        :param city: City name.
        :type city: str, optional

        :param country_code: ISO country code.
        :type country_code: str, optional

        :param country_name: Full country name.
        :type country_name: str, optional
        """
        if city is not unset:
            kwargs["city"] = city
        if country_code is not unset:
            kwargs["country_code"] = country_code
        if country_name is not unset:
            kwargs["country_name"] = country_name
        super().__init__(kwargs)
