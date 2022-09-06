# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class HourlyUsageMeasurement(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "usage_type": (str,),
            "value": (int, none_type),
        }

    attribute_map = {
        "usage_type": "usage_type",
        "value": "value",
    }

    def __init__(self_, *args, **kwargs):
        """
        Usage amount for a given usage type.

        :param usage_type: Type of usage.
        :type usage_type: str, optional

        :param value: Contains the number measured for the given usage_type during the hour.
        :type value: int, none_type, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
