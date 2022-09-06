# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsArchive(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.logs_archive_definition import LogsArchiveDefinition

        return {
            "data": (LogsArchiveDefinition,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        The logs archive.

        :param data: The definition of an archive.
        :type data: LogsArchiveDefinition, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
