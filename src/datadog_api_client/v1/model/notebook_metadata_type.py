# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class NotebookMetadataType(ModelSimple):
    """
    Metadata type of the notebook.

    :param value: Must be one of ["postmortem", "runbook", "investigation", "documentation", "report"].
    :type value: str
    """

    allowed_values = {
        "postmortem",
        "runbook",
        "investigation",
        "documentation",
        "report",
    }

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


NotebookMetadataType.POSTMORTEM = NotebookMetadataType("postmortem")
NotebookMetadataType.RUNBOOK = NotebookMetadataType("runbook")
NotebookMetadataType.INVESTIGATION = NotebookMetadataType("investigation")
NotebookMetadataType.DOCUMENTATION = NotebookMetadataType("documentation")
NotebookMetadataType.REPORT = NotebookMetadataType("report")
