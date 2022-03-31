# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class UsageRumUnitsHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "browser_rum_units": (int,),
            "mobile_rum_units": (int,),
            "org_name": (str,),
            "public_id": (str,),
            "rum_units": (int, none_type),
        }

    attribute_map = {
        "browser_rum_units": "browser_rum_units",
        "mobile_rum_units": "mobile_rum_units",
        "org_name": "org_name",
        "public_id": "public_id",
        "rum_units": "rum_units",
    }

    def __init__(self, *args, **kwargs):
        """
        Number of RUM Units used for each hour for a given organization (data available as of November 1, 2021).

        :param browser_rum_units: The number of browser RUM units.
        :type browser_rum_units: int, optional

        :param mobile_rum_units: The number of mobile RUM units.
        :type mobile_rum_units: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param rum_units: Total RUM units across mobile and browser RUM.
        :type rum_units: int, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageRumUnitsHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
