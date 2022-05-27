# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOBulkDeleteError(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_error_timeframe import SLOErrorTimeframe

        return {
            "id": (str,),
            "message": (str,),
            "timeframe": (SLOErrorTimeframe,),
        }

    attribute_map = {
        "id": "id",
        "message": "message",
        "timeframe": "timeframe",
    }

    def __init__(self, id, message, timeframe, *args, **kwargs):
        """
        Object describing the error.

        :param id: The ID of the service level objective object associated with
            this error.
        :type id: str

        :param message: The error message.
        :type message: str

        :param timeframe: The timeframe of the threshold associated with this error
            or "all" if all thresholds are affected.
        :type timeframe: SLOErrorTimeframe
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.message = message
        self.timeframe = timeframe

    @classmethod
    def _from_openapi_data(cls, id, message, timeframe, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOBulkDeleteError, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.message = message
        self.timeframe = timeframe
        return self
