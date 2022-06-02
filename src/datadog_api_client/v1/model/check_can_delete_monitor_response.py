# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CheckCanDeleteMonitorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.check_can_delete_monitor_response_data import CheckCanDeleteMonitorResponseData

        return {
            "data": (CheckCanDeleteMonitorResponseData,),
            "errors": ({str: ([str],)},),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
    }

    def __init__(self, data, *args, **kwargs):
        """
        Response of monitor IDs that can or can't be safely deleted.

        :param data: Wrapper object with the list of monitor IDs.
        :type data: CheckCanDeleteMonitorResponseData

        :param errors: A mapping of Monitor ID to strings denoting where it's used.
        :type errors: {str: ([str],)}, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CheckCanDeleteMonitorResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
