# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_response_data import SLOResponseData

        return {
            "data": (SLOResponseData,),
            "errors": ([str],),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
    }

    def __init__(self, *args, **kwargs):
        """
        A service level objective response containing a single service level objective.

        :param data: A service level objective object includes a service level indicator, thresholds
            for one or more timeframes, and metadata ( ``name`` , ``description`` , ``tags`` , etc.).
        :type data: SLOResponseData, optional

        :param errors: An array of error messages. Each endpoint documents how/whether this field is
            used.
        :type errors: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
