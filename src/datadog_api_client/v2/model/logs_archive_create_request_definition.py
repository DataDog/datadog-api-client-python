# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchiveCreateRequestDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_create_request_attributes import (
            LogsArchiveCreateRequestAttributes,
        )

        return {
            "attributes": (LogsArchiveCreateRequestAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        The definition of an archive.

        :param attributes: The attributes associated with the archive.
        :type attributes: LogsArchiveCreateRequestAttributes, optional

        :param type: The type of the resource. The value should always be archives.
        :type type: str
        """
        super().__init__(kwargs)
        type = kwargs.get("type", "archives")

        self_._check_pos_args(args)

        self_.type = type
