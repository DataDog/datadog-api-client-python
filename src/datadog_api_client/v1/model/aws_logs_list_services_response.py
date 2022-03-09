# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSLogsListServicesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "label": (str,),
        }

    attribute_map = {
        "id": "id",
        "label": "label",
    }

    def __init__(self, *args, **kwargs):
        """
        The list of current AWS services for which Datadog offers automatic log collection.

        :param id: Key value in returned object.
        :type id: str, optional

        :param label: Name of service available for configuration with Datadog logs.
        :type label: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSLogsListServicesResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
