# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_location import SyntheticsLocation

    globals()["SyntheticsLocation"] = SyntheticsLocation


class SyntheticsLocations(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "locations": ([SyntheticsLocation],),
        }

    attribute_map = {
        "locations": "locations",
    }

    def __init__(self, *args, **kwargs):
        """
        List of Synthetics locations.

        :param locations: List of Synthetics locations.
        :type locations: [SyntheticsLocation], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsLocations, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
