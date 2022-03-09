# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.check_can_delete_slo_response_data import CheckCanDeleteSLOResponseData

    globals()["CheckCanDeleteSLOResponseData"] = CheckCanDeleteSLOResponseData


class CheckCanDeleteSLOResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": (CheckCanDeleteSLOResponseData,),
            "errors": ({str: (str,)},),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
    }

    def __init__(self, *args, **kwargs):
        """
        A service level objective response containing the requested object.

        :param data: An array of service level objective objects.
        :type data: CheckCanDeleteSLOResponseData, optional

        :param errors: A mapping of SLO id to it's current usages.
        :type errors: {str: (str,)}, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CheckCanDeleteSLOResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
