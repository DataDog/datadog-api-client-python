# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.logs_archive_create_request_destination import LogsArchiveCreateRequestDestination

    globals()["LogsArchiveCreateRequestDestination"] = LogsArchiveCreateRequestDestination


class LogsArchiveCreateRequestAttributes(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "destination": (LogsArchiveCreateRequestDestination,),
            "include_tags": (bool,),
            "name": (str,),
            "query": (str,),
            "rehydration_tags": ([str],),
        }

    attribute_map = {
        "destination": "destination",
        "include_tags": "include_tags",
        "name": "name",
        "query": "query",
        "rehydration_tags": "rehydration_tags",
    }

    read_only_vars = {}

    def __init__(self, destination, name, query, *args, **kwargs):
        """
        The attributes associated with the archive.

        :param destination: An archive's destination.
        :type destination: LogsArchiveCreateRequestDestination

        :param include_tags: To store the tags in the archive, set the value "true".
            If it is set to "false", the tags will be deleted when the logs are sent to the archive.
        :type include_tags: bool, optional

        :param name: The archive name.
        :type name: str

        :param query: The archive query/filter. Logs matching this query are included in the archive.
        :type query: str

        :param rehydration_tags: An array of tags to add to rehydrated logs from an archive.
        :type rehydration_tags: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.destination = destination
        self.name = name
        self.query = query

    @classmethod
    def _from_openapi_data(cls, destination, name, query, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArchiveCreateRequestAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.destination = destination
        self.name = name
        self.query = query
        return self
