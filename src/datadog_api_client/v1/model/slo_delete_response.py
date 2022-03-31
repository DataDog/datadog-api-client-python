# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLODeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data": ([str],),
            "errors": ({str: (str,)},),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
    }

    def __init__(self, *args, **kwargs):
        """
        A response list of all service level objective deleted.

        :param data: An array containing the ID of the deleted service level objective object.
        :type data: [str], optional

        :param errors: An dictionary containing the ID of the SLO as key and a deletion error as value.
        :type errors: {str: (str,)}, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLODeleteResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
