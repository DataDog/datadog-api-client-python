# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsIndexesOrder(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "index_names": ([str],),
        }

    attribute_map = {
        "index_names": "index_names",
    }

    def __init__(self, index_names, *args, **kwargs):
        """
        Object containing the ordered list of log index names.

        :param index_names: Array of strings identifying by their name(s) the index(es) of your organization.
            Logs are tested against the query filter of each index one by one, following the order of the array.
            Logs are eventually stored in the first matching index.
        :type index_names: [str]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.index_names = index_names

    @classmethod
    def _from_openapi_data(cls, index_names, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsIndexesOrder, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.index_names = index_names
        return self
