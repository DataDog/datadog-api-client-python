# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class LogsArchiveCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_create_request_destination import (
            LogsArchiveCreateRequestDestination,
        )

        return {
            "destination": (LogsArchiveCreateRequestDestination,),
            "include_tags": (bool,),
            "name": (str,),
            "query": (str,),
            "rehydration_max_scan_size_in_gb": (int, none_type),
            "rehydration_tags": ([str],),
        }

    attribute_map = {
        "destination": "destination",
        "include_tags": "include_tags",
        "name": "name",
        "query": "query",
        "rehydration_max_scan_size_in_gb": "rehydration_max_scan_size_in_gb",
        "rehydration_tags": "rehydration_tags",
    }

    def __init__(self_, destination, name, query, *args, **kwargs):
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

        :param rehydration_max_scan_size_in_gb: Maximum scan size for rehydration from this archive.
        :type rehydration_max_scan_size_in_gb: int, none_type, optional

        :param rehydration_tags: An array of tags to add to rehydrated logs from an archive.
        :type rehydration_tags: [str], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.destination = destination
        self_.name = name
        self_.query = query
