# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookCreateDataAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 80,
            "min_length": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
        from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
        from datadog_api_client.v1.model.notebook_status import NotebookStatus
        from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime

        return {
            "cells": ([NotebookCellCreateRequest],),
            "metadata": (NotebookMetadata,),
            "name": (str,),
            "status": (NotebookStatus,),
            "time": (NotebookGlobalTime,),
        }

    attribute_map = {
        "cells": "cells",
        "metadata": "metadata",
        "name": "name",
        "status": "status",
        "time": "time",
    }

    def __init__(self, cells, name, time, *args, **kwargs):
        """
        The data attributes of a notebook.

        :param cells: List of cells to display in the notebook.
        :type cells: [NotebookCellCreateRequest]

        :param metadata: Metadata associated with the notebook.
        :type metadata: NotebookMetadata, optional

        :param name: The name of the notebook.
        :type name: str

        :param status: Publication status of the notebook. For now, always "published".
        :type status: NotebookStatus, optional

        :param time: Notebook global timeframe.
        :type time: NotebookGlobalTime
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.cells = cells
        self.name = name
        self.time = time

    @classmethod
    def _from_openapi_data(cls, cells, name, time, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCreateDataAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.cells = cells
        self.name = name
        self.time = time
        return self
