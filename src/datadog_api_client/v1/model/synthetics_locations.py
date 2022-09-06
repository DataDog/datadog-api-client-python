# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsLocations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_location import SyntheticsLocation

        return {
            "locations": ([SyntheticsLocation],),
        }

    attribute_map = {
        "locations": "locations",
    }

    def __init__(self_, *args, **kwargs):
        """
        List of Synthetics locations.

        :param locations: List of Synthetics locations.
        :type locations: [SyntheticsLocation], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
