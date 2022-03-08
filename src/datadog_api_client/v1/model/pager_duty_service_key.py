# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PagerDutyServiceKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "service_key": (str,),
        }

    attribute_map = {
        "service_key": "service_key",
    }

    def __init__(self, service_key, *args, **kwargs):
        """
        PagerDuty service object key.

        :param service_key: Your service key in PagerDuty.
        :type service_key: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.service_key = service_key

    @classmethod
    def _from_openapi_data(cls, service_key, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(PagerDutyServiceKey, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.service_key = service_key
        return self
