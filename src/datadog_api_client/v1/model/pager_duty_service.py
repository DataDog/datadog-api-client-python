# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class PagerDutyService(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "service_key": (str,),
            "service_name": (str,),
        }

    attribute_map = {
        "service_key": "service_key",
        "service_name": "service_name",
    }

    read_only_vars = {}

    def __init__(self, service_key, service_name, *args, **kwargs):
        """PagerDutyService - a model defined in OpenAPI

        Args:
            service_key (str): Your service key in PagerDuty.
            service_name (str): Your service name associated with a service key in PagerDuty.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.service_key = service_key
        self.service_name = service_name

    @classmethod
    def _from_openapi_data(cls, service_key, service_name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(PagerDutyService, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.service_key = service_key
        self.service_name = service_name
        return self
