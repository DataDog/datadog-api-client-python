# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.log import Log

    globals()["Log"] = Log


class LogsListResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "logs": ([Log],),
            "next_log_id": (str,),
            "status": (str,),
        }

    attribute_map = {
        "logs": "logs",
        "next_log_id": "nextLogId",
        "status": "status",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """LogsListResponse - a model defined in OpenAPI

        Keyword Args:
            logs ([Log]): [optional] Array of logs matching the request and the `nextLogId` if sent.
            next_log_id (str): [optional] Hash identifier of the next log to return in the list. This parameter is used for the pagination feature.
            status (str): [optional] Status of the response.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
