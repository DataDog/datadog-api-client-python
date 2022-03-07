# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTriggerCITestLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (int,),
            "name": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
    }

    def __init__(self, *args, **kwargs):
        """
        Synthetics location.

        :param id: Unique identifier of the location.
        :type id: int, optional

        :param name: Name of the location.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerCITestLocation, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
