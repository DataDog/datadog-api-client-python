# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_attributes import LogsArchiveAttributes

        return {
            "attributes": (LogsArchiveAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
        "type",
    }

    def __init__(self, *args, **kwargs):
        """
        The definition of an archive.

        :param attributes: The attributes associated with the archive.
        :type attributes: LogsArchiveAttributes, optional

        :param id: The archive ID.
        :type id: str, optional

        :param type: The type of the resource. The value should always be archives.
        :type type: str
        """
        super().__init__(kwargs)
        type = kwargs.get("type", "archives")

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        type = kwargs.get("type", "archives")

        self = super(LogsArchiveDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
