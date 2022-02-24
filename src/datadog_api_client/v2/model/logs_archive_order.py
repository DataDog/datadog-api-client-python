# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_archive_order_definition import LogsArchiveOrderDefinition

    globals()["LogsArchiveOrderDefinition"] = LogsArchiveOrderDefinition


class LogsArchiveOrder(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": (LogsArchiveOrderDefinition,),
        }

    attribute_map = {
        "data": "data",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        A ordered list of archive IDs.

        :param data: The definition of an archive order.
        :type data: LogsArchiveOrderDefinition, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveOrder, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
