# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageIoTHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "hour": (datetime,),
            "iot_device_count": (int,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "hour": "hour",
        "iot_device_count": "iot_device_count",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageIoTHour - a model defined in OpenAPI

        Keyword Args:
            hour (datetime): [optional] The hour for the usage.
            iot_device_count (int): [optional] The total number of IoT devices during a given hour.
            org_name (str): [optional] The organization name.
            public_id (str): [optional] The organization public ID.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageIoTHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
