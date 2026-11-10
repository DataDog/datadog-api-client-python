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


class DeviceGeoIP(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "geo_city": (str,),
            "geo_country_iso_code": (str,),
            "geo_latitude": (float,),
            "geo_longitude": (float,),
            "geo_subdivision_iso_code": (str,),
            "public_ip_address": (str,),
        }

    attribute_map = {
        "geo_city": "geo_city",
        "geo_country_iso_code": "geo_country_iso_code",
        "geo_latitude": "geo_latitude",
        "geo_longitude": "geo_longitude",
        "geo_subdivision_iso_code": "geo_subdivision_iso_code",
        "public_ip_address": "public_ip_address",
    }

    def __init__(
        self_,
        geo_city: Union[str, UnsetType] = unset,
        geo_country_iso_code: Union[str, UnsetType] = unset,
        geo_latitude: Union[float, UnsetType] = unset,
        geo_longitude: Union[float, UnsetType] = unset,
        geo_subdivision_iso_code: Union[str, UnsetType] = unset,
        public_ip_address: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Location derived from the device's public IP address.
        Absent when no location data is available.

        :param geo_city: City resolved from the device's public IP address.
        :type geo_city: str, optional

        :param geo_country_iso_code: ISO 3166-1 alpha-2 country code resolved from the device's public IP address.
        :type geo_country_iso_code: str, optional

        :param geo_latitude: Latitude resolved from the device's public IP address.
        :type geo_latitude: float, optional

        :param geo_longitude: Longitude resolved from the device's public IP address.
        :type geo_longitude: float, optional

        :param geo_subdivision_iso_code: ISO 3166-2 subdivision code (for example, a state or province)
            resolved from the device's public IP address.
        :type geo_subdivision_iso_code: str, optional

        :param public_ip_address: Public IPv4 or IPv6 address of the device.
        :type public_ip_address: str, optional
        """
        if geo_city is not unset:
            kwargs["geo_city"] = geo_city
        if geo_country_iso_code is not unset:
            kwargs["geo_country_iso_code"] = geo_country_iso_code
        if geo_latitude is not unset:
            kwargs["geo_latitude"] = geo_latitude
        if geo_longitude is not unset:
            kwargs["geo_longitude"] = geo_longitude
        if geo_subdivision_iso_code is not unset:
            kwargs["geo_subdivision_iso_code"] = geo_subdivision_iso_code
        if public_ip_address is not unset:
            kwargs["public_ip_address"] = public_ip_address
        super().__init__(kwargs)
