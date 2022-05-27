# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_metadata_type import NotebookMetadataType

        return {
            "is_template": (bool,),
            "take_snapshots": (bool,),
            "type": (NotebookMetadataType,),
        }

    attribute_map = {
        "is_template": "is_template",
        "take_snapshots": "take_snapshots",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Metadata associated with the notebook.

        :param is_template: Whether or not the notebook is a template.
        :type is_template: bool, optional

        :param take_snapshots: Whether or not the notebook takes snapshot image backups of the notebook's fixed-time graphs.
        :type take_snapshots: bool, optional

        :param type: Metadata type of the notebook.
        :type type: NotebookMetadataType, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
