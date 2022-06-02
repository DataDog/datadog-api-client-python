# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOHistoryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_history_response_data import SLOHistoryResponseData
        from datadog_api_client.v1.model.slo_history_response_error import SLOHistoryResponseError

        return {
            "data": (SLOHistoryResponseData,),
            "errors": ([SLOHistoryResponseError],),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
    }

    def __init__(self, *args, **kwargs):
        """
        A service level objective history response.

        :param data: An array of service level objective objects.
        :type data: SLOHistoryResponseData, optional

        :param errors: A list of errors while querying the history data for the service level objective.
        :type errors: [SLOHistoryResponseError], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
