# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ContainerStateTerminatedDto(BaseModel):
    """
    ContainerStateTerminatedDto
    """ # noqa: E501
    exit_code: StrictInt
    exit_code_message: StrictStr
    finished_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    message: StrictStr
    reason: StrictStr
    signal: StrictInt
    started_at: Optional[StrictInt] = Field(default=None, description="Unix timestamp with millisecond precision")
    __properties: ClassVar[List[str]] = ["exit_code", "exit_code_message", "finished_at", "message", "reason", "signal", "started_at"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ContainerStateTerminatedDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if finished_at (nullable) is None
        # and model_fields_set contains the field
        if self.finished_at is None and "finished_at" in self.model_fields_set:
            _dict['finished_at'] = None

        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['started_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ContainerStateTerminatedDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exit_code": obj.get("exit_code"),
            "exit_code_message": obj.get("exit_code_message"),
            "finished_at": obj.get("finished_at"),
            "message": obj.get("message"),
            "reason": obj.get("reason"),
            "signal": obj.get("signal"),
            "started_at": obj.get("started_at")
        })
        return _obj


